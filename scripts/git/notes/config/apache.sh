#!/bin/bash
yum update -y
#instalando apache
yum install -y httpd
#levantando servicio
systemctl start httpd.service
#alternativas cuando no se encuentra el comando por la configuracion de la maquina
#---- aqui la alternativa
systemctl enable httpd.service
echo "hola mundo" > /var/www/hmtml/index.html
