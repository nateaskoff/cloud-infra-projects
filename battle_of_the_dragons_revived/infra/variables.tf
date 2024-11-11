variable "account_id" {
  type        = string
  description = "The AWS account ID"
  sensitive   = true
}

variable "assume_role_name" {
  type        = string
  description = "The name of the role to assume"
  sensitive   = true
}

variable "web_identity_token" {
  type        = string
  description = "The AWS Web Identity Token"
  sensitive   = true
}

variable "env" {
  type        = string
  description = "The environment to deploy to"
  default     = "dev"
}

variable "fly_io_app_ip" {
  type        = string
  description = "The IP address of the Fly.io app"
}
