# botdr

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | 1.9.8 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | 5.75.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | 5.75.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_acm_certificate.web_cert](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/acm_certificate) | resource |
| [aws_acm_certificate_validation.web_cert_val](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/acm_certificate_validation) | resource |
| [aws_cloudfront_distribution.cf_dist_botdr_web](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/cloudfront_distribution) | resource |
| [aws_cloudfront_origin_access_control.default](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/cloudfront_origin_access_control) | resource |
| [aws_cloudfront_response_headers_policy.default](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/cloudfront_response_headers_policy) | resource |
| [aws_route53_record.botdr_app](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/route53_record) | resource |
| [aws_route53_record.botdr_web](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/route53_record) | resource |
| [aws_route53_zone.botdr_zone](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/data-sources/route53_zone) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_env"></a> [env](#input\_env) | The environment to deploy to | `string` | `"dev"` | no |
| <a name="input_fly_io_app_ip"></a> [fly\_io\_app\_ip](#input\_fly\_io\_app\_ip) | The IP address of the Fly.io app | `string` | n/a | yes |

## Outputs

No outputs.
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
