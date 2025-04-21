variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "rg-terraform-test"
}

variable "location" {
  description = "Azure location"
  type        = string
  default     = "UK South"
}
