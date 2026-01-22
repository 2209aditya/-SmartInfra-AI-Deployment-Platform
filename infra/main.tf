provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "model_bucket" {
  bucket = "smartinfra-model-bucket"
  acl    = "private"
}
