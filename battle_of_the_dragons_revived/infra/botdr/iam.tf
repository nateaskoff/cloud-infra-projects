resource "aws_iam_user" "botdr_fly_io_user" {
  #checkov:skip=CKV_AWS_273
  name = "${var.env}-botdr-fly-io-user"
}

resource "aws_iam_user_policy" "botdr_fly_io_user_policy" {
  name = "${var.env}-botdr-fly-io-user-policy"
  user = aws_iam_user.botdr_fly_io_user.name

  policy = data.aws_iam_policy_document.botdr_fly_io_user_policy_doc.json
}
