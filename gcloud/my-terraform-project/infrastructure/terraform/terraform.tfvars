

# terraform.tfvars

project_id           = "soy-objective-437607-n5"
credentials_file     = "../credentials/key.json"  # Ensure this path is correct
bucket_name          = "amjadteststorage"
function_name        = "csvtoparquet"
function_entry_point = "csvtoparquet"                   # Entry point function in your code
function_runtime     = "python39"                       # Runtime environment
source_code_path     = "cloud-functions-files/cloud_function_code.zip"  # Path to your zipped function code
