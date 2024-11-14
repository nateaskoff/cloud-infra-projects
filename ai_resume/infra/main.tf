terraform {
  required_version = "1.9.8"

  backend "azurerm" {}

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.8.0"
    }
  }
}

provider "azurerm" {
  features {}
  use_oidc           = true
  tenant_id          = var.tenant_id
  subscription_id    = var.subscription_id
  client_id          = var.client_id
  oidc_request_token = var.github_oidc_request_token
  oidc_request_url   = var.github_oidc_request_url
}

module "ai_resume" {
  source      = "./ai_resume"
  env         = var.env
  az_location = var.az_location
}
