resource "azurerm_storage_account" "storage_account" {
  #checkov:skip=CKV_AZURE_33:no private endpoint for hobby project
  #checkov:skip=CKV_AZURE_206:no replication needed for hobby projects
  name                            = "${var.env}airesumestac"
  resource_group_name             = azurerm_resource_group.rg.name
  location                        = azurerm_resource_group.rg.location
  account_tier                    = "Standard"
  account_kind                    = "StorageV2"
  account_replication_type        = "LRS"
  local_user_enabled              = false
  public_network_access_enabled   = false
  allow_nested_items_to_be_public = false
  shared_access_key_enabled       = false
  min_tls_version                 = "TLS1_2"

  blob_properties {
    delete_retention_policy {
      days = 7
    }
  }

  sas_policy {
    expiration_period = "90.00:00:00"
    expiration_action = "Log"
  }

  queue_properties {
    logging {
      delete                = true
      read                  = true
      write                 = true
      version               = "1.0"
      retention_policy_days = 1
    }
    hour_metrics {
      enabled               = true
      include_apis          = true
      retention_policy_days = 1
      version               = "1.0"
    }
    minute_metrics {
      enabled               = true
      include_apis          = true
      retention_policy_days = 1
      version               = "1.0"
    }
  }
}

resource "azurerm_storage_account_customer_managed_key" "storage_account_cmk" {
  storage_account_id = azurerm_storage_account.storage_account.id
  key_vault_id       = azurerm_key_vault_key.key_vault_key.id
  key_name           = azurerm_key_vault_key.key_vault_key.name
}
