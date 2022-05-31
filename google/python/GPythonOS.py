#GPythonOS
#OS
#kernel - core del so
#        gestiona Systems resources
#        Network
#        Disk
#        Memoria
#user space, el usuario no interactua con el kernel directamente, interactua con el user space
#            user interface
#            systems programs
#
#files y procesos 
#los scripts viven a nivel user space, y en ocaciones van al so por un poco más de info
#distributions
#unix se desarrollo en los 70 por bell labs
# 
#*NOTA: install and uninstall packages es importante para el rol, apt install
#
#pypi o python package index, es el repositorio donde los developers 
#suben packages que se consideran útiles
#pip es el gestor de paquetes de python
#   ejemplo pip install requests<-- modulo para servicios
#   resp= requests.get(http://)
# el manager installation de mac homebrew
#
# el modulo arrow nos permite tener más operaciones sobre fechas 
# package manager: apt, yum ...
# pil o python image library para manipulacion de imagenes
# python data analysis library
# ejemplo de data analisis
# pip3 install pandas
# WARNING: The scripts f2py, f2py3 and f2py3.8 are installed in '/home/an-b3z/.local/bin' which is not on PATH.
# Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

import pandas
visitors=[23234,12323,34234,3423,342]
errors=[23,34,45,56,67]
df= pandas.DataFrame({"visitors":visitors,"errors":errors},index=["lun","mar","mier","jue","vie"])
# lenguajes compilados faster than interpretados
# c, c++, go, rust
#el tiempo de desarrollo es más rápido para un leguaje interpretado
#   python, ruby, javascript, bash, powershell
# mix de ambos
# java, c#
#
# cat hello_world.py
# python3 hello_world.py <- ejecutar el script
# ~<- le die al so con que queremos que se ejecute
# paso 1. formato script; la primer linea le dice que se ejecute on python3
#!/usr/bin/env python3   
# paso 2. hacerlo ejecutable
 chmod +x hello_world.py
# paso 3. ejecutar l script
 ./hello_world.py
# ./ es dado que el script no se encuentra en algún path de la variable PATH
# PATH contiene la ruta de carpetas con archivos ejecutables
#
##########################Sample
# automatizas el envio diario de correo a manager con la lista de tickets o issues atendidos
# 2 tareas principales: 
#       1. obtener la lista de usuarios a notificar
#       2. crear el email y enviarlo al manager
# del system log bucar los eventos si el evento se encuentra, te notificas
# tarea duplicada, a automatizar, envío de emails
# la construccion de un módulo es codificar en un archivo, funciones, clases y variables que estarán
# disponibles mediante import
# escalabilidad significa que cuando más trabajo se agrega al sistema, 
# el sistema puede haer lo que necesite para completar la carga de trabajo.
# ejemplo la llegada de un nuevo miembro al equipo de trabajo incluye crear cuenta de usuario, 
# mailbox y el home folder, así como el acceso a varios recursos de sistema
# éstas tareas se automatizan 
# el de TI lo que debe hacer es ingresar los nuevos datos al script para la asignación de recursos
# centralizacion de errores es decir si algo está mal en la configracion de una cuenta,
# basta con corregir el script para terminar con el error
# bit rot es el termino que se da a las fallas provenientes de un cambio de entorno, 
# el proceso de automaización falla dado que cambió algo en el ambiente como un label de disco
# loggeo taggeo para poder identificar donde está el error
# así como notificacion para corrección
# verificar tamie que quizá la aea no fallo en ejecución pero el resultado no es el correcto
# automatización de backups, , scheduled, comparación de datos contra el master
# automatización  del health checks para saber el estado del equipo
# modulo shuti para health checks
import shutil
du = shutil.disk_usage("/")
print (du)
#psutil me da la info de cpu_percentage
#!/usr/bin/env python3
import psutil 
import shutil
#check disk usage if more than 20% is free
def check_disk_usage(disk):
    du=shutil.disk_usage(disk)
    free=du.free/du.total*100
    return free>20
# check CPU usage
def check_cpu_usage():
    usage=psutil.cpu_percent(1)
    return usage <75

if not check_disk_usage("/") or not check_cpu_usage():
    print ("Error")
    #aquí se puede lanzar la alerta a los sysadmins
else:
    print ("Everything is good")











#https://learning.oreilly.com/library/view/computational-thinking-/9781780173641/
#https://kodekloud.com/p/learning-path
#mathematical thinking
#mathematics
#computational thinking
#https://learning.oreilly.com/videos/just-enough-math/9781491904077