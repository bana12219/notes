#terraform {
#  backend "remote" {
#    organization = "Wizedemo"
#
#
#    workspaces {
#      name = "wizedemo"
#    }
#  }
#  required_providers {
#    aws = {
#3      source  = "hashicorp/aws"
#      version = "~> 3.26.0"
#3    }
#  }
#}
terraform {
  backend "remote" {
    hostname = "app.terraform.io"
    organization = "Wizedemo"

    workspaces {
      name = "wizedemows"
    }
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.26.0"
    }
  }
}
provider "aws" {

  region  = "us-west-2"
}
resource "aws_instance" "example" {
  ami           = "ami-00f1e37d20049f858"
  instance_type = "t2.micro"

}


Terraform Cloud detected a terraform.tfstate file in your working
directory: ./terraform.tfstate

The presence of this file causes a state migration error which prevents
Terraform from running successfully. To fix this error please migrate
your local terraform.tfstate to Terraform Cloud and make sure the
the file is deleted.

For step by step instructions on how to migrate your terraform.tfstate
file from Terraform Open Source to Terraform Cloud, please see:

   https://www.terraform.io/docs/enterprise/migrate/index.html