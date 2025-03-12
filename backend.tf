terraform {
  backend "s3" {
    bucket = "fiap-hackathon-terraform-state-bucket"
    key    = "lambda/terraform.tfstate"
    region = "us-east-1"
  }
}