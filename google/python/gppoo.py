#google phyton poo
type()# me dice el tipo de un objeto
dir() # me dice los metodos y atributos que tiene
help("")# me da la documentacion del objeto, poner help


class Apple:
    pass #placeholder empty blocks

a= Apple()

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1




#Here, despite G.B. Shaw's quote, our characters have started with       
#different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with 
#one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
def exchange_apples(you, me):
    apple=you.apples
    you.apples=me.apples
    me.apples= apple
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    you.ideas+=me.ideas
    me.ideas=you.ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


#constructor

class Apple:
    """Class definition for the apple object sample"""
    #variables publicas 
    country=""
    #constructor
    def __init__(self,color,flavor):
        #variables privadas
        self.color=color
        self.flavor=flavor
    #metodo to string
    def __str__(self):
        #imprimir json de manzana
        return "Manzana[color:{color},sabor{sabor}]".format(color=self.color,sabor=self.flavor)


#docstreams, se escriben seguido de la declaracion de la funcion
def to_seconds(hours):
    """Return de amount of seconds contained in the specified amount of hours."""
    return hours*3600

#notebooks jupyter notebooks
# son contenedores de piezas de codigo 
#estas piezas de código se ejecutan dentro del notebook
# pueden contener imagenes widgets,  historias interactivas
#

#herencia 
class Fruit:
    sobrescribe="Fruit"
    def __init__(self, color,flavor):
        self.color=color
        self.flavor=flavor
    def get_sobrescribe(self):
        return sobrescribe
    def get_sobrescribe(self, another=2):
        return self.sobrescribe

class Apple(Fruit):
    sobrescribe="apple"


class Grape(Fruit):
    sobrescribe="grape"

app = Apple("a0","ba")
gra= Grape("green","d")
print(app)

print(app.sobrescribe)
print(app.get_sobrescribe())
print(app.get_sobrescribe(2))


#herencia is a
#composition tiene un, se accede por metodos
#siempre inicializa los atributos mutables en el constructor


gra1= Grape("green","d")
gra2= Grape("green","d")
print("Variables estaticas pueden ser publicas o no\n"+ str(Grape.sobrescribe)
+"-"+str(gra1.sobrescribe)
+"-"+str(gra2.sobrescribe)

)


Grape.sobrescribe=89;



print("Variables estaticas pueden ser publicas o no\n"+ str(Grape.sobrescribe)
+"-"+str(gra1.sobrescribe)
+"-"+str(gra2.sobrescribe)

)

gra2.sobrescribe=3
print("Variables estaticas pueden ser publicas o no\n"+ Grape.sobrescribe
+"-"+gra1.sobrescribe
+"-"+gra2.sobrescribe

)



#modulos
#organizar clases, funciones y datos
#como
 import String
 import random
 import datetime
 #datetime module, datetime class, now method
now= datetime.datetime.now()
random.randint(1,10)



lista =[]
lista.append(1)
