terraform {
  backend "azurerm" {
    resource_group_name  = "rg-abdi-dev-uks"
    storage_account_name = "tfbackendfuncapp"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}
