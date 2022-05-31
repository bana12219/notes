# Testing
# Evaluar que el código haga lo que se espera de él
# Automating testing
# Unit test
# Integration test
# Test driven development
# Automating testing, revision automática de que el código cumple las expectations
#   Test cases, que pasa si... las variantes de validacion de inputs
# Unit test: probar partes aisladas de código, comprueban piezas pequeñas 
#   de código como funciones o métodos
#este modulo se llama  rearrange.py
import re
def rearrange_name(name):
    result=re.search(r"^([\w.]*),([\w.]*)$",name)
    return"{}{}".format(result[2],result[1])

# Automatic testing su caracteristica es correras tantas veces como sea necesario
# se escribe en un script separado el archivo debe tener el mismo nombre_test
# rearrange_test.py
#!/usr/bin/env python3
# 2 se importa el modulo que estamos testeando
from rearrange import rearrange_name
import unittest
# 3 importar unittest, para poder usar la clase TestCase para extenderla y heredar sus metodos
class TestRearrange(unittest.TesCase):
# 4. los metodos que empiecen con test se convierten e test automaticamente 
# cuando se corre el framework testing
    def test_basic(self):
    testcase="Lovelace, Ada"
    expected="Ada Lovelace"
    self.assertEqual(rearrange_name(testcase),expected)
    def test_empty(self):
        testcase= ""
        expected=""
        self.assertEqual(rearrange_name(testcase),expected)
# como llamar el test
unittest.main()
# 5. hacer el script ejecutable y correrlo
chmod +x rearrange_test.py
./rearrange_test.py
# Automated test
# Edge cases son inputs en el codigo que producen resultados inesperados

class TestRearrange(unittest.TesCase):
    def test_basic(self):
    testcase="Lovelace, Ada"
    expected="Ada Lovelace"
    self.assertEqual(rearrange_name(testcase),expected)
    def test_empty(self):
        testcase= ""
        expected=""
        self.assertEqual(rearrange_name(testcase),expected)
    def test_double_name(self):
        testcase="Hopper, Grace M."
        expected="grace M. Hopper"
        self.assertEqual(rearrange_name(testcase),expected)
# Understand basic assertions:
# Method	                Checks that	    New in
# assertEqual(a, b) 	    a == b	
# assertNotEqual(a, b)  	a != b	
# assertTrue(x) 	        bool(x) is True	
# assertFalse(x)	        bool(x) is False	
# assertIs(a, b)	        a is b	            3.1
# assertIsNot(a, b) 	    a is not b	        3.1
# assertIsNone(x)	        x is None	        3.1
# assertIsNotNone(x)    	x is not None   	3.1
# assertIn(a, b)    	    a in b	            3.1
# assertNotIn(a, b)	        a not in b	        3.1
# assertIsInstance(a, b)	isinstance(a, b)	3.2
# assertNotIsInstance(a, b)	not isinstance(a, b)3.2
# 
# unittest en jupyter debe correrse  unittest.main(argv = ['first-arg-is-ignored'], exit = False)
# pues por defecto busca sys.argv[0] y como no se lo pasamos ocurre error
# 
# Black Box vs WhiteBox, 
# Whitebox , clear box o transparent testing, descansa en el conocimiento de los 
# creadores del sw para construir los test cases
# Blak Box testing, el tester no sabe nada sobre el sw, no conoce los internals, solo sabe 
#   lo que se supone que el sw haga, sus requerimeintos o especificaciones, pero no como lo haga
# Unit test, se centran en la evaluacion de una funcionalidad específica
# Integration test verifica que la relacion entre diferentes piezas de código en diferentes ambientes,
#   sea segun lo esperado 
# Entonces una unit test no verifica un request de la red
# Integration test verifica la conexion con la db, o la red, prueba el sistema en su totalidad
#   toma modulos de codigo que unite test verificó, los combina y comprueba
#   dependeindo de los modulos que creamos y la interaccion , se crea un test environment, 
#   que corre la version test del software que se intenta validar
# regression test son una variante de Integration test, escritas como parte de debbuging y 
#   troubleshooting para verificar que el issue o error ha sido arreglado
#   un buen approach para encontrar bugs es test fails by triggering el comportamiento del bug
#   arregla el bug para que el test pase y el error no se repita, el error no debe repetirse
#   si es que el el regresssion test no falla 
# Build verification test o smoke test. obteinen su nombre de un concepto que viene de test 
#   hardware equipment, que es conecta la pieza de hw y ve si se incendia o hace humo.
#   en sw estas pruebas son de sanidad para revisar y encontrar mas bugs en un programa
#   responde preguntas como el código corre?, en el puerto que es?
#   estas pruebas son manuales generalmente con poco input
# Load test, verifica que el sistema se comporta bien aún bajo cargas de trabajo considerables
#   simular tráfico de servicio asegurandose de que el performance no se degrade
#   buscar que se comporte igual con 100 usuarios que con 100000
# Test suite, grupo de test de uno o varios tipos
#            
# ##
# 
# Test Driven Development
# ##
# 
# Escribe el test antes del desarrollo, pensando en las maneras en que fallara, 
# en cuentras el problema que resolver
# esceribes el test donde deberá fallar el codigo y lo corres, una vez que falla  lo corriges
# Continuos integration  el repo de codigo 
# 
# Errores y exceptions
# Cuando ocurre un error, el interprete detiene la ejecución, a veces es facil 
# verificar una condicional para invalidar el error
# TypeError, IndexError, ValueError
# El reto es validar todo lo que puede salir mal
import os
def read_file(filename):
    if not os.path.exists(filename):
        return ""
    if not os.path.isfile(filename):
        return""
    if not os.access(filename, os.R_OK):
        return""
    if is_locked(filename):
        return""
    if is_not_acceccible(filename):
        return ""
    #estas validaciones se pueden omitir con trycatch
    try:
        f=open(filename)
    except OSError:
        return None
# 
# Raising errors
# verificar que se escogio un username valido, como 
# raise errer es como throw exception
if minlen<1:
    raise ValueError("minlen must be at least 1")
#assert para validaciones tipo continua si condicion valida, si no lanza error
AssertionError
assert type(username)==str, "username must be a string"

import unittest
from validations import validate_user
class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser",3),True)
    def test_too_short(self):
        self.assertEqual(validate_user("inv",5),False)
    def test_invalid(self):
        #en caso de cumplir la condicion lanza error
        #es una negacion del asser
        self.assertRaises(ValueError,validate_user,"user",-1)
unittest.main()

######sample#########
# Imagine one of your IT coworkers just retired and left a folder of scripts for you to use. 
# One of the scripts, called emails.py, matches users to an email address and lets us easily 
# look them up! For the most part, the script works great — you enter in an employee's name 
# and their email is printed to the screen. But, for some employees, the output doesn't look 
# quite right. Your job is to add a test to reproduce the bug, make the necessary corrections, 
# and verify that all the tests pass to make sure the script works! Best of luck!
# 
# 
#    Write a simple test to check for basic functionality
#    Write a test to check for edge cases
#    Correct code with a try/except statement
# 
# First, you need to find the .csv file called user_emails.csv, which contains user names and 
# their respective email addresses within the data directory. Navigate to this directory using 
# the following command:
#   cd ~/data
# ##
# This script consists of two functions: populate_dictionary(filename) and find_email(argv). 
# The function populate_dictionary(filename) reads the user_emails.csv file and populates a 
# dictionary with name/value pairs. The other function, find_emails(argv), searches the dictionary 
# created in the previous function for the user name passed to the function as a parameter. 
# It then returns the associated email address. This script accepts employee's first name and last
#  name as command-line arguments and outputs their email address.
#
# The script accepts arguments through the command line. These arguments are stored in a list 
# named sys.argv. The first element of this list, i.e. argv[0], is always the name of the file 
# being executed. So the parameters, i.e., first name and last name, are then stored in argv[1] 
# and argv[2] respectively.
#
# Let's test the script now.
#
# Since you know the contents of the user_emails.csv file, choose any name to be passed as a parameter,
# or you can use the following name:
#   python3 emails.py Blossom Gill
# This will give you the email address associated with the Full Name passed as parameters. 
# In this case, the name is Blossom Gill and the email ID associated with this 
# name is blossom@abc.edu.

# Test cases
# 
# In this section, we will write a basic test case and see how it works. 
# A test case is an individual unit of testing that checks for a specific response to a particular 
# set of inputs.
# Use the following command to create a new file (in scripts directory) to write our test cases:
#       nano ~/scripts/emails_test.py
# 
#!/usr/bin/env python3
import unittest
from emails import find_email
class EmailsTest(unittest.TestCase):
# Another important aspect of the unittest module is the test runner. 
# A test runner is a component that orchestrates the execution of tests and provides 
# the outcome to the user.
# A test case is created by subclassing unittest.TestCase. Let's write our first basic 
# test case, test_basic.
    def test_basic(self):
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@abc.edu"
        self.assertEqual(find_email(testcase), expected)
    def test_one_name(self):
        testcase = [None, "John"]
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)
if __name__ == '__main__':
  unittest.main()
# Test Case 1: Missing parameters
#  Let's say, in this case, your script should output "Missing parameter".
# There are two ways to solve this issue:
#    Use a try/except clause to handle IndexError.
#    Check the length of input parameters before traversing the user_emails.csv file 
#       for the email address.
#   
#    First, we execute the try clause.
#    If no exception occurs, the except clause is ignored.
#    If an exception occurs during the execution of the try clause, the rest of the try clause 
#       is then skipped.
#    It then attempts to match the type with the exception named after the except keyword. 
#       If this matches, the except clause is executed. If it doesn't, the control is passed 
#       on to outer try statements. If no handler is found, it's an unhandled exception and 
#       the execution stops with an error message.
#
# emails.py

#!/usr/bin/env python3

import sys
import csv


def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/student-00-551dcb7cc20a/data/user_emails.csv')
    # Find and print the email
    return email_dict.get(fullname.lower())
  except IndexError:
    return "Missing parameters"

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()

##### Test Case 2: Random email address
# 
#!/usr/bin/env python3

import unittest
from emails import find_email


class EmailsTest(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)

  def test_one_name(self):
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)

  def test_two_name(self):
    testcase = [None, "Roy","Cooper"]
    expected = "No email address found"
    self.assertEqual(find_email(testcase), expected)

if __name__ == '__main__':
  unittest.main()
# 


#!/usr/bin/env python3

import csv
import sys


def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/student-00-551dcb7cc20a/data/user_emails.csv')
     # If email exists, print it
    if email_dict.get(fullname.lower()):
      return email_dict.get(fullname.lower())
    else:
      return "No email address found"
  except IndexError:
    return "Missing parameters"

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()

# 
# 
# 
# 
# 
#  
cat user_emails.csv
Blossom Gill,blossom@abc.edu,
Hayes Delgado,nonummy@abc.edu
Petra Jones,ac@abc.edu
Oleg Noel,noel@abc.edu
Ahmed Miller,ahmed.miller@abc.edu
Macaulay Douglas,mdouglas@abc.edu
Aurora Grant,enim.non@abc.edu
Madison Mcintosh,mcintosh@abc.edu
Montana Powell,montanap@abc.edu
Rogan Robinson,rr.robinson@abc.edu
Simon Rivera,sri@abc.edu
Benedict Pacheco,bpacheco@abc.edu
Maisie Hendrix,mai.hendrix@abc.edu
Xaviera Gould,xlg@abc.edu
Oren Rollins,oren@abc.edu
Flavia Santiago,flavia@abc.edu
Jackson Owens,jacksonowens@abc.edu
Britanni Humphrey,britanni@abc.edu
Kirk Nixon,kirknixon@abc.edu
Bree Campbell,breee@abc.edu


