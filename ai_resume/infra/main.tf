terraform {
  required_version = "1.9.8"

  backend "azurerm" {}

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.9.0"
    }
  }
}

provider "azurerm" {
  features {}
}

module "ai_resume" {
  source      = "./ai_resume"
  env         = var.env
  az_location = var.az_location
}
