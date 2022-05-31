git remote -v # version de repo al que estas conectado
#origin	https://github.com/anab3z/it-cert-automation-practice.git (fetch)
#origin	https://github.com/anab3z/it-cert-automation-practice.git (push)

git remote add upstream https://github.com/anab3z/it-cert-automation-practice.git
# crear branch
git branch improve-username-behavior
# cambiar al branch
git checkout improve-username-behavior
cd Course3/Lab4
# modificar Validations.py
#This script should validate usernames if they start with an letter only.
#!/usr/bin/env python3


git clone https://github.com/anab3z/it-cert-automation-practice.git
 1187  cd it-cert-automation-practice
 1189  git remote add upstream https://github.com/anab3z/it-cert-automation-practice.git
 1191  git remote -v
 1192  git branch improve-username-behavior
 1193  git checkout improve-username-behavior
 1194  ls
 1195  cd Course3/Lab4
 1196  ls
 1197  cd Course3/Lab4
 1198  nano validations.py


import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    # debe comenzar con letra
    # solo pueden ser letras numeros o ._
   
    pattern=r'^[a-zA-Z][a-zA-Z0-9._]*$'
    if not re.match(pattern, username):
        return False
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    #if not re.match('^[a-z0-9._]*$', username):
    #    return False
    # Usernames can't begin with a number
    #if username[0].isnumeric():
    #    return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False





git config --global user.email "ing.annab3z@gmail.com"
git config --global user.name "anab3z"
