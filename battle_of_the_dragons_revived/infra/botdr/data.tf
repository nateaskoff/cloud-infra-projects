data "aws_caller_identity" "current" {}

data "aws_route53_zone" "botdr_zone" {
  name = "battleofthedragonsrevived.com"
}

data "aws_iam_policy_document" "s3_web_bucket_policy" {
  statement {
    actions = [
      "s3:GetObject"
    ]

    resources = [
      aws_s3_bucket.web_bucket.arn,
      "${aws_s3_bucket.web_bucket.arn}/*"
    ]

    principals {
      type = "Service"
      identifiers = [
        "cloudfront.amazonaws.com"
      ]
    }

    condition {
      test     = "StringEquals"
      variable = "aws:SourceArn"
      values = [
        "arn:aws:cloudfront::${data.aws_caller_identity.current.account_id}:distribution/${aws_cloudfront_distribution.cf_dist_botdr_web.id}"
      ]
    }
  }
}

data "aws_iam_policy_document" "botdr_fly_io_user_policy_doc" {
  statement {
    actions = [
      "kms:*"
    ]

    resources = [
      aws_kms_key.botdr_key.arn
    ]
  }

  statement {
    actions = [
      "s3:GetObject",
      "s3:ListBucket"
    ]

    resources = [
      aws_s3_bucket.mod_bucket.arn,
      "${aws_s3_bucket.mod_bucket.arn}/*"
    ]
  }
}
