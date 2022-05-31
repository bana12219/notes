#------------------------------------------------------------#
# Vars configuration Block - AWS related                     #
#------------------------------------------------------------#
variable "AWS_REGION"{
    default="us-west-2"
}
variable "AWS_DEFAULT_REGION"{
    default="us-west-2"
}
variable "AWS_DEFAULT_AZ"{
    default="us-west-2a"
}

#AMI by region map
variable "AMIS" {
    type        = map
    description = "mapa de amis por region"
    default     = {
        us-east-1  = "ami-099e-----356cf89"
        us-west-2 = "ami-00f----858"
        }
}

