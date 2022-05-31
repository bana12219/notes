###modulos
#funciones elaiconadas en un archivo py
# primero se buscan los modulos en el current directory si no se busca un built-in python module sys.path
import time
#import myModule
#otra opcion 
#from myModule import*

#standard modules
#string
#math
#unittest
#sys
#os
#urlib
#time
#random
#re
#itertools
#functools

#import turtle, time
import time
print (help(time))
print (time.__dict__)

#packages
#collection de modulos en directorio 


#importar modulos 
from favvObjects import car, webbrowser
#importar un modulo
from faveObjects import car
#importar recursos específicos de un modulo
from faveObjects.Car import accelerate
#import module as an abbreviation
from faveobjects import webbrowser as wb
#importar cada funcion en un medulo sin prefijo
from faveobjets.car import *

t=time

t.clock()