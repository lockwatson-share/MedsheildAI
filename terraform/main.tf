provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "medical_data_bucket" {
  bucket = "medshield-ai-secure-data"

  versioning {
    enabled = true
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    Project     = "MedShield AI"
    Compliance  = "HIPAA-CCPA"
    Environment = "Research"
  }
}

resource "aws_iam_role" "agent_role" {
  name = "medshield-ai-agent-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}