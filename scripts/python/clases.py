#clases
class Person:
    pass
    #class attributes declaration
    # se declara aqui y se accesan Clase.attr
    tipo_sangre="universal"
    #constructor self es como this de java
    def __init__(self, att1,protected_att, private_att):
        #los attributes aqui son de instancia, se accesan obj.attr
        self.name=att1
    #protected attributes aquellos que no deben modificarse fuera de la clase
        self._protected_att= protected_att
    #private aquellos que no pueden modificarse fuera de la clase, necesitan getters y setters
        self.__private_att= private_att
    def get_private_att(self):
        return self.__private_att
    def set_private_att(self, value):
        self.__private_att=value        
    #instance methods, cualquier objeto de la instancia puede mejorar
    #pueden usar o cabiar los attributos y se invocan obj.method
    def greatings(self):
        print("Helo!")
    #valores por defecto
    def favourite_food(self,food="eggs"):
        self.favourite_food=food
    
    #metodos de clase: no tienen acceso a los atributos de instancia
    #@classmethos identifier, el primer atributo es la clase en si
    @classmethod
    def change_something(cls,atr):
        # como accedo a los atributos?
        cls.tipo_sangre= atr

######################
# Herencia
######################    
class Cat:
    def __init__(self,mass,lifespan,speed):
        self.mass_in_kg=mass
    def vocalize (self):
        print('meeeowww')
    
class Leopard (Cat):
    #overriding
    def vocalize(self):
        print("wwghhrr")

class Cheeta (Cat, Leopard):
    def __init__(self,mass,lifespan,speed):
        super().__init__(mass,lifespan,speed)
    def vocalize(self):
        return super().vocalize()


#dunder methods son los que tienen __init__ doble uin bajo al inicio y final

me= Person()
you= Person("Ana")
#puedes agregar atributos a un objeto ya instanciado 
#me.__dict__={}
me.name="ana"
#imprimir el dictionary de un objeto(incluye sus atributos y metodos algo como tostring)
print (me.__dict__)
#imprime diccionario de objeto
print (me.__dict__)
#imprime diccionario de clase
print (Person.__dict__)

##importante cuando modificas un att de clase mediante el objeto, en realidad se hace unacopia del objeto 
##y se modifica el valor
## cuando lo haces mediante la clase, se modifica para todas las instancias de la clase
#cambio para todos
Person.tipo_sangre="+o"
#cambio solo para un objeto
me.tipo_sangre="a"
