#### Interacting with the command line shell
# convert, convertir todos los png en jpeg
# con os.list dir  iterar sobre los archivos del directorio
# y llamar convert con subprocess
import subprocess
subprocess.run(["date"])
# principales comandos
# unix
echo
cat
ls
chmod
# Linux
mkdir
cd
pwd # para saber el directorio actual
cp ../spider.txt. #../ <- significa el directorio padre,   el punto del final regresa al dir actual
# el comando significa que va a copiar el spider.txt que se encuentra en el padre al dir actual
touch myfile.txt # crea el archivo
ls #ls -l da mas info sobre los archivos 
mv 
mv myfile.txt myfile_renamed.txt
cp spider.txt spider_copy.txt
rm
rm * #borra todo el current
rmdir mydir # solo funciona con directorios vacios
# Streams, redirecting
# in/out streams por defecto teclado y pantalla
# redirection te permite mandar el stream a otro lado, un file por ejemplo
# > se usa para redirigir
echo > sample.txt hola
# esto es util para guardar en archivo el resultado de un script por ejemplo
./miscript.py > resultado.txt
# >> append el contenido
echo >> sample.txt concatenando contenido
# redireccionando standar input
#< redirecciona el input para tomarlo de un file por ejemplo o de un comando previo
./miscript <sample.txt
# 2> me permite redirigir los errores que se produzcan de un script a otro lado
./procesamdo_errores.py < log.file 2> errors_file.txt 
# el file descriptor es una variable apuntando a la i/o standar, o std
# 0/1 son para std in / out
# Piping
# toma el output de un programa y lo pasa como input a otro programa
# nos permite pasar el contenido de un comando a otro sin necesidad de guardar el 
# contenido en un archivo intermedio
ls -l | less # el putput de ls se vuelve el input de less 
# enumera las ocurrencias de un texto, ordenalas alfabeticamente y da las 10 mas repetidas
cat spider.txt| tr " " "\n"| sort | uniq -c |sort -nr| head
# tr " " "\n" cambia los espacios por  salto de linea
# sort ordena
# uniq -c elimina las repetidas y cuenta las ocurrencias
# sort nr ordena por numerico en reverse order
# head da el top 10
# python puedes leer inputs de u file usando stdin del modulo sys
# 
# Capialize la primer letra
# capitalize.py

#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print (line.strip().capitalize())
#  
cat harry.txt | ./capitalize.py
# capitile usa como entrada stdin y cat manda a stdout, pipe lo que hace es todar o redirigir
# el flujo de stin a stdou 
# otra manera de escribirlo
./capitalize.py < harry.txt
# cuandos on varios comandos se hace con pipe
# se puede usar tambien grep
# python como herramienta para extender la funcionalidad de bash
# Signalling processes
# comunicacion interprocesos
# la comunicacion puede ser por pipes o por signals
# signals son tokens que indican una accion deseada entre procesos, como reload de la configuracion
# terminar procesos, levantar procesos
ping www.google.com
# envía paquetes icmp
# ctrl+c lo interrumpe enviando una signal de stop llamada SIGINT que lo detiene apropiadamente
# ctrl+z interrumpe tambien la ejecución, pero esta vez de manera abrupta, 
#        SIGSTOP, el resultado es stopped, se detiene sin terminar
# fg, continua con la ejecucion que fue detenida
# kill manda SIGTERM para terminar el programa, es server command y dbee ejecutarse en server terminal
#        se le manda el PID 
# ps muestra los procesos que se están ejecutando o 
#        ps ax, muestra all the xcecuting processes, con grep podemos decirle que solo muestre 
#              los procesos que se llamen x (regex)
ping www.google.com
# en otra terminal
ps ax | grep ping 
# resultado:
   1923 ?        Ssl    1:09 /usr/libexec/gsd-housekeeping
 322479 pts/1    S+     0:00 ping www.google.com
 322484 pts/3    S+     0:00 grep --color=auto ping
# el pid es 322479
# ahora lo matamos
kill 322479
# cheat sheet
#Managing files and directories

#    cd directory: changes the current working directory to the specified one
#    pwd: prints the current working directory
#    ls: lists the contents of the current directory

#    ls directory: lists the contents of the received directory
#    ls -l: lists the additional information for the contents of the directory
#    ls -a: lists all files, including those hidden
#    ls -la: applies both the -l and the -a flags 

#    mkdir directory: creates the directory with the received name
#    rmdir directory: deletes the directory with the received name (if empty)
#    cp old_name new_name: copies old_name into new_name
#    mv old_name new_name: moves old_name into new_name
#    touch file_name: creates an empty file or updates the modified time if it exists
#    chmod modifiers files: changes the permissions for the files according to the 
#                       provided modifiers; we've seen +x to make the file executable
#    chown user files: changes the owner of the files to the given user
#    chgrp group files: changes the group of the files to the given group

#Operating with the content of files

#    cat file: shows the content of the file through standard output
#    wc file: counts the amount of characters, words, and lines in the given file; 
#               can also count the same values of whatever it receives via stdin
#    file file: prints the type of the given file, as recognized by the operating system
#    head file: shows the first 10 lines of the given file
#    tail file: shows the last 10 lines of the given file
#    less file: scrolls through the contents of the given file (press "q" to quit)
#    sort file: sorts the lines of the file alphabetically
#    cut -dseparator -ffields file: for each line in the given file, splits the line according 
#           to the given separator and prints the given fields (starting from 1)

#Additional commands

#    echo "message": prints the message to standard output
#    date: prints the current date
#    who: prints the list of users currently logged into the computer
#    man command: shows the manual page of the given command; manual pages contain a lot of information explaining how to use each command (press "q" to quit)
#    uptime: shows how long the computer has been running

#    free: shows the amount of unused memory on the current system 

# Redirections, Pipes and Signals
#Managing streams

#These are the redirectors that we can use to take control of the streams of our programs

#    command > file: redirects standard output, overwrites file
#    command >> file: redirects standard output, appends to file
#    command < file: redirects standard input from file
#    command 2> file: redirects standard error to file
#    command1 | command2: connects the output of command1 to the input of command2

#Operating with processes

#These are some commands that are useful to know in Linux when interacting with processes. 
# Not all of them are explained in videos, so feel free to investigate them on your own.

#    ps: lists the processes executing in the current terminal for the current user

#    ps ax: lists all processes currently executing for all users
#    ps e: shows the environment for the processes listed 

#    kill PID: sends the SIGTERM signal to the process identified by PID
#    fg: causes a job that was stopped or in the background to return to the foreground
#    bg: causes a job that was stopped to go to the background
#    jobs: lists the jobs currently running or stopped

#    top: shows the processes currently using the most CPU time (press "q" to quit) 
# 
# Bash script
# ps
# free
# uptime
# echo
# who
# date
# echo "string ${date}"# ${} placeholder del output de date
# 
# Variables y Globs
# Environment vriables
# variables
# set value =
# access value $
# no se declaran, se asignan
# variable="mensaje"# no debe haber espacios intermedios
# echo $varible
# export # accede a variables de environment
# puedes escribir más de un comando en una sola linea separandolos por ;
mensaje="mensajito"; echo $mensaje; mensaje="otro"; echo $mensaje
# globs son caracteres que permiten escribir lista de archivos
# *, ?  ; permiten crear secuencias de filenames para usarlas como parametros de los comandos en los 
#           scripts
# * significa todo lo que coincida con la busqueda , 
echo *.py # muestra todos los filename que terminen con .py
# ? significa exactamente 1 caracter
# buscar los filenames con 5 caracteres
echo ?????.py
# python tiene un módulo blog que te permite usar los comodines de bash
# las variables que defines son locales al environment en el que las defines
# export para compartir variables entre ambientes
# loops se basan en exit status of commands
# para saber el exitstatus of commands usa $?, 0 significa success
# se usa en if, si preguntas por el status de un comando y es 0 significa true
# por ejemplo saber si /etc/hosts contiene una entrada para 127.0.0.1 
if grep "127.0.0.1" /etc/hosts; then 
    echo "existe"
else
    echo"no esta"
fi
# la identacion no es obligatoria en bash, aunque hace código de calidad
# test ayuda a evaluar condiciones, exits 0 cuando true y 1 cuando false
if test -n "$PATH"; then echo "Path no empty"; fi
# -n significa no empty
if [ -n "$PATH" ]; then echo "Path no empty"; fi
# los [] cumplen la funcion de test pero recordar que debe haber espacio antes del ]
# while
n=1
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1))
done
# caso de uso, comandos reintentando conectarse, o lanzando peticiones
n=0 
command=$1# este es como sys.argv[1], para acceder al primer commandline
# se mantiene reintentando hasta que command sea 0, que significa status de exito
while $command &&[ $n -le 5 ]; do
    sleep $n
    ((n=n+1)) #va incrementando para esperar mas tiempo entre intentos
    echo "Retry #$n"
done;

# un script simulndo caso de exito o falla de conexxion
#!/usr/bin/env python3
import sys
import random
value= random.randint(0,3)
print ("returning "+str(value))
sys.exit(value)
# ./random_exit.py
#  ./retry.sh ./random_exit.py
# se le pasa el  el commando o script como parametro  y se ejecuta con las consultas
# FOR
#!/bin/bash
for fruit in peach orange apple; do
    echo "I like $fruit!"
done
# caso de uso oterar sobre los filenames de una carpeta para encontrar un archivo
# se complementa con * o ? para saber la lista sobre la cual iterar
# caso de uso, migración de un sitio web a otro servidor y renombrar los archivos HTML por html
cd old_website/
ls -l
# separa el nombre de la extension
basename retry.sh .sh 
# rename.sh
#!/bin/bash
for file in *.HTML; do
#"$file" las comillas permiten incluir aquellos archivos que contengan espacios en el nombre
    name=$(basename="$file" .HTM)
    mv "$file" "$name.html"
done
# recomendacion anes de correr un script que altere correrlo sin alterar para validar
# para ello correrlo con echo antes de mv, de ésta manera muestra como planea renombrar 
#!/bin/bash
for file in *.HTML; do
#"$file" las comillas permiten incluir aquellos archivos que contengan espacios en el nombre
    name=$(basename="$file" .HTM)
    echo mv "$file" "$name.html"
done

# advanced command integration
# system log file  /var/log/syslog
tail /var/log/syslog#para vr las últimas 10 lineas
'''
Aug 30 23:19:31 an-b3z systemd[1]: NetworkManager-dispatcher.service: Succeeded.
Aug 30 23:20:04 an-b3z gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Aug 30 23:20:04 an-b3z gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Aug 30 23:20:04 an-b3z gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Aug 30 23:20:04 an-b3z gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Aug 30 23:20:04 an-b3z gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Aug 30 23:20:04 an-b3z gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Aug 30 23:20:04 an-b3z gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Aug 30 23:20:04 an-b3z gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Aug 30 23:20:04 an-b3z gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).'''
# cut para hacer split de las líneas
# date computer shellpid error
tail /var/log/syslog | cut -d' ' -f5-
'''
snapd[878]: storehelpers.go:438: cannot refresh: snap has no updates available: "core", "core18", "gnome-3-28-1804", "gnome-3-34-1804", "gtk-common-themes", "snap-store", "snapd"
gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
'''
# split de la línea para mostrar a partir del campo 5
# ordenarlas por la mas repetida y contar cuantas veces se repite
cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head
'''
     10 systemd-resolved[803]: Server returned error NXDOMAIN, mitigating potential DNS violation DVE-2018-0001, retrying transaction with reduced feature level UDP.
      9 snapd[878]: storehelpers.go:438: cannot refresh: snap has no updates available: "core", "core18", "gnome-3-28-1804", "gnome-3-34-1804", "gtk-common-themes", "snap-store", "snapd"
      4 systemd-resolved[803]: message repeated 2 times: [ Server returned error NXDOMAIN, mitigating potential DNS violation DVE-2018-0001, retrying transaction with reduced feature level UDP.]
      3 gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
      3 gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
      3 gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
      3 gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
      3 gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
      3 gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
      3 gnome-shell[1842]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
'''
# procesar las lineas del log que terminan en log
#topologlines.sh
#!/bin/bash

for logfile in var/log/*log; do
    echo "processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
# bash para archivos y sistems commands
# python para tareas más complejas o que se vuelva dificil entender el código, usar un lenguaje de 
# general purpose
# bash no es tan flexible o robusto como python, con strings list and dictionaries, 
# la disponibilidad depende tambien del so donde se ejecute
# algunos comandos bashs son propios de la plataforma linux o windows, entonces algunos scripts
# deben traducirse a powershell
# 
# ############## Editign -files using substrings
#Introduction

#In this lab, you'll change the username of your coworker Jane Doe from "jane" to "jdoe" in 
#compliance with company's naming policy. The username change has already been done. 
# However, some files that were named with Jane's previous username "jane" haven't been updated yet. 
# To help with this, you'll write a bash script and a Python script that will take care of the 
# necessary rename operations.
#What you'll do

#    Practice using the cat, grep, and cut commands for file operations
#    Use > and >> commands to redirect I/O stream
#    Replace a substring using Python
#    Run bash commands in Python
#Prerequisites

#For this lab, you should have a sound knowledge of these Linux commands:

#    cat
#    grep
#    cut

#cat:

#The cat command allows us to create single or multiple files, view the contents of a file, 
# concatenate files, and redirect output in terminal or other files.

#Syntax:

#cat [file]

#grep:

#The grep command, which stands for "global regular expression print", processes 
# text line-by-line and prints any lines that match a specified pattern.

#Syntax:

#grep [pattern] [file-directory]

#Here, [file-directory] is the path to the directory/folder where you want to perform a 
# search operation. The grep command is also used to search text and match a string or 
# pattern within a file.

#Syntax:

#grep [pattern] [file-location]

#cut:

#The cut command extracts a given number of characters or columns from a file. 
# A delimiter is a character or set of characters that separate text strings.

#Syntax:

#cut [options] [file]

#For delimiter separated fields, the - d option is used. The -f option specifies 
# the field, a set of fields, or a range of fields to be extracted.

#Syntax:

#cut -d [delimiter] -f [field number]

#Linux I/O Redirection

#Redirection is defined as switching standard streams of data from either a user-specified 
# source or user-specified destination. Here are the following streams used in I/O redirection:

#    Redirection into a file using >

#    Append using >>

#Redirection into a file

#Each stream uses redirection commands. A single greater than sign (>) or a double 
# greater than sign (>>) can be used to redirect standard output. If the target file doesn't 
# exist, a new file with the same name will be created.

#Commands with a single greater than sign (>) overwrite existing file content.

#cat > [file]

#Commands with a double greater than sign (>>) do not overwrite the existing file content, 
# but it will append to it.

#cat >> [file]

#So, rather than creating a file, the >> command is used to append a word or string to the 
# existing file.
#Exercise
#The Scenario

#Your coworker Jane Doe currently has the username "jane" but she needs to it to "jdoe" to 7
# comply with your company's naming policy. This username change has already been done. 
# However, some files that were named with Jane's previous username "jane" haven't been updated. 
# For example, "jane_profile_07272018.doc" needs to be updated to "jdoe_profile_07272018.doc".

#Navigate to data directory by using the following command:

#cd data

#You can list the contents of the directory using the ls command. This directory contains a 
# file named list.txt. You will also find some other files within this directory.

#To view the contents of the file, use the following command:

#cat list.txt

grep " jane " ../data/list.txt | cut -d ' ' -f 1
grep " jane " ../data/list.txt | cut -d ' ' -f 2
grep " jane " ../data/list.txt | cut -d ' ' -f 3
# 1. el cambio de nombre de jane no se hizo del todo, revisamos que hubieran archivos
# 2. ahora hay que revisar que el archivo de su perfil exista 
# test EXPRESSION -e 
# la -e nos dice si el archivo existe, toma el nombre de archivo como parámetro  
# y regresa true si el archivo existe
if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi
# 3. Crear un archivo de prueba test.txt
> test.txt
#   para guardar un mensaje de prueba
echo "Añadiendo mensaje al archivo" >> test.txt


#find_jane.sh
# el script va a extraer las lineas de jane y ponerlas en oldFiles.txt
#!/bin/bash
#crear el archivo de jane
#test que el archivo no tenga nada escrito
if test -e /media/an-b3z/Windows/files/oldFiles.txt;
then
    echo "el archivo oldFiles.txt ya existe"
else 
    > oldFiles.txt
fi
#~/data/; jane
#buscar las lineas del archivo list.txt con los filenames jane, y guardarlo en una variable files
grep " careers " /media/an-b3z/Windows/files/harry.txt | cut -d ' ' -f 3 | while read -r filename ; do
    echo "Matched name:  $filename"
    #si el archivo existe
    if test -e /media/an-b3z/Windows/files/$filename.doc;
    then 
        #files=$files" "$filename
        echo "File exists"; 
        echo $filename>> oldFiles.txt
    else echo "File doesn't exist"; 
    fi
done
##############################
# verificar que los filenames encontrados existan en el file system (estén almacenados)
for filename in ~/data/oldFiles.txt; do
#aquí hacer el cut para que de la linea me de solo el filename
    files=$files" "$filename
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
    grep " jane " ../data/list.txt | cut -d ' ' -f 3
done



#leyendo las lineas y filtrando las que cnicidan, para despues iterar sobre ellas
grep "careers" /media/an-b3z/Windows/files/harry.txt| while read -r line ; do
    echo "Matched Line:  $line"
    # your code goes here
done

#iterando solo sobre la informacion relevante, filtrada y coratada la linea solo el campo 
grep " careers " /media/an-b3z/Windows/files/harry.txt | cut -d ' ' -f 3 | while read -r filename ; do
    echo "Matched name:  $filename"
    #si el archivo existe
    if test -e /media/an-b3z/Windows/files/$filename.doc;
    then 
        #files=$files" "$filename
        echo "File exists"; 
        echo $filename>> oldFiles.txt
    else echo "File doesn't exist"; 
    fi
done

if test -e ~/data/jane_profile_07272018.doc; 
then echo "File exists"; 
else echo "File doesn't exist"; 
fi


#########################################333
# parte 2, renombrando archivos en python
#changeJane.py  /scripts
#!/usr/bin/env python3
import sys
import subprocess
def change_name():
    old_name_file=sys.argv[1]
    #validar que el archivo no esté vacío
    old_name="jane"
    new_name="jdoe"
    new_line=""
    with open(old_name_file) as file_names:
        for line in file_names.readlines():
            new_line=line.strip().replace(old_name,new_name)
            #en log
            print("line: {} replaced with:{}".format(line,new_line)) 
            #en archivo
            result=subprocess.run(["mv","{} {}".format(line,new_line)], capture_output=True)
            print(result.returncode)
            print(result.stdout)
            print(result.stderr)
    old_name_file.close()

variable= input("tipo de volumen a:io1")
