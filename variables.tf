variable "prefix" {
 description = "The prefix used for all resources in this environment"
}

variable "location" {
  description = "The Azure location where all resources in this deployment should be created"
  default     = "uksouth"
}
variable "client_id" {
  description = "OAUTH CLIENT ID"
  sensitive = true
}
variable "client_secret" {
  description = "OAUTH CLIENT SECRET"
  sensitive = true
}
variable "secret_key" {
  description = "SECRET KEY"
  sensitive = true
}
