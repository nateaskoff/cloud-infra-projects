variable "env" {
  description = "The environment to deploy to"
  type        = string
}

variable "az_location" {
  description = "The Azure location to deploy to"
  type        = string
}

variable "tenant_id" {
  description = "The Azure tenant ID"
  type        = string
}

variable "subscription_id" {
  description = "The Azure subscription ID"
  type        = string
}

variable "client_id" {
  description = "The Azure client ID"
  type        = string
}

variable "github_oidc_request_token" {
  description = "The GitHub OIDC request token"
  type        = string
}

variable "github_oidc_request_url" {
  description = "The GitHub OIDC request URL"
  type        = string
}
