#######Listas []
### listas  ordenadas
### indexadas
### contienen tipos arbitrarios
### nestable

#####Tuplas ()
# son listas inmutables , 
# son mejores para trabajar con tipos heterogeneos
# es más rápido iterar en ellas
# pueden usarse como llave de diccionarios
# se pueden pasar como parametro con la confianza de que no se van a cambiar
#tupla=(1,2,3,4,5,6,7,8,9)
# slicing, acceso a una parte de la tupla
#pedacito= tupla[inclusive_start_index: exclusive_stop_index:increment]

#########dictionarios
#nickname=dict(bob="boby",Alice='ally')
#diccionario2={'Bob':'Bobby','Alice':'Ally'}
#dictionaries son key value
#indexados por keys que generalmente son strings
# las llaves son por defecto desordeadas
# guardan pares de valores  key- value en orden de inserción
########sets{}
#lo sets son como las listas pero no indexados
# no repetidos
#sets son fifo entonces devuelven el primero

#packing, unpacking
#packing
#packing_tupla= 2,3,5,'letras'
#print(packing_tupla)
#unpacking
#a,b,c,d=packing_tupla


def decompress(texto):
   
    #tomar el primer set
    #leer en orden inverso
    # hacer impresion recursiva
    
    rev_indice= -1
    longitud=(len(texto))*-1
    indice =0
    numero=''
    letras=''
    is_string="c"
    constante=''
    print (rev_indice)
    #caso ideal
    while rev_indice>=longitud: 
        last_c= texto[rev_indice]
        print(last_c)
        if last_c==']':
            #nested case
            rev_indice-=1
            is_string="s"
            print("siguiente es caracter")
            continue
        if last_c=='[':
            rev_indice-=1
            is_string='n'
            print("siguiente es numero")
            continue
        print(is_string)
        if is_string=='c':
            constante=last_c
        if is_string=='s':
            letras=last_c+letras
        if is_string=='n':
            numero=last_c+numero   
        rev_indice-=1
    print(numero,letras,constante)
    repetir=int(numero)
    mensaje=letras* repetir
    print (mensaje+constante)



decompress("2[a]b")
 #revisar formato
    #n+[s+]*s   
