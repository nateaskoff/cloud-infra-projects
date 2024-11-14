resource "azurerm_virtual_network" "vnet" {
  name                = "${var.env}-vnet-ai-resume"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  address_space = [
    "10.0.0.0/16"
  ]
  dns_servers = [
    "10.0.0.4",
    "10.0.0.5"
  ]
}

resource "azurerm_subnet" "subnet" {
  name                 = "${var.env}-subnet-ai-resume"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes = [
    "10.0.1.0/24"
  ]
}
