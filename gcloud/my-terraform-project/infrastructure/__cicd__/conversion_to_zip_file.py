import os
import zipfile
import subprocess

def install_dependencies(source_dir):
    """
    Installs dependencies from requirements.txt into the source directory.
    Google Cloud Functions will handle dependency installation during deployment.
    """
    requirements_path = os.path.join(source_dir, 'requirements.txt')
    
    if not os.path.isfile(requirements_path):
        print(f"Error: 'requirements.txt' not found at '{requirements_path}'.")
        return False

    print("Verifying dependencies...")
    try:
        # Optionally, verify if dependencies can be installed (local check)
        subprocess.check_call(['pip', 'install', '--dry-run', '-r', requirements_path])
        print("Dependencies verification passed.")
    except subprocess.CalledProcessError as e:
        print(f"Error verifying dependencies: {e}")
        return False

    # No need to install dependencies locally
    return True

def zip_function(source_dir, output_dir, zip_name):
    """
    Zips main.py and requirements.txt into cloud_function_code.zip
    """
    zip_path = os.path.join(output_dir, zip_name)
    print(f"Creating zip file at '{zip_path}'...")

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add main.py
        main_py = os.path.join(source_dir, 'main.py')
        if os.path.isfile(main_py):
            zipf.write(main_py, arcname='main.py')
            print("Added 'main.py' to zip.")
        else:
            print("Warning: 'main.py' does not exist.")

        # Add requirements.txt
        req_txt = os.path.join(source_dir, 'requirements.txt')
        if os.path.isfile(req_txt):
            zipf.write(req_txt, arcname='requirements.txt')
            print("Added 'requirements.txt' to zip.")
        else:
            print("Warning: 'requirements.txt' does not exist.")

    # Verify if the zip file was created
    if os.path.isfile(zip_path):
        print(f"Zip file successfully created at '{zip_path}'.")
    else:
        print(f"Error: Failed to create zip file at '{zip_path}'.")

    # List contents of the output directory
    print(f"Contents of '{output_dir}':")
    for item in os.listdir(output_dir):
        print(f" - {item}")

def main():
    # Define paths
    source_directory = r"C:\Users\HP\Documents\Simplon\projects\intensif\week7\gcloud\Simplon\gcloud\my-terraform-project\data-services\v1\ingestion\cloud_functions"
    output_directory = r"C:\terraform\my-terraform-project\infrastructure\terraform\cloud-functions-files"
    zip_filename = "cloud_function_code.zip"

    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created output directory '{output_directory}'.")
    else:
        print(f"Output directory already exists at '{output_directory}'.")

    # Install dependencies (verification only)
    if install_dependencies(source_directory):
        # Create the zip file
        zip_function(source_directory, output_directory, zip_filename)
    else:
        print("Failed to verify dependencies. Zip file not created.")

if __name__ == "__main__":
    main()
