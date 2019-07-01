terraform {
  backend "remote" {
    hostname = "app.terraform.io"
    organization = "joaoclaudio"

    workspaces {
      name = "my-vpc"
    }
  }
}
