# 1-variables.tf

variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region"
  type        = string
  default     = "us-central1"
}

variable "credentials_file" {
  description = "Path to the GCP credentials JSON file"
  type        = string
}

variable "bucket_name" {
  description = "The name of the Cloud Storage bucket"
  type        = string
}

variable "function_name" {
  description = "The name of the Cloud Function"
  type        = string
}

variable "function_entry_point" {
  description = "The entry point of the Cloud Function"
  type        = string
  default     = "hello_world"
}

variable "function_runtime" {
  description = "The runtime of the Cloud Function"
  type        = string
  default     = "python39"
}

variable "source_code_path" {
  description = "Path to the zipped Cloud Function source code"
  type        = string
  default     = "cloud-functions-files/cloud_function_code.zip"
}
