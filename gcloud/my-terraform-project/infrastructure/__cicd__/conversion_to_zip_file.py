import os
import zipfile

def create_zip(source_dir, output_dir, zip_name):
    """
    Zips the contents of source_dir into a zip file named zip_name located in output_dir.
    
    Args:
        source_dir (str): Path to the directory containing the Cloud Function code.
        output_dir (str): Path to the directory where the zip file will be saved.
        zip_name (str): Name of the resulting zip file.
    """
    # Ensure the source directory exists
    if not os.path.isdir(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Ensure the output directory exists; if not, create it
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory '{output_dir}'.")

    zip_path = os.path.join(output_dir, zip_name)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the source directory
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Arcname ensures the file is at the root of the zip
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
                print(f"Added '{file_path}' as '{arcname}'.")

    print(f"Zip file created at '{zip_path}'.")

if __name__ == "__main__":
    # Define paths
    source_directory = r"C:\terraform\my-terraform-project\data-services\v1\ingestion\cloud_functions"
    output_directory = r"C:\terraform\my-terraform-project\infrastructure\terraform\cloud-functions-files"
    zip_filename = "cloud_function_code.zip"

    create_zip(source_directory, output_directory, zip_filename)
