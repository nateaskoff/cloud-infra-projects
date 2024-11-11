variable "env" {
  type        = string
  description = "The environment to deploy to"
  default     = "dev"
}

variable "fly_io_app_ip" {
  type        = string
  description = "The IP address of the Fly.io app"
}
