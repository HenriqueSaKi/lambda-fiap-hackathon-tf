resource "aws_lambda_function" "fiap_lambda_function" {
  filename      = "lambda_email_sender.zip"
  function_name = "FiapHackathonSendEmail"
  role          = "arn:aws:iam::${var.accountId}:role/LabRole"
  handler       = "index.test"

  source_code_hash = data.archive_file.lambda.output_base64sha256

  runtime = "python3.13"

  environment {
    variables = {
      Environment = "development"
    }
  }
}