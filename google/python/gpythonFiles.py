# files
# absolute path es el path completo donde se encuentra ubicado u recurso en el filesystem
# /home/ana
# relative paths es una especie de shortcut del path, se calcula a partir de 
# el path base (current directory) sumado del path relativo
# file descriptor, python le pasa la información sobre los permisos sobre el archivo abierto
# file descriptor es un token generado por el OS que permite a los programas hacer más 
# operaciones con el archivo, éste token es un atributo del file object
file = open ("file.txt")
file.readline()
file.close()
#open, use, close
# hay un numero limite de files descriptors que el SO uede crear por archivo, 
# es decir, un tope de por eso cerrar los archivos es importante
# el recurso puede ser bloqueado, o tratar de ser modificado por varios procesos a la vez
# consuo de recursos
# para la gestion de el proceso abrir, usar, cerrar, es mejor usar with, y que python lo haga por ti
with open("file.txt") as file:
    print (file.readline())
# la desventaja de with, es que solo puedes usar el archivo dentro del bloque,
# el archivo es tratado de manera similar al string o listas
file.readlines() 
# me devuelve una lista de lineas del archivo, esto implica que las lineas se mostraran en orden alfabetico
print("[",end="")
# con end le podemos decir el caracter de fin de linea, es decir que no sea \n si no , por ejemplo
# writting files
# por defecto los archivos se abren en modo r
# espeificar el mode: w  si el archivo no existe, python lo crea
# a append
# r+ read write
# si se abre un archivo en modo W y ya existe el archivo se sobrescribe
# write te dice al final cuantos caracteres escribió
import os
os.remove("file.txt")
os.rename("firstname", "lastname")
os.path.exists("file.txt")
os.path.getsize("file.txt")
# revisar cuando fue creado el archivo, te da el tiempo en sergundos, unix timestamp
os.path.getmtime("file.txt")
import datetime
date= datetime.datetime.fromtimestamp(os.path.getmtime("file.txt"))

d= datetime.date.fromtimestamp(os.path.getmtime("file.txt"))
os.path.isfile("file.txt")
#saber el absolute path
os.path.abspath("file.txt")
#revisar current location
os.getcwd()
os.mkdir("new_dir")
# cambiar de current directory
os.chdir("/another/path")
# remove directory/ el directorio debe estar vacio
os.rmdir()
# listar el contenido de un dir / me da solo los filenames
os.listdir("website")
# para saber si es directorio o archivo
os.path.isdir()
# para crear el absolute path, es mejor usar join en vez de la union manual para
# hacer el código portable, la funcion sabe que si es linux, usará / si es w usará\\
os.path.join("website")
#ejemplo

website_dir="website"
for name in os.listdir(website_dir):
    fullname=os.path.join(website_dir,name)
    if os.path.isdir(fullname):
        print("{} is directory".format(fullname))
    else:
        print("{} is file".format(fullname))

#CSV
import csv
f = open ("file.csv")
csv_f= csv.reader(f)

#parseando cada row en un elemento de lista
for row in csv_f:
    #umpacking the row
    name,phone,role=row
    #tambien puede hacerse parcial, name= row[0]
f.close()
#escribiendo CSV writerow / writerows 
import csv
hosts=[["workstation.local","172.0.0.2"],["workstation.cloud","172.0.0.2"]]
with open("host.csv","w") as hosts_csv:
    writer= csv.writer(hosts_csv)
    writer.writerows(hosts)

#csv con dictionaries
#dictinaries primer columna es el nombre de los files
# dictreader
import csv
hosts=dict()
with open("software.csv","w") as software:
    reader= csv.DictReader(software)
    
    for row in reader:
        print (("{} has {} users").format(row["name"], row["users"]))
#dict writer
# se pasa una lista de dictionaries  y una lista con ecabezados
users=[{"name":"ana", "username":"an","department":"infra"},
{"name":"ana", "username":"an","department":"infra"},
{"name":"ana", "username":"an","department":"infra"}]
keys =["name","username","department"]
with open ("file.csv") as by_dep:
    writer= csv.DictWriter(by_dep,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
    




# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""
    f=open(filename)
    # Read the rows of the file
    rows = csv.reader(f)
    # Process each row
    for row in rows:
        print(row)
        name,color,typ = row
        if not name=="name".strip():
      # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(name.strip(),color.strip(),typ.strip())
    return return_string

#Call the function
print(contents_of_file("filename.csv"))

#################final

#1/usr/bin/env python3
import csv
def read_employees(csv_file_location):
    csv.register_dialect('empDialect',skipinitialspace=True,strict=True)
    employee_file=csv.DictReader(open(csv_file_location),dialect='empDialect')
    employee_list=[]
    for data in employee_file:
        employee_list.append(data)
    return employee_list

def process_data(employee_list):
    department_list=[]
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data={}
    for department_name in set (department_list):
        department_data[department_name]=department_list.count(department_name)
    return department_data

def write_report(dictionary,report_file):
    with open(report_file,"w") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+"\n")
    f.close()

write_report(process_data(read_employees("employees.csv")),"report.txt")