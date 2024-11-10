resource "aws_s3_bucket" "web_bucket" {
  #checkov:skip=CKV_AWS_300
  bucket        = "${lower(var.aws_env)}-botdr-primary-site-web-bucket"
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
