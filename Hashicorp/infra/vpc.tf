##••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••##
## definiendo los recursos que corresponden con la configuracion de la VPC      ##
##••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••##
#------------------------------------------------------------#
# Resources configuration Block - VPC                        #
#------------------------------------------------------------#
#Creacion de la nueva VPC
resource "aws_vpc" "sample_tf_vpc" {
  cidr_block       = "10.0.0.0/16"
  #deafult te permite desplegar las instancias en HW compartido
  instance_tenancy = "default"
  enable_dns_support = true
  enable_dns_hostnames = true
  enable_classiclink = false
  tags = {
    Name = "sample_tf_vpc"
  }
}

#------------------------------------------------------------#
# Resources configuration Block - Subnet Private             #
#------------------------------------------------------------#
resource "aws_subnet" "private_tf_subnet_a" {
  vpc_id     = aws_vpc.sample_tf_vpc.id
  cidr_block = "10.0.4.0/24"
  map_public_ip_on_launch = "false"
  availability_zone = "us-west-2a"
  tags = {
    Name = "private_tf_subnet_a"
  }
}
