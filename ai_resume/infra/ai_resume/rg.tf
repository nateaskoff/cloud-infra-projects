resource "azurerm_resource_group" "rg" {
  name     = "${var.env}-rg-ai-resume"
  location = var.az_location
}
