pwd #imprime el directorio actual
ls #lista el contenido del directorio
cd #navegar entre directorios
mkdir newfolder #crear nuevo folder
mv testfile.txt /home/newfolder/ # mueve el archivo al nuev foder
mv /home/newfolder/testfile.txt . # regresa el archivo al directorio actual "." representa el directorio actual
cp originalfile.txt newfile.txt # hacer la copia del archivo
cat file.txt # mostrar el contenido de un archivo
rm testfile.txt #borrar archivo
rm -r newfolder # -r  de recursivo, borra el folder y su contenido


#shorcuts
.. #parent directory
#tab autocomplete filenames
vi newfile # cra un nuevo archivo y lo abre para edicion





###files 
ownership 
	ugo-> user, group, other
	chown, si no se cambia el owner será el creador y su grupo primario sera el group owner
	chgrp
permisions mode
	rwx
	chmod
	
	Sobre archivos
     chmod [usr catg] [oper] [permiso] file
     categoría de usuario ugoa
     u    user
     g    group
     o    other
     a    all
     operacion +-=
     +    add
     -    substract
     =     set
     permiso rwx
     r    read
     w    write
     x    execute
     permiso base numerica
     r    w    x
     0    0    0    value for off
     1    1    1    value for on
     4    2    1    decimal
     octal    Binario String    Descripcion
     0          0      ---    No
     1          1      --x    Exe
     2          10     -w-    Write
     3          11     -wx    Wrote and exe (2+1)
     4          100    r--    Read only
     5          101    r-x    read and exe(4+1)
     6          110    rw-    read and write(4+2)
     7          111    rwx    read, write and exe(4+2+1)
   agregar permisos de escritura al archivo para todos los usuarios del grupo
   chmod g+w file.txt
   trwxrwxrwx 
