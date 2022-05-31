#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••#
# definiendo de security group de la VPC sample_tf_vpc                         #
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••#
#------------------------------------------------------------#
# Resources configuration Block - Security Group             #
#------------------------------------------------------------#
resource "aws_security_group" "allow_sample_vpc_ssh"{
    vpc_id = aws_vpc.sample_tf_vpc.id
    name = "allow_sample_vpc_ssh"
    description = "This security groups allows ssh connections from anywhere to allow_sample_vpc_ssh"
    egress =  {
      cidr_blocks = [ "0.0.0.0/0" ]
      description = "egress allow_sample_vpc_ssh rule all protocols anywhere"
      from_port = 0
      #-1 significa todos los protocolos, 
      #lo que es aplicable a AWs 
      #podría ser especifico, ssolo la lista de protocolos permitidos
      protocol = "-1"
      to_port = 0
    } 
    tags = {
      Name = "allow_sample_vpc_ssh"
    }
}