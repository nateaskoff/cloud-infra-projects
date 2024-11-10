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
  assume_role_with_web_identity {
    role_arn                = "arn:aws:iam::${var.account_id}:role/${var.assume_role_name}"
    web_identity_token_file = "/github/workspace/.aws/oidc-token"
  }
}

module "botdr" {
  source        = "./botdr"
  env           = var.env
  fly_io_app_ip = var.fly_io_app_ip
}
