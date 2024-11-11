resource "aws_kms_key" "botdr_key" {
  #checkov:skip=CKV_AWS_7:no rotation for now
  description             = "KMS key for BotDR"
  deletion_window_in_days = 10
  policy = jsonencode({
    Version = "2012-10-17",
    Id      = "key-default-1",
    Statement = [
      {
        Sid    = "Enable IAM User Permissions",
        Effect = "Allow",
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        },
        Action   = "kms:*",
        Resource = "*"
      }
    ]
  })
}

resource "aws_kms_alias" "botdr_key_alias" {
  name          = "alias/${var.env}-botdr-key"
  target_key_id = aws_kms_key.botdr_key.id
}
