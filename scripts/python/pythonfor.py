import time
# Booleans
#

#if condition andor:
    #some code 
# elif
#else


#while condition:

#else <- else es opcional visualmente te permite saber que terminó el bucle, pero igual funciona si solo quitas el tab

#num % candidate  ==0 <- evalua que el residuo sea 0

#FOR
#para for necesitas un objeto que sea iterable, como listas archivos ...
#for  number in numberlist:

# range se usa para generar una lista de numeros
#iterar un numero específico de veces  (for lop)
# genera un indice disponible para el usuario
# range (start,stop, step)
# start es inclusive
# stop es exlusive 
# step es el numero de cambio de la secuencia
for i  in range (0,10):
    print (i)

for i  in range (0,-10,-1):
    print (i)

#generando coordenadas
cordenadas=[]
for x in range (0,5):
    for y in range(2,6):
        c = str(x)+','+str(y)
        cordenadas.append(c)
print (cordenadas)
# break continue pass
# break rompe el ciclo
# continue se salta la iteración pero continua el ciclo 

for x in range (0,5):
    for y in range(2,6):
        if y==3:
            pass
        c = str(x)+','+str(y)
        cordenadas.append(c)
print (cordenadas)

