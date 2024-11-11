terraform {
  required_version = "1.9.8"

  backend "local" {
    path = "terraform.tfstate"
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
}

module "botdr" {
  source = "./botdr"
  env    = var.env
}
