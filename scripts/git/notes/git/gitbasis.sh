#configuracion inicial de Git
# una vez instalado
#agrega el username al git config file 
#--global le indica que lo use para todos los repositorios en los que se conecte
git config --global user.name "uname"
#git config email
git config --global user.email "umail@mail.com"

git init    #- inicia o convierte la carpeta en un repositorio 
            # crea un folder .git dentro del current directory 
            # para empezar a hacer track de los files contenidos
git clone url # para hacer una copia de un repositorio existente 
git status  # muestra el estado del reposiorio para saber si hay cambios o no
            #cualquier cambio en el repo se registra
git add file.txt # agrega el archivo para que se comience a hacer tracking 
git add .    # agrega todos los archivos del current directory
git commit -m "comantarios razon de cambio" #guarda los cambios
            # los archivos pueden tener 3 estados: modified, staged, commited
            # los archivos modificatos pasan a staged cuando les damos add y
            # están lostos para ser commited (parte del siguiente snapshot)
            # staged significa marcados para hacer tracking
            # committed es que ya son parte del repo es decir en git directory


"
Commit message style guide for Git

The first line of a commit message serves as a summary.  When displayed
on the web, it's often styled as a heading, and in emails, it's
typically used as the subject.  As such, you should capitalize it and
omit any trailing punctuation.  Aim for about 50 characters, give or
take, otherwise it may be painfully truncated in some contexts.  Write
it, along with the rest of your message, in the imperative tense: 'Fix
bug' and not 'Fixed bug' or 'Fixes bug'.  Consistent wording makes it
easier to mentally process a list of commits.

Oftentimes a subject by itself is sufficient.  When it's not, add a
blank line (this is important) followed by one or more paragraphs hard
wrapped to 72 characters.  Git is strongly opinionated that the author
is responsible for line breaks; if you omit them, command line tooling
will show it as one extremely long unwrapped line.  Fortunately, most
text editors are capable of automating this.

:q
"
git log # muestra los messages
git commit -a #es un shortcut para git commit +add, 
#pero no funciona sobre new files que no se encuentran versionados, es decir solo sirve para
# aquellos files que estan bajo version de condigo y fueron modificados
git commit -a -m "mensaje "
git commit –v  # agrega el resultado del diff al mensaje del commit 
git diff   #ver los cambios en un archivo 

--- cambios remove 

+++cambios add 

git diff  --staged # ver los cambios que no han sido commited, solo son parte de staging area 
.gitignore   # git ignore files, define que archivos no deben subirse nunca
             #     *      0 + veces 
             # pattern/   solo foldernames 
             # /pattern   en el mismo directorio que eo .gtiignore 
             # !          excenciones, los que no contengan el pattern, por ejemplo !TODO quedan excentos 
             #Documentation /**/*.html  no va a subir todos los html que esten en algun subfolder de documentation 
             # para comentarios 
https://github.com/github/gitignore contiene mas ejemplos
# patch file toma el archivo generado por diff y se lo aplica al original
wdiff# highlits the words changed in files
patch # compara los archivos viejo y nuevo y aplica los cambios al original
# caso real revisar si una computadora tiene mucha carga y alarmar si la carga está muy alta
patch cpu_usage.py < cpu_usage.diff 
#patch te pone todos los cambios en el archivo, pero aun falta hacer el merge para ver cual es
# el efectivo

    Git log --2  muetsra solo los ultimos 2 commits 

    Git log --p muestra el patch hecho 

    Git log  --pretty = oline , full, fuller formato del output 

    Git log --since/from/until “2 months” 

    Git log --graph 


Undoing Mistakes
 git commit --ammend #, abre el ultimo commit para hacer correcciones 
                     # y reemplaza el commit

    Git log # para obtener el id de commit que se debe reersar 

    Git revert  commitid  

    Git remote add new-remote http://new-remote-example 

    Git fetch te permite obtener la info de un repo remoto para saber que cambios hay 

    Git merge origin/master incluye los cambios remotos en origin a la rama master local 

    Updating 3009aed... 38966cd      significa que esta actualizando de un commit a un nuevo commit 

    Git add changed.file      # una vez agregamos los cambios sigue hacer add nuevamente para pasar a staging 

    Git commit  # para pasar a git directory 

    Git push origin master     #hacer push de origin a la rama master 
    Git fetch                  #de                 nsde remote mantiene actualizado al ultimo commit 
    git pull                   # actualiza el local

    TAGGING

    Git tag – lista los tags del repo 

    Git tag – list <glob> muestra los tags que hacen match con el pattern 

    Git fetch                               #desde remote mantiene actualizado al ultimo commit 

    Git tag “1.1.1” 

    Git show “1.1.1” 

    Git tag –a "1.1.1"  -m “ejemplo de tag anotado” #-a de anotado 

    Git push origin 1.1.1.  # hacer push del tag 

    Git push origin –tags 

    #BRANCHING 
    Git branch new-branch-name  # crea un nuevo branch 

    Git checkout new-branch-name #mueve el head al nuevo branch, para empezar a trabajar en el 

    1231  git checkout -b bugfix
    #Merging branches
    #crando el master
  mkdir originalbranch
  cd originalbranch/
  git init
  echo "este es el archivo original de prueba" > readmefile.txt
  git add .
  git commit -m "commit inicial, para que master brancho no este vacia"
    #creando un feature branche para hacer cambios
  git checkout -b feature-branch-name
  git branch
  nano readmefile.txt 
  git status
  git add readmefile.txt 
  git commit -m "despues de agregar cambios al file desde el segundo branch, hay que hacer add y commit, para agregar el cambio que ya quedo listo"
    # creando un bugfix branch
  git checkout -b bugfix
  git branch
  nano readmefile.txt 
  git status

  git add readmefile.txt 
  git commit -m "añadiendo el cambio de bugfix"
  git checkout master
  #comenzando los merge
  git merge bugfix
  #borrando branch
  git branch -d bugfix
  #regresando a master para el ultimo merge
  git checkout master
  #comenzando los merge
  git merge bugfix
  #borrando branch
  git branch -d bugfix

  
                                                                    
#remote branches
git push <remote> <branch-name>

"""rebasing changes
para hacer merge a un branch hacia el master hay dos opciones 
git merge 
git rebase, rebasing es cambiar la base del comit usada ara nuestro branch
"""
git rebase ''' conforme vas haciendo commits se van haciendo checkpoits  o snapshots de tu desarrollo
            entonces cuando haces tu branch, se hace a partir del checkpoint o snapshot del proyecto en ese momento
            con el tiempo el master va evolucionando y teniendo mas checkpoints pero el 
            branch sigue apuntando al pasado. 
            git rebase te permite apuntar al branch actual, 
            esto te permite a ti: 
                *que tu branch tenga la version actual del master y así no caer en la tendencia de 
                que ambas versiones evolucionen tanto que se vuelvan productos diferentes
                * que git haga fastforward merge y keep history linear más facil y estructurado
            '''
git rebase basebranch # la sintaxis es git rebase, mas el basebranch al que queremos apuntar


'''
Commit message style guide for Git  #subject

The first line of a commit message serves as a summary.  When displayed
on the web, it's often styled as a heading, and in emails, it's
typically used as the subject.  As such, you should capitalize it and
omit any trailing punctuation.  Aim for about 50 characters, give or
take, otherwise it may be painfully truncated in some contexts.  Write
it, along with the rest of your message, in the imperative tense: "Fix
bug" and not "Fixed bug" or "Fixes bug".  Consistent wording makes it
easier to mentally process a list of commits.

Oftentimes a subject by itself is sufficient.  When it's not, add a
blank line (this is important) followed by one or more paragraphs hard
wrapped to 72 characters.  Git is strongly opinionated that the author
is responsible for line breaks; if you omit them, command line tooling
will show it as one extremely long unwrapped line.  Fortunately, most
text editors are capable of automating this.

:q
'''
