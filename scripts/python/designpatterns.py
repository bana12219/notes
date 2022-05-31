# clasificacion por comportamiento, relacion con otros, jerarquiz
''' iterators
    # es un patron donde tiene un next object, como listas, tuplas, dict, sets,
'''
lista=list()
iterator=lista.__iter__()
iterator.__next__()
'''decorators
     es una funcion que toma otra funcion y aumenta o extiende su funcionamiento
     sin modificarla 
     no aplica a las clases
     en python las funciones son firstclass- objects, lo que significa que pueden ser definidas 
     dentro de otras funciones o incluso retornadas por otras funciones
'''
''' herencia
    una clase (clase hija) se define en funcion de otra (clase padre)
    overriding, una clase provee un comportamiento distinto
    overloading la clase hija provee ina implementacion distinta del metodo definido en la clase padre
    overloading definir el mismo metodo, con la misma firma oero diferentes argumentos
'''
object.__bases__() # da una tupla que puede estar vacia que contiene las clases padre
object.__subclases__() #cada clase tiene una lista que referencía a las subclases inmediatas
class Pet(object):
    """Clase base para todas las mascotas"""
    def __init__(self, name, species):
        self.name= name
        self.species= species
    def get_name(self):
        return self.name
    def get_species(self):
        return self.species
    def __str__():
        return "%s is a %s" % (self.name, self.species)
class Dog (Pet):
    def __init__(self,name,chases_cats):
        super().__init__(name, "Dog")

Pet.__subclasses__()
Dog.__bases__()
#herencia multiple
'''
'''
__mro__ # es una tupla de clases que van a ser consideradas como base clases para la resolucion de un método

class A(object):
    def __init__(self):
        print('A')
    @staticmethod
    def foo():
        print('foo')
class B (object):
    def __init__(self):
        print('B')
    @staticmethod
    def bar():
        print('bar')
class C (A,B):
    def foobar(self):
        self.foo()
        self.bar()
'''
c=c() imprime A, puesto que el metodo init se toma de la clase A, 
    va a tomar los metodos por orden de precedencia
c.__mro__ imprime todas las clases de las que va extentiendo
'''
'''factory
    defina una interface para la creacion de objetos, 
    dejando la instanciación para el momento de ejecución.
    la idea es proveer una manea de crear objetos en tiempo de ejecucion conforme el usuario 
    lo necesite
'''
#ejemplo tenemos un shapeInterface que es extendido por clases concretas como circle, square
#    rectangle, pero tambien tenemos un shape factory que devuelve instancias de shape segun se las pida 
#    factoryPatternDemo
class ShapeInterface:
    def draw(self):
        '''Draw interface definition, this must be implemetes by the subclasses
        '''
        pass
class Circle (ShapeInterface):
    def draw (self):
        print ("Circle.draw")
class Square (ShapeInterface):
    def draw (self):
        print ("Square.draw")
class ShapeFactory (ShapeInterface):
    @staticmethod
    def get_shape (type):
        if type=='circle':
            return Circle()
        if type=='square':
            return Square()
        assert 0, "Type not suported"
'''Abstract Factory
    proveer la interface para crear familias de objetos relacionados 
    sin especificar sus clases concretas
    es básicamente la misma idea que factory con una capa más de abstracción o flexibilidad
    *crear una familia de interfaces o clases abstractas
    *crear clases abstractas para cada una de éstas
    *crear abstract factory que se aplique para toda la familia
    *crear una concrete factory para cada clase base
'''
class Shape2DInterface:
    def draw(self):
        '''Draw interface definition, this must be implemetes by the subclasses
        '''
        pass
class Shape3DInterface:
    def build(self):
        '''Draw interface definition, this must be implemetes by the subclasses
        '''
        pass
#concrete shape classes
class Circle (Shape2DInterface):
    def draw (self):
        print ("Circle.draw")
class Square (Shape2DInterface):
    def draw (self):
        print ("Square.draw")
class Sphere (Shape3DInterface):
    def draw (self):
        print ("Circle.build")
class Cube (Shape3DInterface):
    def draw (self):
        print ("Square.build")


7 years of experience