##Usuarios 
Ver el systema dividido en 2
	users- usuarios y procesos
	kernel - acceso a hardware mediante sus drivers
   los usuarios y procesos requieren acceder a el hw, para ello esto proveen interfaces por lo que se tiene system calls y permisos

pero root está dentro del scoope del kernel
   
su -switch user
sudo -super user do
 en ubuntu el acceso a root es mediante sudo
 centos te permite iniciar sesion con root
 ------------------centos---------------------
 sudo useradd lori<- el susuario debe estar en el archivo sudoers
 #agregado usuario a grupo 
 sudo usermod -aG wheel user <- se debe reiniciar el shell para que cargue de nuevo el env con los nuevos permisos, wheel es grupo de sudoers
 entonces user ya puede agregar usuarios 
 sudo useradd lori
 grep lori /etc/passwd
 sudo -i abre root shell
 su -   abre root shell pero solicita contraseña
 uname:x:1000:1000:Ana,,,:/home/uname:/bin/bash
usuario:contraseña_UID:GID:comentarios:homedir:shell
 --------sudoers config----------
 *****Ubuntu
 # User privilege specification
root    ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL

##formato user host = (usuarios) [NOPASSWORD:]comandos 

******CENTOS
  %wheel ALL=(ALL) ALL
  %Grupo allHosts=(Allcommands) asallUsers
  root    ALL=(ALL:ALL) ALL
  esta es la config para un solo usuario
  ana ALL=/bin/passwd      <-- modificando los privilegios para que ana pueda cambiar contraseña
  ##logeados como ana su - ana si ejecutamos el comando siguiente podemos cabiar al password de root
  sudo passwd root
  ## en /etc/sudoers.d puedes tener un file de config de usuario
  ##al poner nopassword implica que no requiere poner pasword para ejecucion, open configuration
  otro-usr ALL=(ALL) NOPASSWD:ALL
 
chvt<--- change virtual terminal, 6  terminales virtuales en  linux
	la vt 1 es grafical 
	tambien llamada tty, apartir de la 2 son text
	
	graphical desktop se tiene 3 sesiones
	pts /0 
	pts1 y 2 son las sesiones
ssh
sshkeygen
ssh-copy-id
scp copy files entre servidores bajo ssh stack


	
	














