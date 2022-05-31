#------------------------------------------------------------#
# Resources configuration Block - Key Pair                   #
#------------------------------------------------------------#

#------------------------------------------------------------#
# Resources configuration Block - Instance                   #
#------------------------------------------------------------#
resource "aws_instance" "MyInstance" {
  #AMI Image se puede obtener desde ami finder de la distro
  ami           = lookup(var.AMIS, var.AWS_REGION)
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.private_tf_subnet_a.id
  vpc_security_group_ids = [ aws_security_group.allow_sample_vpc_ssh.id ]
  tags = {
    #se hace referencia al indice de la variable 
    "Name" = "tfdemo"
  }
}

