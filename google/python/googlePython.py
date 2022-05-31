#potencias
x=10**2
#keywords
False	class	    finally	    is	    return
None	continue	for	        lambda	try
True	def	from	nonlocal	while
and	    del	global	not	        with
as	    elif	    if	        or	    yield
assert	else	    import	    pass	
break	except	    in	        raise	
#operators
    a + b = Adds a and b
    a - b = Subtracts b from a
    a * b = Multiplies a and b
    a / b = Divides a by b
    a ** b = Elevates a to the power of b. For non integer values of b, this becomes a root (i.e. a**(1/2) is the square root of a)
    a // b = The integer part of the integer division of a by b
    a % b = The remainder part of the integer division of a by b
abs()   delattr()   hash()  memoryview()    set()   all()   dict()  help()      min()
setattr()   any()   dir()   hex()   next()  slice()     ascii()divmod()id()object()
sorted()    bin()   enumerate()input()  oct()   staticmethod()bool()    eval()  int()
open()  str()
breakpoint()exec()      isinstance()          ord()       sum()   bytearray()
filter()    issubclass()pow()   super()       bytes()       float()     iter()      print()
tuple()     callable()  format()len()         property()    type()      chr()       frozenset()
list()      range()     vars()  classmethod() getattr()     locals()    repr()      zip()
compile()   globals()   map()   reversed()  __import__()    complex()   hasattr()   max()   round()
	
#datatypes
Strings "", ''
Integers
Floats
no puedes sumar strings y enteros
Preguntarle a python el tipo de un objeto usa 
print(type("string"))
#variables
deben comenzar con letras o (__)
solo letras, numeros o (__)
case sensitie naming

#Implicit convertion
#explicit convertion
#a string
number=10
print(str(number))
#functions
print ()
type()
str()
#user functions
def greeting(name):
    print("welcome, "+name)
def convert_seconds(seconds):
    #floor division me da el entero
    hours=seconds//3060
    minutes=(seconds-(hours*3600))//60
    remaining_seconds=seconds-(hours*3600+minutes *60)
    #return multim¿ple values, lo convierte a lista (autoboxing)
    return hours,minutes,seconds

#unboxing auomatico
hours,minutes,seconds=convert_seconds(123244)
print(hours,minutes,seconds)
#len() me dice el numero de elementos en un string o lista o iterable


def month_days(month,days):
    print(month+" has"+str(days)+" days.")
june="June"
july="July"
june_days = 30
july_days = 31

month_days(june,june_days)
month_days(july,july_days)

#code style
#codigo descriptivo
#operadores logicos
and or not
if 1<2:
    pass
elif 1>3:
    pass
else:
    pass


    a and b: True if both a and b are True. False otherwise.
    a or b: True if either a or b or both are True. False if both are False.
    not a: True if a is False, False if a is True.


#importante siempre inicializar las variables de lo contrario puedes agarrar un
#valor de alguna ejecución anterior
 #si range () recibe 3 parametros 
 #crea una secuencia entre el primero y ultimo incrementando lo indicado por el 3 parametro

for left in range(7):
    for right in range(left, 7):
        print("["+srt(left)+"|"+str(right)+"]",end=" ")
        #el parametro end le dice que el fin de linea no va a ser \n si no espacio
    print()
    #este print imprime el salto de linea
    if(true):
        pass
    else:
        pass

def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(start,stop+1):
			print(str(x*y), end=" ")
		print()

#String
#"" ''
#los strings son inmutables
len() longitud
regex strings
str.index("c")  me dice el valor de la primer ocurrencia
si no está da error

"string" in "sentence string"
me dice si un string está es substring de otro
puede servir por ejemplo para cambiar los dominios de email
strip() quita los espacion en blanco saltos de loniea tabs de inicio y fin
lstrip() quita los de la derecha
rstrip() quita los de la derecha
 
endswith()
isnumeric
int()
.join()
" ".join(["esta","linea"])  va a crear una linea con las palabras de la lista unidas con espacio

"una liniea con espacios ".split()
"string".capitalize
"String {} para {} rellenar{} con formato".format("palabras ","de ", " relleno ")
format te permite poner expresiones o variables dentro
"String {vari} para {otra} rellenar{mas} con formato".format(vari="2 ",otra="4 ", mas=" 6 ")
ejemplos de formatos a dos digitos
"string ${:.2f}".format(34.567)
"string ${price:.2f}".format(price=34.567)
"string {price} ${price:.2f}".format(price=34.567)
#formating le da formato al string sobre la cantidad de decimales eso se indica con <
for x in range(4,100,40):
    for y in range(5,500,170):
        "{ints:>3} F | {centi:>6.2f} C".format(centi=x,ints=y)

String operations

    len(string) Returns the length of the string
    for character in string Iterates over each character in the string
    if substring in string Checks whether the substring is part of the string
    string[i] Accesses the character at index i of the string, starting at zero
    string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

String methods

    string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
    string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
    string.count(substring) Returns the number of times substring is present in the string
    string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
    string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
    string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
    string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
    delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 

Expr	Meaning	Example
{:d}	integer value	                                '{:d}'.format(10.5) → '10'
{:.2f}	floating point with that many decimals	        '{:.2f}'.format(0.5) → '0.50'
{:.2s}	string with that many characters	            '{:.2s}'.format('Python') → 'Py'
{:<6s}	string aligned to the left that many spaces	    '{:<6s}'.format('Py') → 'Py    '
{:>6s}	string aligned to the right that many spaces	'{:>6s}'.format('Py') → '    Py'
{:^6s}	string centered in that many spaces	            '{:^6s}'.format('Py') → '  Py '
#una nueva manera de escribiro es
"base string with %d and %d placeholders" % (value1, value2)

str.capitalize("a")
str.rfind()



def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    input_string=input_string.capitalize()
    for letter in input_string:
        if not letter.isspace():
            new_string = new_string+letter
            reverse_string = letter+reverse_string
    if new_string==reverse_string:
            return True
    return False
def is_palindrome(input_string):
    start_time = time.time()
    new_string = ""
    reverse_string = ""
    for letter in input_string:
        if letter!=" ":
            letter=letter.capitalize()
            new_string = new_string+letter
            reverse_string = letter+reverse_string
    if new_string==reverse_string:
            print(time.time() - start_time)
            return True
    print(time.time() - start_time)
    return False

def is_palindrome(input_string):
...     new_string = ""
...     reverse_string = ""
...     input_string=input_string.replace(" ","")
...     input_string=input_string.capitalize()
...     for letter in input_string:
...         reverse_string = letter+reverse_string
...     if input_string==reverse_string:
...         return True
...     return False

start_time = time.time()
print(is_palindrome("Never Odd or Even"))
print(time.time() - start_time)

string="string"
string.rfind("in")
string.endswith("g")
#secuencias, 
# listas[]
len()
elemento in lista
lista[i]
lista.append() #agregar elementos al final
lista.insert(index, element)#agrega en una posicion
lista.remove(element)
lista.pop(index)
lista[index]=2

#tuplas son inmutables
#se escriben en () o []
#se usan cuando te quieres asegurar de que un elemento 
# se guardó en una posición específica y no cambia
# por ejemplo representar un nombre completo
# donde el primer elemento sea el nombre, el segundo app y 3 apm
# es decir la posicion en la tupla tiene significado
# por ejemplo cuando regresas más de un valor en una función 
# por ejemplo regresar horas minutos y segundos
def convert_seconds(seconds):
    hours=seconds//3600
    minutes=(seconds-hours*3600)//60
    remaining_seconds=seconds-hours*3600-minutes*60
    return hours,minutes,remaining_seconds

result=convert_seconds(5000)
type(result)
#el resultado es una tupla, donde el primer elemento serán horas, mins, seg
#las tuplas se pueden desempacar entonces 
horas, mins, segs= result
#enumeraciones
#quieres saber el indice de un elemento de la lista mientras caminas a travez de la lista
# usas range para crear un indice que te permita recorrer la lista o tupla 
#otra opcion es crear un enum, enumeration te da tuplas, un elemento es el indice el segundo es el elemento
winners=["Ashley","dylan","reese"]

for i in range(len(winners)):
    print("{}-{}".format(i+1,winners[i]))

for i,person in enumerate(winners):
    print("{}-{}".format(i+1,winners[i]))

for i in winners:
    print("{}-{}".format(i+1,person))

p26eFdZRpJV7vdc

new=()
new.add("2")

def skip_elements(elements):
	# code goes here
	new=[]
	for i,person in enumerate(elements):
		if i%2==0:
			new.append(person)
	return new

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

#trabajar con copias de una lista al iterar sobre ellas y modificarlas, para no alterar el orden de 
#indices y obtener resultados no deseados, se puede usar enumeration para ésto


#list comprenhension crea listas basadas en secuencias o 


#escribir multiplos de 7 hasta 70
multiples=[]
for x in range (1,11):
    multiples.append(x*7)

multiples=[x for x in range(1,70,7)]
multiples=[x for x in range(1,70,7) if x%3==0]#me dará los multiplos de 3



#listas
    len(sequence) Returns the length of the sequence
    for element in sequence Iterates over each element in the sequence
    if element in sequence Checks whether the element is part of the sequence
    sequence[i] Accesses the element at index i of the sequence, starting at zero
    sequence[i:j] Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
    for index, element in enumerate(sequence) Iterates over both the indexes and the elements in the sequence at the same time
    list[i] = x Replaces the element at index i with x
    list.append(x) Inserts x at the end of the list
    list.insert(i, x) Inserts x at index i
    list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
    list.remove(x) Removes the first occurrence of x in the list
    list.sort() Sorts the items in the list
    list.reverse() Reverses the order of items of the list
    list.clear() Removes all the items of the list
    list.copy() Creates a copy of the list
    list.extend(other_list) Appends all the elements of other_list at the end of list

List comprehension

    [expression for variable in sequence] Creates a new list based on the given sequence. Each element is the result of the given expression.

    [expression for variable in sequence if condition] Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true. 

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
for i,filename in enumerate(filenames):
    print("{}-{}".format(i+1,winners[i])) 
lis=[]
for i,filename in enumerate(filenames):
    if filename.endswith(".hpp"):
        filenames[i]=filename[:filename.rfind(".hpp")]+".h"
print(lis) 

string=""
string.endswith(".hpp")
p26eFd$ZRpJV7vdc

he permissions of a file in a Linux system are split into three sets of three permissions: read, write, 
and execute for the owner, group, and others. Each of the three values can be expressed 
as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. 
Or it can be written with a string using the letters r, w, and x or - when the permission is not granted. 
For example: 640 is read/write for the owner, read for the group, and no permissions for the others; 
converted to a string, it would be: "rw-r-----" 755 is read/write/execute 
for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"








filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames=[]
for i,filename in enumerate(filenames):
    if filename.endswith(".hpp"):
        newfilenames.append(filename[:filename.rfind(".hpp")]+".h")
    else:
        newfilenames.append(filename)
print(newfilenames) 



def pig_latin(text):
  say = ""
  # Separate the text into words
  pword=[]
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    pword.append(word[1:]+word[0]+"ay")
    # Turn the list back into a phrase
  return " ".join(pword)



def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for dig in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if dig>= value:
                result += letter
                dig -= value
            else:
                result += "-"
    return result


def group_list(group, users):
  members = ", ".join(users)
  return '"{grou}: {membe}"'.format(grou=group,membe=members)

def guest_list(guests):
	for invitado in guests:
		nombre,edad,prof= invitado
		print("{nom} is {ed} years old and works as {pro}.".format(nom=nombre, ed=edad,pro=prof))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#dictionaries
#key-value
#{}
nickname=dict(bob="boby",Alice='ally')
diccionario2={'Bob':'Bobby','Alice':'Ally'}

del nickname["bob"]

for name in nickname:
    print(name)

#itera sobre las llaves
# items o keys itera sobre los elementos
for  keys, values in nickname.items():
    print(keys,values)
#como keys puedes usar inmutables o primitives
# booleans, numbers
# no listas
nickname.
    len(dictionary) - Returns the number of items in the dictionary
    for key in dictionary - Iterates over each key in the dictionary
    for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
    if key in dictionary - Checks whether the key is in the dictionary
    dictionary[key] - Accesses the item with key key of the dictionary
    dictionary[key] = value - Sets the value associated with key
    del dictionary[key] - Removes the item with key key from the dictionary

    dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
    dict.keys() - Returns a sequence containing the keys in the dictionary
    dict.values() - Returns a sequence containing the values in the dictionary
    dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
    dict.clear() - Removes all the items of the dictionary

#strings lists dictionaries
#tuples sets

string.upper
string.replace



#Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses 
#into dictionaries, with names of their friends and how many guests each friend is bringing. 
#Each dictionary is a partial list, but Rory's list has more current information about the number of guests. 
#Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the 
#number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. 
#Then print the resulting dictionary.


def combine_guests(guests1, guests2):
    
    for persona,invitados in guests1.items():        
        guests2.update({persona:guests2.get(persona,0)+invitados})
    return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))
