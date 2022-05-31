#saber los shells 
#shebang = bin bash
cat /etc/shells 
#saber el bash que ejecutamos
which bash

#grep [opt] "pattern" file/*    <- pattern matches in fle
#  -i no case sensitive
#  -w exactamente la palabra
#  -v complemento de es decir las que no contengan pattern
#  -o muestra solo las partes que hacen match con el pattern
#  -n matched line numbers
#  -c cuenta en cuantas lineas hubo almenos un match
#  -A Display N lines After match
#  -B  before
#  -C  arround
#  -r recursive in directory
#  -l solo los nombres de archivos donde hubo match
#  -h solo las lineas de los archivos
printf 
# es similar a echo, te permiten imprimir solo qur echo al final siempre te pone \n
# otra ventaja es poder darle formato al output
# 
  tput cols # te permite saber el numero de columnas en display
  printf "%113s" " "| tr " " "-"
  printf "%$(tput cols)s" "-" | tr " " "-"3
  
  awk '{print $2" "$3" likes to "$5}' employees.txt
  
#awk [option] '[selection]{action}'
#	el separador default es espacio o tab
	
#	$0 signfica archivo completo, es igua pornerlo o no imprimirá todo el archivo
	awk '{print }' demo.txt 
	#o  ambas lineas significan lo mismo
	awk '{print $0}'
	#BEGIN {OFS="_"} el searador de columnas defaul es espacio así se cambia el separador por _
	awk 'BEGIN {OFS="_"} {print $1,$2}' demo.txt
	
#   NR imprime el numero de línea
	awk '{print NR, $0}' demo.txt
#   NF imprime el numero de fields en la linea
	awk '{print NR, $0, NF}' demo.txt
	#imprime el ultimo campo de la linea
	awk '{print NR, $0, NF , $NF}' demo.txt

sed 
# sed [options] commands [file]
# stream editor
# trabaja sobre stream of data
# searching, viewing, find and replace, inserstion or deletion
# regular expressions
	#ver un archivo o por linea
	sed '' demo.txt
	# p = print
	sed 'p' demo.txt
	# imprime linea 3
	sed '3p' demo.txt
	#imprime de linea 2 al final de file
	sed '2,$p' demo.txt
	# imprime 3 lineas a partir de la 6
	sed '6,+3p' demo.txt
	# imprime cada 3 lineas: 1,4,7,10,13
	sed '6~3p' demo.txt
	# se puede hacer todo lo anterior con delete cambiando p por d
	# borra 3 lineas a partir de la 6
	sed '6,+3d' demo.txt
	# borra desde la linea 2, afectando al archivo
	sed -i '2,$3d' demo.txt
	
mount | grep '^/dev'	
#####################################################################################

comandos referentes a filesystems

#####################################################################################
lsblk
fdisk
partprobe
gdisk
mkfs
mount
findmnt <- saber donde estan montados y que esta montado
umount <- desmontar
lsof <- list open files que no permiten desmontar
 
#AWS Disk formatting 
 sudo fdisk /dev/xvdb
 m
 n
 p
 1
 default number
 defaut
 (echo p; echo 1; echo; echo; echo w) | sudo fdisk /dev/xvdb
 #sid¿ de vuelve data es que hay que configurar, no hay file system
 sudo mkfs -t ext4 device_name
#mount point
 sudo mkdir mount_poit
#montar la unidad en el directorio
 sudo sudo mount -t ext4 -o defaults device_name mount_point
# editar para montado automático
 sudo cp /etc/fstab /etc/fstab.orig
 #agregar linea con nano
 device_name mount_point file_system_type fs_mntops
 /dev/xdvb   /data        ext4            defaults, nofail 0 2
#desmontar la unidad
 sudo umount data 

#obtener la zona de disponibilidad de una instancia EC2 consultando los metadatos de la ip
 EC2_AVAIL_ZONE=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
