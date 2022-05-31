### listas  ordenadas
### indexadas
### contienen tipos arbitrarios
### nestable
lista =[]
lista.append(1)
####hace split de iterable y agrega todos los elementos de otro
#lista.extend(iterable)
#lista.insert(index,item)
#lista.remove(item)
#lista.pop()
#lista.pop(index)
lista.clear()
####devuelve la primer ocurrencia de un item
####puede darse el rango de elementos entre los que evaluar
#lista.index(item,opt_start,opt_end)
#lista.count(value)
#lista.sort(key=None, reverse=False)
lista.reverse()
lista.copy()
#lista.clear() es igual que del a[:]

lista_numbers =[1,2,3,4,5,6,7,8,9,10]
letters=['a','b','c','d']
'''
lista_numbers.append(1)
lista_numbers.extend(iterable)
lista_numbers.insert(index,item)
lista_numbers.remove(item)
lista_numbers.pop()
lista_numbers.pop(1)
lista_numbers.clear()
lista_numbers.index(item,opt_start,opt_end)
lista_numbers.count()
lista_numbers.sort(key=None, reverse=False)
lista_numbers.reverse()
lista_numbers.copy()
'''
squares = [num **2 for num in range(1,11)]
print (squares)


def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  list1.reverse()
  return list2.extend(list1)
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
Jamies_list.reverse()
Drews_list.append(Jamies_list)

#####Tuplas
# son listas inmutables , 
# son mejores para trabajar con tipos heterogeneos
# es más rápido iterar en ellas
# pueden usarse como llave de diccionarios
# se pueden pasar como parametro con la confianza de que no se van a cambiar
tupla=(1,2,3,4,5,6,7,8,9)
# slicing, acceso a una parte de la tupla
#pedacito= tupla[inclusive_start_index: exclusive_stop_index:increment]

#packing, unpacking
#packing
packing_tupla= 2,3,5,'letras'
print(packing_tupla)
#unpacking
a,b,c,d=packing_tupla
print(a)
print(b)
print(c)
print(d)
print(packing_tupla)
#slicing
tupla_range= tupla[2:5]
#de 2 a fin peor de dos en dos
even_nums= tupla[1::2]
#desde el inicio pero de dos en dos
odd_nums= tupla[0::2]
# una funcion puede regresar más de un valor si devuelves la tupla

def calcula_area(radio):
    import math
    return (math.pi*radio**2, 2*math.pi*radio)

#meodos de tuplas
# me dice si algo es iterabe
pets=('perro','gato','caballo')
print(any(pets))
print(any(pets[1]))

#count, me dice en número de ocurrencias de un elemento
print(pets.count("cat"))
print (max(pets))
print (min(pets))
