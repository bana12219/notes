#naming conventions 
#snake case
my_variable=""
MY_CONSTANT=""
#bloques son los sentencias que se ejecutan consecutivas como for
# usas indentacion para separar los bloques
#if x>0
#    print "s"
#else
#    print "n"

# Variables  puede ser 
# strings
# flotantes
# boleanos
# data structures

# numeric values
# flotantes
# ** exponente
# // floor division : solo te da la parte entera  9//2= 4
#  strings

print (2**10)
# input
#a=input()
#importas tambien con import
import math
#binarios, octales y hexadecimales
0b111
0b10
#hexadecimales
0xf
0x9ac
#octales 
0o20
#convertir de base a 10 a otras
bin(7)
hex(100)
oct(234)

#int
i = int("11",2)
i2 = int("41",16)
#+= concatena
#strings
#indices negativos empiezas de atras para delante, comenzando por -1; en sentido normal empiezas con 0
#strign [start:fin]
# los strings son inmutables, lo que haces es una reasignacion o cambio de string 
name='bob'
name=name.title()
print(name)
#formateando
#string interpolation
pi=3.14
print(f"el numero {pi}")
print(f"el numero {pi+1}")
oracion="alguna palabra"
print("otro string que completa {}".format(oracion))
string="puedes tener {} u {} objeto"
print(string.format("uno", "otro"))
string.capitalize()
string.lower()
string.upper()

print(string.startswith("3"))
print(string.endswith("3"))
#extrae del string sin los caracteres de inicio y fin
print(string.strip("u"))
#reemplaza la ocurrencia del primer argumento con el segundo
print(string.replace("uno","dos"))
#split por defecto ocupa espacio
print(string.split())
print(string.count("{"))
var= "strings y listas tienen operaciones similares"
#substring
print(var[0:5])
print(var[-5:])
print(var)
x= float(input("intruduce un nmero"))
print(x)
#for each
for elemento in var:
    print(elemento)
lista=[1,2,3,4]
for indice, elemento in enumerate(lista):
    
    lista[indice]*=2
print(lista)
#tuplas
t=('Ana','Paola','Becerra','Zepeda')
print(t[0])
#t[0]='ana'<- error no puedes modificar la tupla

print(t.count)

#print(t.__add__('ols'))
#conjuntos agregan en orden
 #listas se pueden sumar, multiplicar
listas= ["A","BE","cora"]
#replace
l=[0,1,2,3,4,5,6,7]
l[3:6]=["a","b","c"]
print(l)
m=l
l[2]=22
#es una referencia, si cambias uno cambias los dos
print(l,m)
#crear una copia de la lista para mantener la independencia entre ambos
copy= list(l)
# len da la longitud de la lista
# min, max, 
# sorted reorganiza los numeros
# sum suma los valores si son enteros o
#print(list.sort())
print(sorted(list, reversed=True))

