# reading data interactively
# input, para que el user de valores
name = input("type your name: ")
int(input("type a number: "))
#convierte el input en entero
#i/o streams:
# standar input stream  --  stdin     metodo estandar de entrada, como teclado
# standar output stream --  stdout    metodo estandar de salida como imprimir en pantalla
# standar error         --  stderr    canal para mensajes de error o de diagnostico
data = input("this come from STDIN: ")
print ("this goes to STDOUT: "+data)
print ("generating an error STDERR: "+data+1)#causa error porque tratas de sumar 1 a un string
# Environment variables
import os
#leyendo variables de entorno
print ("HOME: "+os.environ.get("HOME",""))
print ("SHELL: "+os.environ.get("SHELL",""))
print ("PATH: "+os.environ.get("PATH",""))
# ENviron es un dictionary del modulo os que python provee para usar las variables de entorno
os.environ["HOME"]
# se puede usar como diccionario, la cuestión es que si lo usas como diccionario y la variable no 
# existe vas a tener un error, si usas el metodo tienes la validacion y tratamiento en caso de error
# el metodo te regresa una cadena vacia si no existe la variable
# export VARIABLE=valor <---- para setear variables desde la terminal
# pasar argumentos desde linea de comandos
import sys
print(sys.argv)# imprime los parametros pasados desde la linea de comandos 
# es como String args del main
# Exist status o return code. 
#este es bash
$? # para consultar el return code
# exit status nos permite saber si la ejecuccion fue exitosa o no 
# nos permite tambien al automatizar poder reintentar si la ejecicion fallo, o incluso
# contar cuantos reintentos van
#este es bash
wc # cuenta el numerode lineas, palabras y caracters en un archivo
wc /media/an-b3z/Windows/files/harry.txt
#output
  276  3587 33826 /media/an-b3z/Windows/files/harry.txt
echo $?
#output 
0
# Systems commands 
# Subprocesos
# correr bash en python 
import subprocess
subprocess.run(["date"])
#output
mar 25 ago 2020 20:31:13 CDT
CompletedProcess(args=['date'], returncode=0)
# se creal subproceso bloqueandose el proceso primaruio hasta que el subproceso termine
subprocess.run(["sleep",2])
# mientras corre el subprocess python se bloquea
result = subprocess.run(["ls", "this_file_doesnt_exist"])
ls: cannot access 'this_file_doesnt_exist': No such file or directory
>>> print (result.returncode)
2
#obtener el output de system command
# para tener acceso al output desde python se le debe indicar a subprocess.run
capture_output=True
result= subprocess.run(["host","8.8.8.8"],capture_output=True)
result= subprocess.run(["host","8.8.8.8"],capture_output=True)
>>> print (result.returncode)
0
>>> print(result.stdout)
b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
# la b significa que el string no viene de python
# array of bytes, la computadora transmite en bytes, y para traducir a diferentes 
# lenguajes por ejemplo se hace un encoding, cada lenguaje tiene diferentes posibles caracteres
# el chino por ejemplo tiene 10000 caracteres, mientras la compu usa hasta 256 por eso se usan 
# las especificaciones o encoding para saber que secuencias de bytes representan que caracteres
# el estándar más usado es UTF encoding para recuperar la informacion se hace el decode
# por defecto se usa UTF8 ya que es el estándar
>>> print (result.stdout.decode().split())
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']
# para obener los posibles errores que se generan de la ejecucion
# stderr
result= subprocess.run(["rm","arch_no_existe"], capture_output=True)
>>> print(result.returncode)
1
>>> print(result.stdout)
b''
>>> print(result.stderr)
b"rm: cannot remove 'arch_no_existe': No such file or directory\n"
# variables de entorno
import os
import subprocess
my_env= os.environ.copy()
my_env["PATH"]= os.pathsep.join(["/opt/myapp/", my_env["PATH"]])
result= subprocess.run(["myapp"],env=my_env)
# usos: cambiar de directorio con cwd al momento de ejecutar el script, 
# matar un proceso despues de trascurrido un tiempo
# logg searching
import re
import sys
logfile= sys.argv[1]
with open(logfile) as f:
    for line in f: 
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result= re.search(pattern,line)
        print(result[1])
# We're using the same syslog, and we want to display the date, time, and process id that's 
# inside the square brackets. We can read each line of the syslog and pass the contents to the 
# show_time_of_pid function. Fill in the gaps to extract the date, time, and process id from 
# the passed line, and return this format: Jul 6 14:01:23 pid:29440.
import re
def show_time_of_pid(line):
  pattern = r"^([A-Za-z]{3}[0-9 :]{11}) .*\[([0-9]{,5})\]:.*"
  format=r"\1 pid: \2"
  result = re.sub(pattern,format,line)
  return result

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
# Making sense out of data
# buscar los movimientos de un usuario
import re 
import sys
logfile= sys.argv[1]
usernames={}
with open (logfile)as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern=r"USER \((\w+)\)$"
        result= re.search(pattern,line)
        if result is None:
            continue
        usernames[name]= usernames.get(name,0)+1
print (usernames)
# 
# Sample Introduction
#
#Imagine one of your colleagues is struggling with a program that keeps throwing an error. 
# Unfortunately, the program's source code is too complicated to easily find the error there. 
# The good news is that the program outputs a log file you can read! 
# Let's write a script to search the log file for the exact error, then output that error 
# into a separate file so you can work out what's wrong.
#What you'll do
#    Write a script to search the log file using regex to find for the exact error.
#    Report the error into a separate file so you know what's wrong for further analysis. 
# In the /data directory, there's a file named fishy.log, which contains the system log. 
# Log entries are written in this format:
# Month Day hour:minute:second mycomputername "process_name"["random 5 digit number"] 
# "ERROR/INFO/WARN" "Error description"
# Find an error
# In this lab, we'll search for the CRON error that failed to start. 
# To do this, we'll use a python script to search log files for a particular type of 
# ERROR log. In this case, we'll search for a CRON error within the fishy.log 
# file that failed to start by narrowing our search to "CRON ERROR Failed to start".

# For defining the output file, we'll use the method os.path.expanduser ('~'), which returns the home directory of your system instance. 
#find_error.py
#!/usr/bin/env python3
import sys
import os
import re
def error_search(log_file):
    error= input("What is the error? ")
    returned_errors=[]
    error_patterns=[]
    error_patterns.append(r"error")
    for i in error.split(" "):
        error_patterns.append(r"{}".format(i.lower()))
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in file.readlines():
            if all(re.search(error_pattern,log.lower())for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors
def file_output(returned_errors):
    with open (os.path.expanduser('~')+"/data/errors_found.log","w") as file:
        for error in returned_errors:
            file.write(error)
        file.close()
if __name__=="__main__":
    log_file= sys.argv[1]
    returned_errors=error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)


error="CRON ERROR Failed to start"
print(error.split())

for i in error.split(" "): #range(len(error.split(' '))):
    print(i)

error_patterns=[]
for i in range(len(error.split(' '))):
    print(i)
    error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
    print(error.split(' ')[i])

print(error_patterns)


for i in error.split(" "): 
    error_patterns.append(r"{}".format(i.lower()))