provider "aws" {
  region = var.region
}

module "vpc" {
    source = "../../../aws/modules/vpc/vpc/"

    vpc_cidr = "${var.vpc_cidr}"
}
