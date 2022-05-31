terraform {
  backend "remote" {
    organization = var.TF_ORGANIZATION
    hostname     = var.TF_HOST
    workspaces {
      name = var.TF_WORKSPACE
    }
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}

provider "aws" {
#le dice a terraform que perfil utilizar
#Note: If you leave out your AWS credentials, Terraform will automatically search 
#for saved API credentials (for example, in ~/.aws/credentials) or IAM instance 
#profile credentials. This is cleaner when .tf files are checked into source control 
#or if there is more than one admin user.
  profile = "default"
  region  = var.AWS_REGION
}

#resource "aws_instance" "example" {
#  ami           = "ami-830c94e3"
#  instance_type = "t2.micro"
  #si presenta fallos puede requerir datos sobre la vpc
  #esto si no hay una default
  #vpc_security_group_ids = ["sg-0077..."]
  #subnet_id              = "subnet-923a..."
#}

