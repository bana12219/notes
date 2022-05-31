#dictionaries and sets
#dictionarios
#dictionaries son key value
#indexados por keys que generalmente son strings
# las llaves son por defecto desordeadas
# guardan pares de valores  key- value en orden de inserción
# crear un diccionario
nickname=dict(bob="boby",Alice='ally')
diccionario2={'Bob':'Bobby','Alice':'Ally'}
#preguntar si es una instancia de dict
isinstance(nickname,dict)
type(nickname)
print(nickname["Alice"])
nickname["Ana"]=5
# para saber los metodos y propiedades de la clase de un objeto
dir(nickname)
another=nickname.copy()
#agregar
a={'a':1,'b':2}
another.update(a)
print(another)
another.update({2:'r'})
nickname.keys()
keys=dict.fromkeys(nickname)
#pop, devuelve el valor de la llave solicitada, si no la encuentra devuelve d 
#nickname.pop(k,d=None)
nickname.pop("Ana", None)
#devuelve el ultimo
nickname.popitem()
nickname.pop()


