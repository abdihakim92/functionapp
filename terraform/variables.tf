variable "location" {
  description = "Azure location"
  type        = string
  default     = "UK South"
}

variable "storage_account_name" {
  default = "compoundcalcstor"
}

variable "app_service_plan_name" {
  default = "compoundcalc-plan"
}

variable "function_app_name" {
  default = "compoundcalc-func"
}
