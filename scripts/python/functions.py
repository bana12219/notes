#built in functions
# las de python
input()
max()
print()
#user define functions
def function_name(param_one, param_two,aram_tree):
    #code
    return param_one
#llamada
function_name(1,2,3)

#ejemplo priamide
def pyramid():
    symbol='#'
    for i in range (0,10):
        #center es para darle formato a la línea
        #el primer parámetro es la longitud de linea, el segundo es el simbolo de relleno
        print (symbol.center(12,"-"))
        symbol+="#"

pyramid()
#variables especiales que se ejecutan antes de empezar el interpreter
#_name_ nombre del archivo que se eecuta
#_main_
# if _name_== "_main_" <- nos permite saber si el archivo que se está ejecutando actualmente es el principal o desde otro
# para invocar desde otro archivo
#  import nombre_archivo
#  nombre_archivo.nombre_function(param)
repetir =3
print("mensaje"*repetir)
#funciones anónimas o lambda
#lambda arg_1, arg_2: ops
#declaracion
add= lambda x,y:x+y
print add(2,3)
#elevar a una potencia
#var**2
#pasar una constante a una lambda
definicion= lambda m, c=.54: m*c**2

print (definicion(5))

