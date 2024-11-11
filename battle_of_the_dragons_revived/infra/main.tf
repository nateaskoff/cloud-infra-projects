terraform {
  required_version = "1.9.8"

  cloud {
    organization = "cloud-infra-projects"
    hostname     = "app.terraform.io"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.75.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
  assume_role_with_web_identity {}
}

module "botdr" {
  source = "./botdr"
  env    = var.env
}
