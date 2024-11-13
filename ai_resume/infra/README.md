# infra

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | 1.9.8 |
| <a name="requirement_azurerm"></a> [azurerm](#requirement\_azurerm) | 4.9.0 |

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_ai_resume"></a> [ai\_resume](#module\_ai\_resume) | ./ai_resume | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_az_location"></a> [az\_location](#input\_az\_location) | The Azure location to deploy to | `string` | n/a | yes |
| <a name="input_client_id"></a> [client\_id](#input\_client\_id) | The Azure client ID | `string` | n/a | yes |
| <a name="input_container_name"></a> [container\_name](#input\_container\_name) | The Azure storage container name | `string` | n/a | yes |
| <a name="input_env"></a> [env](#input\_env) | The environment to deploy to | `string` | n/a | yes |
| <a name="input_github_oidc_request_token"></a> [github\_oidc\_request\_token](#input\_github\_oidc\_request\_token) | The GitHub OIDC request token | `string` | n/a | yes |
| <a name="input_github_oidc_request_url"></a> [github\_oidc\_request\_url](#input\_github\_oidc\_request\_url) | The GitHub OIDC request URL | `string` | n/a | yes |
| <a name="input_resource_group_name"></a> [resource\_group\_name](#input\_resource\_group\_name) | The Azure resource group name | `string` | n/a | yes |
| <a name="input_state_key"></a> [state\_key](#input\_state\_key) | The Azure storage state key | `string` | n/a | yes |
| <a name="input_storage_account_name"></a> [storage\_account\_name](#input\_storage\_account\_name) | The Azure storage account name | `string` | n/a | yes |
| <a name="input_subscription_id"></a> [subscription\_id](#input\_subscription\_id) | The Azure subscription ID | `string` | n/a | yes |
| <a name="input_tenant_id"></a> [tenant\_id](#input\_tenant\_id) | The Azure tenant ID | `string` | n/a | yes |

## Outputs

No outputs.
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
