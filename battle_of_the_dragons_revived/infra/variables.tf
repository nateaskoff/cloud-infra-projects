variable "aws_account_id" {
  type        = string
  description = "AWS Account ID"
  sensitive   = true
}

variable "assume_role_name" {
  type        = string
  description = "The name of the role to assume"
  sensitive   = true
}

variable "env" {
  type        = string
  description = "The environment to deploy to"
  default     = "dev"
}

variable "github_sha" {
  type        = string
  description = "The GitHub SHA to deploy"
}
