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
| [aws_iam_user.botdr_fly_io_user](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/iam_user) | resource |
| [aws_iam_user_policy.botdr_fly_io_user_policy](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/iam_user_policy) | resource |
| [aws_kms_alias.botdr_key_alias](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/kms_alias) | resource |
| [aws_kms_key.botdr_key](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/kms_key) | resource |
| [aws_route53_record.botdr_web](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/route53_record) | resource |
| [aws_route53_record.web_cert_val_record](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/route53_record) | resource |
| [aws_s3_bucket.mod_bucket](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/s3_bucket) | resource |
| [aws_s3_bucket.web_bucket](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/s3_bucket) | resource |
| [aws_s3_bucket_lifecycle_configuration.web_bucket_lifecycle](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/s3_bucket_lifecycle_configuration) | resource |
| [aws_s3_bucket_policy.web_bucket_policy](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/s3_bucket_policy) | resource |
| [aws_s3_bucket_public_access_block.mod_bucket_acc_blk](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/s3_bucket_public_access_block) | resource |
| [aws_s3_bucket_public_access_block.web_bucket_acc_blk](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/s3_bucket_public_access_block) | resource |
| [aws_s3_bucket_server_side_encryption_configuration.web_bucket_sse](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/resources/s3_bucket_server_side_encryption_configuration) | resource |
| [aws_caller_identity.current](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/data-sources/caller_identity) | data source |
| [aws_iam_policy_document.botdr_fly_io_user_policy_doc](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.s3_web_bucket_policy](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/data-sources/iam_policy_document) | data source |
| [aws_route53_zone.botdr_zone](https://registry.terraform.io/providers/hashicorp/aws/5.75.0/docs/data-sources/route53_zone) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_env"></a> [env](#input\_env) | The environment to deploy to | `string` | n/a | yes |

## Outputs

No outputs.
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
