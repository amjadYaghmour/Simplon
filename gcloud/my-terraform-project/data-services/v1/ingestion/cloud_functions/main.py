from flask import Request, jsonify
from google.cloud import storage
import pandas as pd
import pyarrow.parquet as pq
import io

def csvtoparquet(request: Request):
    try:
        request_json = request.get_json(silent=True)
        if not request_json:
            return jsonify({'error': 'Invalid request, JSON body missing'}), 400

        bucket_name = request_json.get('bucket')

        if not bucket_name:
            return jsonify({'error': 'Missing bucket in request'}), 400

        # Define the folder paths
        CSV_FOLDER = 'Bronze/CSV'
        PARQUET_FOLDER = 'Bronze/Parquet'

        # Initialize the Google Cloud Storage client
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)

        # List all files in the 'Bronze/CSV/' folder
        blobs = bucket.list_blobs(prefix=CSV_FOLDER)

        processed_files = []

        for blob in blobs:
            file_name = blob.name

            # Process only CSV files
            if file_name.endswith('.csv'):
                try:
                    # Download CSV content directly
                    csv_content = blob.download_as_text()

                    # Convert CSV content to pandas DataFrame
                    df = pd.read_csv(io.StringIO(csv_content))

                    # Convert DataFrame to Parquet in-memory
                    parquet_buffer = io.BytesIO()
                    df.to_parquet(parquet_buffer, engine='pyarrow')
                    parquet_buffer.seek(0)  # Rewind the buffer

                    # Define the Parquet file path
                    parquet_file_name = file_name.replace(CSV_FOLDER, PARQUET_FOLDER).replace('.csv', '.parquet')

                    # Upload the Parquet file directly to GCS
                    parquet_blob = bucket.blob(parquet_file_name)
                    parquet_blob.upload_from_file(parquet_buffer, content_type='application/octet-stream')

                    processed_files.append(parquet_file_name)
                except Exception as e:
                    print(f"Error processing file {file_name}: {e}")
            else:
                print(f"Skipping non-CSV file: {file_name}")

        return jsonify({'message': 'Successfully processed files', 'processed_files': processed_files}), 200

    except Exception as e:
        print(f"Function error: {e}")
        return jsonify({'error': str(e)}), 500
