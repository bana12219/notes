#regular expression
#consulta de busquda de texto expresado en un string pattern
# se usa para busquedas como palabras de 4 lettras en un archivo
# tipos de errores e un log
# modulo de expresiones regulares
import re
# en cmd o terminal:
# grep, buscar las palabras con thon en el nombre
#grep thon /home/texto.txt
# grep es case sensitive para ignorarlo usar -i
# comodines como . que significa 1 cualquier
# grep l.rts /home/texto.txt
# buscará  las palabras que tengan l seguido de un caracter seguido de rts
# en python
#busca el primer ocurrencia aza en el string plaza
result= re.search(r"aza","plaza")
# r: rawstring
# <re.Match object; span=(2, 5), match='aza'>
# el resultado me indica en span, la ubicacion de la ocurrencia dentro del string
# ^x que empiece con x
# [ab] cuanquier caracter del conjunto
# [^ab] cualquierncaracter que no este en el grupo
# [^a-zA-Z] que no sea lettra
#  | una expresion o la otra
# busque gato o perro
re.search(r"cat|dog", "like cats and dogs")
# buscar todas las coincidencias
print(re.findall(r"cat|dog", "like cats and dogs"))
#.* cualquier caracter 0 o mas veces
re.search(r"Py.*n", "Pyton Programming")
# greedy, ambicioso porque el pattern abarca no solo pyton si no programin toma la ulltima n
# si queremos que estén en la misma palabra, podemos:
re.search(r"Py[a-z]*n", "Pyton Programming")
# + una o mas ocurrencias
re.search(r"o+l+","woolly")
#  busca una o mas o seguidas de 1 o mas l
# ? 0 o una vez
re.search(r"p?each", "to each word")
# la p puede o no estar pero each si debe estar
# review .*+?^$[]
# secuencias de escape y caracteres especiales
# \. para buscar puntos, \n, \t
re.search(r"\.com","web.com")
# \w alfanumericos, letras numero y _
re.search(r"\w*", "this is an example")
# \d para digitos
# \s para caracteres
# $ para indicar fin de la linea 
# ^ para indicar que empieza la linea
r"^[a-zA-Z_]\w*$"

# # # # 

#The check_web_address function checks if the text passed qualifies as a 
#top-level web address, meaning that it contains alphanumeric 
#characters (which includes letters, numbers, and underscores), 
#as well as periods, dashes, and a plus sign, followed by a period and a 
#character-only top-level domain such as ".com", ".info", ".edu", etc. 
#Fill in the regular expression to do that, using escape characters, 
#wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.

import re
def check_web_address(text):
  pattern = r"[\w\.\-\+][\.com|\.info|\.edu]"
  result = re.search(r"^[\w\-\.\+]+\.[a-zA-Z]+$", text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True
print(check_web_address("My_Favorite-Blog.US2")) # True
print(check_web_address("$My_Favorite-Blog.US")) # False

'''Question 2

The check_time function checks for the time format of a 12-hour clock, as follows: 
the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes 
between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. 
Fill in the regular expression to do that. 
How many of the concepts that you just learned can you use here?'''

import re
def check_time(text):
  pattern = r"^((1[0-2])|(0?[0-9])):([0-5][0-9]) ?(AM|PM|am|pm)$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


'''Question 3

The contains_acronym function checks the text for the presence of 
2 or more characters or digits surrounded by parentheses, with at 
least the first character in uppercase (if it's a letter), returning True 
if the condition is met, or False otherwise. For example, "Instant messaging 
(IM) is a set of communication technologies used for text-based communication" 
should return True since (IM) satisfies the match conditions." 
Fill in the regular expression in this function: '''

import re
def contains_acronym(text):
  pattern =r"\([A-Z0-9][A-Za-z0-9]*.*\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True

print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True

print(contains_acronym("Please do NOT enter without permission!")) # False

print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True

print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


'''Question 6
Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as 
follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits. 
The zip code needs to be preceded by at least one space, and cannot be at the start of the text.'''
import re
def check_zip_code (text):
  result = re.search(r"^.* [0-9]{5}(-[0-9]{4})?", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False


###advanced

# Capturing groups
# extrer la porcion de información que cumple con el pattern para ser input de otro proceso
# Capturing groups son porciones de patrones que se encierran en paŕentesis
# por ejemplo tienes un archivo con lineas donde se encuentra app , nombre
# 
result= re.search(r"^(\w*), (\w*)$","Lovelace, Ada")
print(result.groups())
('lovelace','Ada')
result[0]# contiene la tupla
result[1]#contiene el apellido
result[2]# contiene el nombre
# el resultado es una tupla de dos elementos
# repetir una cantidad defnida de veces numeric repetition cualifiers
r"a{5}" # repetir a 5 veces
r"[a-z]{5}"# busca 5 letras repetidas
# buscador , es una palabra válida, pues tiene almenos 5 letras repetidas
# que pasa si solo quieres las que contengan exactamente 5 letras?
# \b , se debe poner al principio y final del pattern
r"\b[a-z]{5}\b"
# de ésta manera solo contarán as palaras que tengan 5 letras de longitud
# la repeticion puede ser parte de un rango
r'[a-z]{5,10}' # buscará las palabras que tengan entre 5 y 10 palabras
# el rango puede ser abierto, para indicar las palabras que tengan más de 5 letras
r'[a-z]{5,}'
# buscar las palabras que tengan hasta 8 letras
res=re.findall(r"\b[a-z]{,8}\b","probando este intervalo el tipo   de palabrassssssssssssssssssssss")
print(res)
# buscar los pid de un log
reg=r"\[(\d+)\]"
res=re.search(reg,"esta es una linea de log proceso[2222]")
print(res)
print(res[0])
def extract_pid(log_line):
    regex = r"\[(\d+)\]: \b([A-Z]{2,})\b"
    result = re.search(regex, log_line)
    print(result,"------",result.groups())
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])
print(extract_pid("A string [34567] but no uppercase message")) # None
# Split y replace
# split te permite separar oraciones por  regex
reg=r"[.!?]"
re.split(reg,"unaoracion. otra! Una más? si otra!")
# ['unaoracion', ' otra', ' Una más', ' si otra', '']
# no incluye el simbolo, para incluirlo
reg=r"([.!?])"
re.split(reg,"unaoracion. otra! Una más? si otra!")

# sub, te permite sustituir la parte del string que contiene el pattern
# con replace
#busca email
import re
reg=r"[\w.%+-]+@[\w.-]+"
#a sub se le pasa el regex y la palabra con que reemplazar
re.sub(reg,"[CONFIDENCIAL]","mensaje recibido de ico.ana@gmail.com")
# puedes reformatear o reemplazar
re.sub(r"^([\w.-]*), ([\w.-]*)",r"\2 \1","Lovelace, Ada")
#el output:
'Ada Lovelace'
# r"^([\w.-]*), ([\w.-]*)" le pasamos  dos () () por lo que creo 2 output o capturing groups
# r"\2 \1" ---->\2 y \1 representan los output o capturing groups que buscamos, y le decimos como pintarlos
# "Lovelace, Ada" ---> es el texo de donde sacamos la informacion
re.sub(r"^([\w.-]*), ([\w.-]*)",r"Her name is \2 and Her last name \1","Lovelace, Ada")
#el output:
'Her name is Ada and Her last name Lovelace'
# 
'''1.
Question 1
We're working with a CSV file, which contains employee information. 
Each record has a name field, followed by a phone number field, and a role field. 
The phone number field contains U.S. phone numbers, and needs to be modified to the 
international format, with "+1-" in front of the phone number. 
Fill in the regular expression, using groups, to use the transform_record function to do that.'''
import re
def transform_record(record):
  #pattern=r",([0-9]{3}-?[0-9]{3}-?[0-9]{4}),"
  pattern=r",([0-9\-]{10,12}),"
  format=r",+1-\1,"
  new_record = re.sub(pattern,format,record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

'''2.
Question 2

The multi_vowel_words function returns all words with 3 or more 
consecutive vowels (a, e, i, o, u). 
Fill in the regular expression to do that.'''
import re
def multi_vowel_words(text):
  pattern = " ?(\w*[aeiou]{3}\w*) ?"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) # ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) # ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) # ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) # ['queue']

print(multi_vowel_words("Hello world!")) # []

'''4.
Question 4

The transform_comments function converts comments in a Python script into those usable 
by a C compiler. This means looking for text that begins with a hash mark (#) and 
replacing it with double slashes (//), which is the C single-line comment indicator. 
For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded 
inside of a Python command, and assume that it's only used to indicate a comment. 
We also want to treat repetitive hash marks (##), (###), etc., as a single comment 
indicator, to be replaced with just (//) and not (#//) or (//#). 
Fill in the parameters of the substitution method to complete this function: '''
import re
def transform_comments(line_of_code):
  pattern=r"(#+)"
  format=r"//"
  result = re.sub(pattern,format,line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

'''
5.
Question 5
The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX 
(3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), and 
converts it to a more formal format that looks like this: (XXX) XXX-XXXX. Fill in the 
regular expression to complete this function.'''

import re
def convert_phone_number(phone):
  pattern=r"\b([0-9]{3})-([0-9]{3}-[0-9]{4})\b"
  format=r"(\1) \2"
  result = re.sub(pattern,format,phone)
  if result is None:
        return None
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300


phone="mensaje 212-345-9999."
phone="123-123-12345"
pattern=r"\b([0-9]{3})-([0-9]{3}-[0-9]{4})\b"
result = re.search(pattern,phone)
print(result.groups())


##final 
#buscar en un user_emails.csv, los dominios abc.edu y reemṕlazarlos con xyz.edu
#!/usr/bin/env python3
import re
import csv
def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,
  in the domain position, false if not."""
  domain_pattern=r'[\w\.-]+@'+domain+'$'
  if re.match(domain_pattern,address):
    return True
  return False

def replace_domain(address, old_domain,new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern=r''+old_domain+'$'
  address= re.sub(old_domain_pattern,new_domain,address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  #constantes nuevo/ viejo dominio, archivo de correos y reporte de salida
  old_domain, new_domain="abc.edu","xyz.edu"
  csv_file_location="/home/user/data/user_emails.csv"
  report_file= "/home/user/data"+'/updated_user_emails.csv'
  #declarando las variables, lista de emails
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []

  with open(csv_file_location, 'r') as f:
    #leyendo el archivo y extrallendo los email
    user_data_list = list(csv.reader(f))
    #pasando de rows a lista
    user_email_list = [data[1].strip() for data in user_data_list[1:]]
  #procesando la lista
  for email_address in user_email_list:
    #validando que tenga el aniguo dominio
    if contains_domain(email_address, old_domain):
      old_domain_email_list.append(email_address)
      replaced_email = replace_domain(email_address, old_domain, new_domain)
      new_domain_email_list.append(replaced_email)
  #definiendo los headers del reporte
  email_key = ' ' + 'Email Address'
  email_index = user_data_list[0].index(email_key)
#
  for user in user_data_list[1:]:
    for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
      if user[email_index] == ' ' + old_domain:
        user[email_index] = ' ' + new_domain
  f.close()
  #escribiendo el reporte final
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()


main()






Full Name, Email Address
Blossom Gill, blossom@abc.edu
Hayes Delgado, nonummy@utnisia.com
Petra Jones, ac@abc.edu
Oleg Noel, noel@liberomauris.ca
Ahmed Miller, ahmed.miller@nequenonquam.co.uk
Macaulay Douglas, mdouglas@abc.edu
Aurora Grant, enim.non@abc.edu
Madison Mcintosh, mcintosh@nisiaenean.net
Montana Powell, montanap@semmagna.org
Rogan Robinson, rr.robinson@abc.edu
Simon Rivera, sri@abc.edu
Benedict Pacheco, bpacheco@abc.edu
Maisie Hendrix, mai.hendrix@abc.edu
Xaviera Gould, xlg@utnisia.net
Oren Rollins, oren@semmagna.com
Flavia Santiago, flavia@utnisia.net
Jackson Owens, jackowens@abc.edu
Britanni Humphrey, britanni@ut.net
Kirk Nixon, kirknixon@abc.edu
Bree Campbell, breee@utnisia.net
