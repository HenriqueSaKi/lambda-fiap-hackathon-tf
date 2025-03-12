data "archive_file" "lambda" {
  type        = "zip"
  source_file = "lambda_email_sender.py"
  output_path = "lambda_email_sender.zip"
}