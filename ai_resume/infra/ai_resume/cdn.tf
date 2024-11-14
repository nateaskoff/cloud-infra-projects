resource "azurerm_cdn_profile" "cdn_profile" {
  name                = "${var.env}-cdn-profile-ai-resume"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Standard_Microsoft"
}

resource "azurerm_cdn_endpoint" "cdn_endpoint" {
  name                = "${var.env}-cdn-endpoint-ai-resume"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  profile_name        = azurerm_cdn_profile.cdn_profile.name

  origin {
    name      = "${var.env}-cdn-endpoint-ai-resume-origin"
    host_name = azurerm_storage_account.storage_account.primary_blob_endpoint
  }

  is_http_allowed = false
}
