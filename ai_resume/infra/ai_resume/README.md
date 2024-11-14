# ai_resume

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | 1.9.8 |
| <a name="requirement_azurerm"></a> [azurerm](#requirement\_azurerm) | 4.9.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_azurerm"></a> [azurerm](#provider\_azurerm) | 4.9.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [azurerm_cdn_endpoint.cdn_endpoint](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/cdn_endpoint) | resource |
| [azurerm_cdn_profile.cdn_profile](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/cdn_profile) | resource |
| [azurerm_key_vault.key_vault](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/key_vault) | resource |
| [azurerm_key_vault_access_policy.key_vault_access_policy](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/key_vault_access_policy) | resource |
| [azurerm_key_vault_key.key_vault_key](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/key_vault_key) | resource |
| [azurerm_network_security_group.vnet_sec_group](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/network_security_group) | resource |
| [azurerm_private_endpoint.key_vault_private_endpoint](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/private_endpoint) | resource |
| [azurerm_private_endpoint.storage_account_private_endpoint](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/private_endpoint) | resource |
| [azurerm_resource_group.rg](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/resource_group) | resource |
| [azurerm_storage_account.storage_account](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/storage_account) | resource |
| [azurerm_storage_account_customer_managed_key.storage_account_cmk](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/storage_account_customer_managed_key) | resource |
| [azurerm_subnet.subnet](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/subnet) | resource |
| [azurerm_subnet_network_security_group_association.subnet_nsg_association](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/subnet_network_security_group_association) | resource |
| [azurerm_virtual_network.vnet](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/virtual_network) | resource |
| [azurerm_client_config.current](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/data-sources/client_config) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_az_location"></a> [az\_location](#input\_az\_location) | The Azure location to deploy to | `string` | n/a | yes |
| <a name="input_env"></a> [env](#input\_env) | The environment to deploy to | `string` | n/a | yes |

## Outputs

No outputs.
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
