provider "aws" {
  version = "~> 2.70"
  region = var.region
}

locals {
  module_tag = "${var.project}-${var.namespace}-${var.stage}"
  tags = "${map(
    "project", "${var.project}",
    "environment", "${var.stage}",
    "namespace", "${var.namespace}"
  )}"
}

### NETWORKING ###
resource "aws_vpc" "octobuy_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support = true
  tags = local.tags
}

resource "aws_eip" "octobuy_eip" {
  instance = aws_instance.baremetal.id
  vpc = true
}

resource "aws_route53_record" "route53_record" {
  zone_id = var.hosted_zone_id
  name    = "octobuy-app.com"
  type    = "A"
  ttl     = "300"
  records = ["${aws_eip.octobuy_eip.public_ip}"]
}

resource "aws_internet_gateway" "octobuy_gateway" {
  vpc_id = aws_vpc.octobuy_vpc.id
  tags = local.tags
}

resource "aws_subnet" "octobuy_subnet" {
  cidr_block = cidrsubnet(aws_vpc.octobuy_vpc.cidr_block, 3, 1)
  vpc_id = aws_vpc.octobuy_vpc.id
  availability_zone = "eu-west-2a"


}

resource "aws_route_table" "octobuy_route_table" {
  vpc_id = aws_vpc.octobuy_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.octobuy_gateway.id
  }
  tags = local.tags
}
resource "aws_route_table_association" "octobuy_subnet_association" {
  subnet_id = aws_subnet.octobuy_subnet.id
  route_table_id = aws_route_table.octobuy_route_table.id
}


resource "aws_security_group" "octobuy_security_group" {
  name = "${local.module_tag}-sg"
  vpc_id = aws_vpc.octobuy_vpc.id

  ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
    from_port = 22
    to_port = 22
    protocol = "tcp"
  }

  ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
    from_port = 6080
    to_port = 6080
    protocol = "tcp"
  }

    ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
    from_port = 4444
    to_port = 4444
    protocol = "tcp"
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }
}

### BAREMETAL INSTANCE ###
resource "aws_instance" "baremetal" {
  ami = "ami-00f6a0c18edb19300"
  instance_type = "c5n.metal"
  key_name = "metal"
  security_groups = [aws_security_group.octobuy_security_group.id]
  subnet_id = aws_subnet.octobuy_subnet.id
  tags = local.tags

  root_block_device {
      volume_size = 80
  }
}

resource "aws_s3_bucket" "baremetal" {
  bucket = "baremetal.bucket"

  versioning {
    enabled = true
  }
}

resource "aws_s3_bucket_object" "file_upload" {
  bucket = "baremetal.bucket"
  key    = "Nike.apk"
  source = "${path.module}/provision/Nike.apk"
  etag   = "${filemd5("${path.module}/provision/Nike.apk")}"
}
