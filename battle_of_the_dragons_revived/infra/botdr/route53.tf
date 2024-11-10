resource "aws_route53_record" "botdr_app" {
  zone_id = data.botdr_zone.botdr.zone_id
  name    = "app-${var.env}.battleofthedragonsrevived.com"
  type    = "A"
  ttl     = "300"
  records = [
    var.fly_io_app_ip
  ]
}

resource "aws_route53_record" "botdr_web" {

}
