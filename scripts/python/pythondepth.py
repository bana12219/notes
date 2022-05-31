"""multiline
strings
into
triple quotes"""
#los strings se concatenan con + pero solo entre strings con otros tipos no funciona

# la funcion id me da la referencia en memoria o el puntero a la variable
var= "string"
print (id(var))
print (id("stirng"))
print (id("string"))
# usa la optimizacion de meoria parecido a java, pues 
print (id(var))
print (id("string"))
# dan el mismo valor de referencia de memoria, al igual que java para optimizar el consumo de memoria
# las variables son referencias al objeto en memoria a menos que se hag new Variable
# python los strings son inmutables, lo que significa que tendrías que reasignar con un slicing
# slicing
variable= "someverylargewordhere"
# me da en reverse order
variable[::-1]
#una si y una no 
variable[::2]
id(obj)# me da la dir de memoria
dir (obj) # me da todos los builtin methods disponibles para mi object
alumnos=["ana","pala","paola"]
print(" ".join(alumnos))
import string
print(string.ascii_lowercase)
from string import ascii_lowercase
print(ascii_lowercase)
#extrapolation
stock_value="1000"
print (f"the price of goole stock is {stock_value}")
print ("the price of goole stock is {}".format(stock_value))
print ("the price of goole stock is {value}".format(value=stock_value))
print ("String {vari} para {otra} rellenar{mas} con formato".format(vari="2 ",otra="4 ", mas=" 6 "))
#ejemplos de formatos a dos digitos
print ("string ${:.2f}".format(34.567))
print ("string ${price:.2f}".format(price=34.567))
print ("string {price} ${price:.2f}".format(price=34.567))
h all the strings joined by the delimiter 

Expr	Meaning	Example
{:d}	integer value	                                '{:d}'.format(10.5) → '10'
{:.2f}	floating point with that many decimals	        '{:.2f}'.format(0.5) → '0.50'
{:.2s}	string with that many characters	            '{:.2s}'.format('Python') → 'Py'
{:<6s}	string aligned to the left that many spaces	    '{:<6s}'.format('Py') → 'Py    '
{:>6s}	string aligned to the right that many spaces	'{:>6s}'.format('Py') → '    Py'
{:^6s}	string centered in that many spaces	            '{:^6s}'.format('Py') → '  Py '
#una nueva manera de escribiro es
"base string with %d and %d placeholders" % (value1, value2)

# numeric types
# Integers , floats
# modules 
# math
# mod %
7 %2 # 1
6%2#0
7//2#3
6//2#3
import math
math.pow(10,5)# 10**5
math-log2(10000)
import random
random.randint(0,100000)
#conditionals
    true    false
and  true, true= true
and  true, false= false
or  true, true= true
or  false, true= false
or  false, false= false
#types
text:strings
numbers: int, float
functions: built-in, custom
custom objects: classes
# control flow
iterators, for/while loops, 
#compound datatypes
list 
dict
set
tuple
#data structures
list()
lista=["elemnt",2,False]
#######################
dict()
nickname=dict(bob="boby",Alice='ally')
diccionario2={'Bob':'Bobby','Alice':'Ally'}
######################
# los set son como las listas pero no permiten 
# valores duplicados
set()
sets={"elemnt",2,False}
# no esta ordenado, y recorrerlo 
#no se hace siempre en el mismo orden
######################
tuple()
tuplas=("elemnt",2,False)
# son idexadas y ordenadas e inmutables
#####Listas: operaciones
# sort- sort() sorted()
# find- len(), min(), max(),in, indeing, slicing, count()
# insert/remove- append(), insert(), extend(), remove(), pop()
# sublist- slicing, inplace, copying
#iteration- for/while
lista.sort()
anotherlist=sorted(lista)
#id(obj) me permite saber si se trata del mismo objeto
# veri si existe
print(2 in lista)
#consultar la posicion del elemento
print(lista.index(2))
#minmo y max para strings se usa alphabetical order
min(lista)
max(lista)
#contar ocurrencias
print(lista.count(2))
#append agrega al final
lista.append(345)
#insert agrega e ep indice indicado
index=3
elemento="13"
lista.insert(index,elemento)
#agregar los elementos de una lista a otra
nueva=[2,3,4,5,6,7]
lista.extend(nueva)
#eliminar
lista.pop()#elimina el ultimo
lista.remove()#elimina 
########listas[]
########tuplas()
# son inmutables
usan () en vz de []
##########sets {}
#colecciones desordenadas, sin duplicados
#convertir lista a set para remover duplicados
my_set= set(lista)
#loops
#iterando sobre elementos
for elem in lista:
    print (elem)
#iterando sobre idices
for inde in range(len(lista)):
    print(index)
for item in diccionario2.items():
    print(item)
    #unpacking
    key,value=item

#automatically unpacking
for key,value in diccionario2.items():
    print (key,value)

lista2= [randint(1,100)for num in range(100)] # agregando automaticamente 100 numeros aleatorios
lista2= [num**2 for num in range(100)] 
#convertir numero a ascii
from random import randint, choice
from string import ascii_lowercase
lista3=[coice(ascii_lowercase)for num in range(100)]
enumerate(lista)# me permite asociar el indice al elemento
for index,item in enumerate(lista):
    print (index,item)

#funciones
def function(input):
    '''use this function to do...
    input: list of integers
    output: sorted list '''

#funciones paso por valor y por referencia
#los inmutables como enteros se pasan el valor
# las listas por emjemplo que son mutables se pasa referencia 
def funct1(entero, lista):
    entero=entero +1
    lista [0]= lista[0]+1
    print (entero,"lista: ", lista)
    var1,var2=funct2(entero, lista)
    print (entero,"lista: ", lista)
    print(var1,var2)
    return var1,var2

def funct2(entero, lista):
    entero=entero +1
    lista [0]= lista[0]+1
    print (entero,"lista funct 2: ", lista)
    return entero, lista

entero=0
lista =[0]
print (entero,"lista: ", lista)
print (funct1(entero, lista))
# tomar esto en cuenta para el desarrollo con patterns

# metodos especiales de objetos
def __str__(self): # es el tostring para el usuario
def __repr__(self): # es la reperesentacion del objeto
def __len__(self): # aquí defines como se va a medir la longitud del objeto
#otros metodos  lt, gt, eq

#files
