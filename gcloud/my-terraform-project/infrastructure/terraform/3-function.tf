# 3-function.tf

resource "google_storage_bucket" "function_source_bucket" {
  name          = "${var.bucket_name}-function-source"
  location      = var.region
  force_destroy = true
}

resource "google_storage_bucket_object" "function_source_archive" {
  name   = "${var.function_name}.zip"
  bucket = google_storage_bucket.function_source_bucket.name
  source = "cloud-functions-files/cloud_function_code.zip"
}

resource "google_cloudfunctions_function" "function" {
  name        = var.function_name
  description = "My Cloud Function"
  runtime     = var.function_runtime
  region      = var.region
  entry_point = var.function_entry_point

  source_archive_bucket = google_storage_bucket.function_source_bucket.name
  source_archive_object = google_storage_bucket_object.function_source_archive.name

  trigger_http = true

  available_memory_mb   = 256
  timeout               = 60

  ingress_settings      = "ALLOW_ALL"

  environment_variables = {
    BUCKET_NAME = google_storage_bucket.data_bucket.name
  }
}
