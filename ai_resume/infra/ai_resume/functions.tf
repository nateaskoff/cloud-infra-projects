resource "azurerm_service_plan" "open_ai_svc_plan" {
  #checkov:skip=CKV_AZURE_212:hobby project, no need for minimum instance failover
  #checkov:skip=CKV_AZURE_225:hobby project, zone redundancy not needed
  name                = "${var.env}-sp-openai"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "P1v2"
}

resource "azurerm_linux_function_app" "open_ai_function_app" {
  name                = "${var.env}-lnx-fa-openai"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  storage_account_name       = azurerm_storage_account.storage_account.name
  storage_account_access_key = azurerm_storage_account.storage_account.primary_access_key
  service_plan_id            = azurerm_service_plan.open_ai_svc_plan.id

  https_only                    = true
  public_network_access_enabled = false

  site_config {
    linux_fx_version = "PYTHON|3.12"
  }
}
