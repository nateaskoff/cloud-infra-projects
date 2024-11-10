# infra

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | 1.9.8 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | 5.75.0 |

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_botdr"></a> [botdr](#module\_botdr) | ./botdr | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_account_id"></a> [account\_id](#input\_account\_id) | The AWS account ID | `string` | n/a | yes |
| <a name="input_assume_role_name"></a> [assume\_role\_name](#input\_assume\_role\_name) | The name of the role to assume | `string` | n/a | yes |
| <a name="input_env"></a> [env](#input\_env) | The environment to deploy to | `string` | `"dev"` | no |
| <a name="input_fly_io_app_ip"></a> [fly\_io\_app\_ip](#input\_fly\_io\_app\_ip) | The IP address of the Fly.io app | `string` | n/a | yes |

## Outputs

No outputs.
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
