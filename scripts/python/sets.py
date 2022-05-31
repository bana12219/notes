#lo sets son como las listas pero no indexados
# no repetidos
a={1,2,3}
b={2,3,4}

#iterar
for item in a:
    print (item)

a.add(4)
b.add(5)

# al update le pasas otro set que es el que va a unir con el actual, omitiendo repetidos

b.update({6,7,8,9})
#eliminar objetos
b.remove(9)
b.discard(8)
#sets son fifo entonces devuelven el primero
print (b.pop())
a.update({5,6,7,8})
b.update ({9,10,11,12,13})
#################################################
###operaciones con sets
#################################################

#>>> print (a)
#{1, 2, 3, 4, 5, 6, 7, 8}
#>>> print (b)
#{3, 4, 6, 7, 9, 10, 11, 12, 13}
#union
c= a.union(b)
c= a|b
#intersection
d= a.intersection(b)
d=a&b
#diferencia
e=a.difference(b)
e=a-b
# diferencia simetrica, que es a negacion de la diferencia
a.symmetric_difference(b)
#subset
a.issubset(b)
# super set, 
a.issuperset(b)

c= a.copy()
a.pop()
print(a)
print(c)


c= a
a.pop()
print(a)
print(c)

#frozen set, son sets inmutables
a= frozenset([1,2,3])







