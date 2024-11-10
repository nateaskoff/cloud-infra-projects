resource "aws_s3_bucket" "web_bucket" {
  #checkov:skip=CKV_AWS_300
  #checkov:skip=CKV2_AWS_61:github deploy is the lifecycle
  #checkov:skip=CKV_AWS_21:versioning is in github
  #checkov:skip=CKV_AWS_145:cannot use kms with cloudfront
  #checkov:skip=CKV2_AWS_62
  #checkov:skip=CKV_AWS_18
  #checkov:skip=CKV_AWS_144
  bucket        = "${lower(var.env)}-botdr-primary-site-web-bucket"
  force_destroy = true
}

resource "aws_s3_bucket_public_access_block" "web_bucket_acc_blk" {
  bucket = aws_s3_bucket.web_bucket.id

  ignore_public_acls      = true
  restrict_public_buckets = true
  block_public_acls       = true
  block_public_policy     = true
}

resource "aws_s3_bucket_policy" "web_bucket_policy" {
  bucket = aws_s3_bucket.web_bucket.id
  policy = data.aws_iam_policy_document.s3_web_bucket_policy.json
}
