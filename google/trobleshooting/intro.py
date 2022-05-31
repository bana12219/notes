"""
troubleshooting, edentificar, analizar y resolver problemas // el systema que corre la app
debbuging idntificar analizar y remover bugs // aplicacion
herramientas tcpdum y wireshark
"""


#comandos utiles
ps
top
free

strace para ver las llamadas hechas al systema por el programa
ltrace ver las librerias que llama el programa
#debuggers para ver el codigo linea a linea ver cambios en variables 
# interrumpir el programa bajo ciertas condiciones 
#1 geting informations
    # que issue es cuando pasó que hizo
    # reproduciton case como y cuando aparecio el problema
#2 encuetra la causa raiz 
#3 remediar
#4 documenta

"""Strace
systems calls son las llamdas que el programa hace al systema a la hora de ejecutarse
"""
strace ./purple.py | less
"""
que intentabas hacer
que pasos seguiste
que esperabas que hiciera
que hizo

"""
"""
Reproduction case
 verificar si el problema fue resuelto o no
"""
"""
linux 
/var/log/syslog.xsession-errors
MACOS
/Library/Logs
Windows
Eventviewer
"""
iostat
vmstat
iftop
# algunas consideraciones: 
#   la carga de la compuadora
#   cantidad de procesos concurrentes
#   el uso de la red

"""
    Efecto observador:
    los errores que desaparecen cuando los debuggeas, generalmente se tratan de 
    mal manejo de recursos como son memoria, conecciones de red
    archivos abiertos
"""

import re
def compare_strings(string1, string2):
    #Convert both strings to lowercase 
    #and remove leading and trailing blanks
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()
    #Ignore punctuation
    punctuation = r"[.?!,;:\-']"
    string1 = re.sub(punctuation, r"", string1)
    string2 = re.sub(punctuation, r"", string2)
    #DEBUG CODE GOES HERE
    print(string1+"  -  "+string2)
  return string1 == string2

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False





import datetime
from datetime import date

def add_year(date_obj):
    try:
        new_date_obj = date_obj.replace(year = date_obj.year + 1)
    except ValueError:
    # This gets executed when the above method fails, 
    # which means that we're making a Leap Year calculation
        new_date_obj = date_obj.replace(year = date_obj.year + 4)
    return new_date_obj

def next_date(date_string):
    # Convert the argument from string to date object
    date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
    next_date_obj = add_year(date_obj)
    # Convert the datetime object to string, 
    # in the format of "yyyy-mm-dd"
    next_date_string = next_date_obj.strftime("%Y-%m-%d")
    print(type(next_date_obj)) 
    return next_date_string

today = date.today()  # Get today's date
print(next_date(str(today))) 
# Should return a year from today, unless today is Leap Day


def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1


def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

cat contacts.csv | ./import.py --server test
# saber el numero de líneas
wc -l contacts.csv
# usar head o tail para ir obteniendo parte del archivo
head -20 contacts.csv
tail -20 contacts.csv
head -50 contacts.csv | ./import.py --server test
head -50 contacts.csv | head -25| ./import.py --server test




def find_item(list, item):
  #Returns True if the item is in the list, False if not.
    if len(list) == 0:
        return False
    list.sort()
  #Is the item in the center of the list?
    middle = len(list)//2
    if list[middle] == item:
        return True
  #Is the item in the first half of the list? 
    if item < list[middle]:
    #Call the function with the first half of the list
        return find_item(list[:middle], item)
    else:
    #Call the function with the second half of the list
        return find_item(list[middle+1:], item)
    return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False





"""
Question 3

The binary_search function returns the position of key in the list 
if found, or -1 if not found. We want to make sure that it's working 
correctly, so we need to place debugging lines to let us know each 
time that the list is cut in half, whether we're on the left or the 
right. Nothing needs to be printed when the key has been located.

For example, binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) first 
determines that the key, 3, is in the left half of the list, and 
prints "Checking the left side", then determines that it's in the 
right half of the new list and prints "Checking the right side", 
before returning the value of 2, which is the position of the key in 
the list. 
"""

def binary_search(list, key):
    #Returns the position of key in the list if found, -1 otherwise.
    #List must be sorted:
    list.sort()
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        if list[middle] == key:
            return middle
        if list[middle] > key:
            print("Checking the left side")
            right = middle - 1
        if list[middle] < key:
            print("Checking the rigth side")
            left = middle + 1
    return -1 

print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
"""Should print 2 debug lines and the return value:
Checking the left side
Checking the left side
0
"""

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
"""Should print no debug lines, as it's located immediately:
4
"""

print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
"""Should print 3 debug lines and the return value:
Checking the right side
Checking the left side
Checking the right side
6
"""

print(binary_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
"""Should print 3 debug lines and the return value:
Checking the right side
Checking the right side
Checking the right side
9
"""

print(binary_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
"""Should print 4 debug lines and the "not found" value of -1:
Checking the right side
Checking the right side
Checking the right side
Checking the right side
-1
"""


"""
Question 5

The best_search function compares linear_search and binary_search 
functions, to locate a key in the list, and returns how many steps 
each method took, and which one is the best for that situation. 
The list does not need to be sorted, as the binary_search function 
sorts it before proceeding (and uses one step to do so). 
Here, linear_search and binary_search functions both return the 
number of steps that it took to either locate the key, or determine 
that it's not in the list. If the number of steps is the same for 
both methods (including the extra step for sorting in binary_search), 
then the result is a tie. Fill in the blanks to make this work. 
"""
def linear_search(list, key):
    #Returns the number of steps to determine if key is in the list 
    #Initialize the counter of steps
    steps=0
    for i, item in enumerate(list):
        steps += 1
        if item == key:
            break
    return steps 

def binary_search(list, key):
    #Returns the number of steps to determine if key is in the list 
    #List must be sorted:
    list.sort()
    #The Sort was 1 step, so initialize the counter of steps to 1
    steps=1
    left = 0
    right = len(list) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        if list[middle] == key:
            break
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return steps 

def best_search(list, key):
    steps_linear = linear_search(list, key) 
    steps_binary = binary_search(list, key)
    results = "Linear: " + str(steps_linear) + " steps, "
    results += "Binary: " + str(steps_binary) + " steps. "
    if (steps_linear<steps_binary):
        results += "Best Search is Linear."
    elif (steps_linear>steps_binary):
        results += "Best Search is Binary."
    else:
        results += "Result is a Tie."
    return results
 
print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
#Should be: Linear: 1 steps, Binary: 4 steps. Best Search is Linear.

print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
#Should be: Linear: 4 steps, Binary: 4 steps. Result is a Tie.

print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
#Should be: Linear: 4 steps, Binary: 5 steps. Best Search is Linear.

print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
#Should be: Linear: 6 steps, Binary: 5 steps. Best Search is Binary.

print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
#Should be: Linear: 10 steps, Binary: 5 steps. Best Search is Binary.
