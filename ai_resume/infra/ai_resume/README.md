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
| [azurerm_resource_group.rg](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/resource_group) | resource |
| [azurerm_storage_account.storage_account](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/storage_account) | resource |
| [azurerm_storage_queue_properties.storage_account_queue_properties](https://registry.terraform.io/providers/hashicorp/azurerm/4.9.0/docs/resources/storage_queue_properties) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_az_location"></a> [az\_location](#input\_az\_location) | The Azure location to deploy to | `string` | n/a | yes |
| <a name="input_env"></a> [env](#input\_env) | The environment to deploy to | `string` | n/a | yes |

## Outputs

No outputs.
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
