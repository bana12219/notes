https://www.pathname.com/fhs/pub/fhs-2.3.html
/etc<-- los de las aplicaciones del sistema, configuracion que define el comportamiento del sistema 
      // del sistema
	host system config. A "configuration file" is a local file used to control the operation of a 
	program; it must be static and cannot be an executable binary.
	----------------------------------------------------------------------------------------------
	Requirements

		No binaries may be located under /etc. [5]
		The following directories, or symbolic links to directories are required in /etc:

	Directory	Description
	opt	Configuration for /opt
	X11	Configuration for the X Window system (optional)
	sgml	Configuration for SGML (optional)
	xml	Configuration for XML (optional)
	
	########################SGML################################################################
	##https://www.debian.org/doc/manuals/sgml-howto/x59.html                                  ##
	##(SGML es como latex?, html)                                                             ##
	##Standard Generalized Markup Language, para documentar                                   ##
	##Documentacion estructurada en chapters, sections, paragraphs... elementos labeled según ##
	##su tipo: references, program output... No especifica como presentar la info, solo       ##
	##estructura y contenido                                                                  ##
	########################SGML################################################################
	----------------------------------------------------------------------------------------------
	Specific Options
	
/opt<-- optional, los de las aplicaiones que insrtala el usuario// del usuario
/usr<-- del usuario
montaje mount
       mount [-l|-h|-V]

       mount -a [-fFnrsvw] [-t fstype] [-O optlist]

       mount [-fnrsvw] [-o options] device|dir

       mount [-fnrsvw] [-t fstype] [-o options] device dir






###############################################################################################
file systems. Operaciones sobre discos y distribucion del sistema de archivos
###############################################################################################
devices. nivel de hardware es como el dispositivo se le presenta a linux, puede venir de diferentes environments
	disk. físico o virtual
	Storage. es externo y puede venir de una SAN con protocolos ISCSI o fibra
	
	esto se representa como /dev/sda
			/dev -> devices: los files del device que implementan la interface con el hardware del device
			  /sd... -> iscsi  y la letra que corresponde con el numero del device en cuestion
			  	dentro se tiene la distribucion para ubicar áreas esecíficas, porque no es comun que se use el disco entero
			  	partition
			  	LVM logical volume manager, particion dentro de particion
			  	MBR , GPt, esquema de particionamiento
			  	 ubuntu usa GPT
			  	 redhat usa MBR
 		######particionamiento	 #########
lsblk<- ver los discos disponibles
fdisk /dev/sdb <- para comenzar a particionar
	m del menu
	p para ver lo que tiene actualmente el disco
	n new partition
	  p: primary partitions
	  e: extended 
	  ...
	  w: write
lsblk -l read master boot record  	 
 		######filesystem #########
 mkfs <- permite hacer uso de
 		El file sysem por defecto xfs, redhat
 		ext4, systema por defecto en ubuntu
 		vfat, compatible con todos los sistemas operativos
 		btrfs, version reciente puede encontrarse en algunos oracle
 		ntfs, es una opcion en ubuntu pero tiene detalles ya que deriva de una reverse engineering
 mkfs.xfs /dev/sdb1 <- redhat
 mkfs.ext4 /dev/sdb1 <- ubuntu
  		######mount #########
mount /dev/sdb1 /myapp
lsoft /myapp

