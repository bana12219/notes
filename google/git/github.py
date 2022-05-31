"""Fork es crear una copia dl repositorio remoto que pertenezca a l ususario
    donde puedas subir cambios y posteriormente pasarlos al repo original
"""
'''El workflow para trabajar con repos hosted en git hub es primero hacer un fork o copia 
trabajar sobre la copia y hacer los commits en nuestra copia, posteriormente hacer un 
pull request '''
'''
pull request es una serie de commits que envias al propietario del repo para incorporar 
tus cambios al arbol
'''
#primero hacer fork en github para crear nuestra copia del repo en nuestra cuenta
git clone https://github.com/anab3z/validations.git # descargar esa copia
 1009  cd validations # entrar a ella
 1012  git log # ver el history
 1013  git checkout -b add-readme # hacer un nuevo branch para trabajar y cambiar a el
 # crear README.md md es de markdown
''' request in github'''
'''FORKING es crear una copia del repositorio que ertenezca a nuestro usuario
para ahí trabajar
nos permite subir cambios incluso cuando no podamos subir cambios a otro repo
( es tu propia version del repositorio remoto)
'''
'''el flujo adecuado  es:
1 crear tu fork para trabajar,(la copia es del proyecto a tu usuario)
2 clonarlo para trabajar en local
3 hacer el merge de tu fork con el repo original
4 hacer pull request

'''
''' Pull request es un commit o serie de commits que envías al dueño de 
el repositorio para que incorpore los cambios en el árbol
'''
#1. hacer el fork del repo de alguien mas desde interfaz web
#2. clonarlo en local
git clone https://github.com/anab3z/rearrange.git
#3. hacer el branch nuevo que se llame addreadme
git checkout -b add-readme
    # hacer un cambio, agregando un readme
    nano README.md
#4. add
git add README.md
#5. commit
git commit -m "agregando readme"
#6. push al branch correspondiente
git push -u origin add-readme
    # desde la interfaz hacer el pull request donde indica si hacer el merge no tiene comflictos

'''actualizar un pull request, para hacer una mejora'''
    # hacer un cambio, agregando un readme
    nano README.md

'''Squashing changes'''
 '''rebaese -i  dar mas info sobre el commit
 '''
git rebase -i
git push -f

#issue tracker , 
#bug tracker
#comunication channesl
#style guides


#CI build y test per cambio git lab lo pfrece, github necesita travis para ésto
#CD despliege continuo Jenkins
#pipelines especifican los pasos necesarios para obtener un resultado
# artefactos archivos generados como parte de un pipeline
    # llaves ssh, api tokens
    #cosideraciones
    #   1. asegurate de las entidades autorizadas para los servidores de test 
    #       no son las mismas entidades autorizadas para el despliegue a produccion
    #   2. plan para recuperacion de aceso en caso de que el pipeline se vea comprometido