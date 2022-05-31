# Procesos
# 1. Understand the problem statement, inputs y outṕuts
# 2. Research, heramientas disponibles para atacar el problema, incluso scripts previos
# 3. planning, pensar en los datatypes, algoritmos, sinergia, incluso ponerlo en papel
# 4. writing, escribir la solucion identificando los planes y problemas, testing
# 
# Servidor Ticky, donde todos se loggean, se genera un log
# explotacion de logs, para hacer reportes
# syslog  username ticket
# dos reportes, los errores del mas recurrentes, un ranking de errores recurrentes, 
# una lista de los errores generados y cuantas veces se repiten, usin tomar en cuenta los usuarios
#
# otra, un estadistico de los usuarios del sistema, 
# es decir todos los usuarios que han usado el sistema y cuantos infomessages y error messages genera 
# ordenados por username para visualizar en una webpage servida en 
# un web server, ya existe un csv llamado csv_to_html.py, este script hace la 
# presentacion de datos en una tabla html 
#########3
# para procesar loglines usar regexp
# testear (regex101.com) el pattern que se diseña y probarlo antes de integrarlo en python 
# python interpreter para saber que esta trayendo la informacion adecuada
# despues de la extraccion de informacion, debes contar cuantos errores hay del mismo tipo
# y que tantos info y error messages hay por usuario
# (un calculo por tipo de error, otro por usu que tantos info y error genera), dictionries
# un dictionary para error messages
# otro para contar por uso de usuario, 
# sortear el dictionry por criteria para acomodar los datos que serán presentados
# al script se le pasan dos parametros:
    #   el nombre del csv file
    #   el nombre del html a generar
# este ultimo paso se puede hacer de un python o de un bash
# como el script llama comandos y mueve archivos se recomienda hacer en bash
#####
#What you'll do

#    Use regex to parse a log file
#    Append and modify values in a dictionary
#    Write to a file in CSV format
#    Move files to the appropriate directory for use with the CSV->HTML converter

#### se tiene un syslog. log co el siguiente formato
'''
May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)
Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)
'''
# si el systema se ejecuta bien se crea un info con el numero de ticket, lo que hizo, 
# el user y un ticket
# si es error, , indica lo que estuvo mal, el susuario  que lanzó la accion que cusó error
# algunos errores :
    
    #   Timeout while retrieving information
    #   The ticket was modified while updating
    #   Connection to DB failed
    #   Tried to add information to a closed ticket
    #   Permission denied while closing ticket
    #   Ticket doesn't exist
# para filtrar solo las lineas de ticky 
grep ticky syslog.log
# mostrar los errores 
grep "ERROR" syslog.log
# listar un error específico
grep "ERROR Tried to add information to closed ticket" syslog.log



# 1 errores 
# 2 errores por tipo

import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
re.search(r"ticky: INFO: ([\w ]*) ", line)
<_sre.SRE_Match object; span=(29, 57), match='ticky: INFO: Created ticket '>
re.search(r"ticky: ERROR: ([\w ]*) ", line)

#para  la ordenacion 
fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
sorted(fruit.items())
[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]
import operator
sorted(fruit.items(), key=operator.itemgetter(0))
[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]
sorted(fruit.items(), key=operator.itemgetter(1))
[('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]
sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)
[('bananas', 7), ('apples', 5), ('oranges', 3), ('pears', 2)]

#files
nano user_emails.csv
Full Name, Email Address
Blossom Gill, blossom@abc.edu
Hayes Delgado, nonummy@utnisia.com
Petra Jones, ac@abc.edu
Oleg Noel, noel@liberomauris.ca
Ahmed Miller, ahmed.miller@nequenonquam.co.uk
Macaulay Douglas, mdouglas@abc.edu
Aurora Grant, enim.non@abc.edu
Madison Mcintosh, mcintosh@nisiaenean.net
Montana Powell, montanap@semmagna.org
Rogan Robinson, rr.robinson@abc.edu
Simon Rivera, sri@abc.edu
Benedict Pacheco, bpacheco@abc.edu
Maisie Hendrix, mai.hendrix@abc.edu
Xaviera Gould, xlg@utnisia.net
Oren Rollins, oren@semmagna.com
Flavia Santiago, flavia@utnisia.net
Jackson Owens, jackowens@abc.edu
Britanni Humphrey, britanni@ut.net
Kirk Nixon, kirknixon@abc.edu
Bree Campbell, breee@utnisia.net

sudo chmod +x csv_to_html.py
sudo chmod  o+w /var/www/html
# al script se le pasan el archivo de datos y el path/nombre de archivo de salida.html
./csv_to_html.py user_emails.csv /var/www/html/<html-filename>.html

#############################
## los reportes  
# The ranking of errors generated by the system: A list of all the error messages logged 
#                           and how many times each error was found, sorted by the most 
#                           common error to the least common error. This report doesn't 
#                           take into account the users involved.
# The user usage statistics for the service: A list of all users that have used the system, 
#                           including how many info messages and how many error messages 
#                           they've generated. This report is sorted by username
#
# nano ticky_check.py

#!/usr/bin/env python3
def validating_file():
    pass
def clasifiying_log_lines(filename):
     = dict()
    per_user=dict()
    with open(filename) as log_file:
        pattern=r'ticky: (INFO|ERROR): ([\w ]*) (\(\w+\))$'
        for line in filename.readlines():
            result = re.search(pattern, line)
            message_type=result[1]
            message_info=result[2]
            username =result[3]
            if message_type =="ERROR":
                errors_counter[message_info]=errors_counter.get(message_info,0)+1
            per_user_count= per_user.get(username,dict(INFO=0,ERROR=0))
            per_user_count[message_type]=per_user_count.get(message_type)+1
            per_user[username]=per_user_count
    

    filename.close()
        '''
May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)
Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)
'''
re.search(r"ticky: INFO: ([\w ]*) ", line)
<_sre.SRE_Match object; span=(29, 57), match='ticky: INFO: Created ticket '>
re.search(r"ticky: ERROR: ([\w ]*) ", line)
        

def writting_file():
    pass