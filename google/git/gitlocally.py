git commit -a #es un shortcut para git commit +add, 
#pero no funciona sobre new files que no se encuentran versionados, es decir solo sirve para
# aquellos files que estan bajo version de condigo y fueron modificados
git commit -a -m "mensaje "

#head  alias representa el current checked out snapshot del proyecto
#current snapshot es el ultimo commit del proyect
#head se usa mas para undo y rollbacks
#PATCH
# git log nos da informacion del autor, fecha de cambio y comentario
 git log -p # nos da el patch que fue creado 
#       #recordar que patch el file que se crea con los cambios incluidos del antiuo y nuevo file
 git show commit-id#nos da mas informacion del ultimo commit y el patch asociado
 git log --stat # muestra stats de los cmabios del commit como qu archivos se cambiaron, 
                # cuantas lineas fueron added o removed
# add al stagging area
 git diff # diferencias o cambios en un archivo contra la version previa equivalente a diff -u
# si el cambio incluye varios archivos muesra solo los del archivo especificado 
# en vez de los de todos los archivos
git add -p # nos agrega los archivos y permite esecificar si queremos stage o no, 
# es decir cambios que no que no queremos commit,
# para esos cambios que aún no estan completos pero ya debes hacer el commit
git diff --staged # me enseña los cambios added pero no commited
git rm # quitar el tracking del file, es decir es la accion contraria al add,
#borra el file del repository, mas no del proyecto local, solo lo desmarca
git mv # para renombrar files en el repository 
''' Undoing things
'''
 checkout # descartar cambios en un file que no quieres conservar en un stado stagged, 
        # es decir despues de add commit
git reset #  para deshacer un add, cuando se te fueron algunos files que no quieres 
        # incluir en el commit, por ejemplo si usaste git add *
git add * # agrega todos los files unstaged, al working tree o staged area
git reset HEAD file# Head es the current checked out snapshot, haciendole reset reversamos los cambios
        # al current snapshot, el file no se modifica, pero su estado ya no es add
git commit --amend# para esos casos en los que te equivocaste al hacer un commit, toma lo que
        # esta en el staging area y sobrescribe el ultimo commit.
        # suponiendo que al hacer el comnit omitiste hacer add sobre un file.
        # para corregir ese commit, haces 
        git add missingfile.txt
        git commit --amend - m "adding files"
'''rollback'''
# caso en los que el cambio ya está en snapshot
git revert commit # hace un commit que contiene el inverse de todos los cambios del ultimo commit
        # se basa en el HEAD, que contiene el inverso del ultimo commit
# apuntar a un commit especifico para tratar un error que proviene de varios commits anteriores
#  para ello usa el commit id
# para saber el id de un commit puedes hacer git log, el id se muestra despues de la palabra commit
git log -1 # el id se muetsra haseado en sha1
git show commit-id # no es necesario escribir el hash completo puedes escribir los primeros 5 digits
# git incluye el id del commit que se esta haciendo revert, como parte de los comments, 
# git revert commit genera un nuevo commitid para la accion 
'''
Branching and merging
'''
# branch un branch apunta a un commit en particular representando una linea independiente de 
#       desarrollo en un proyecto, el cimmit al que apunta representa el ultimo link en la 
#       cadena de desarrollo; es una rama que se crea a partir de un commit especifico y de ahí se 
#       parte un nuevo desarrollo 
# Master es el branch inicial de desarrollo  creado por git, cada nuevo branch es una nueva 
#       variación o implementacion del proyecto que desarolla una nueva versión o idea adicional al mismo
# existen varias opciones para trabajar un branch
#git branch 
#        list
#        create
#        delete
#        manipulate
git branch new-feature-branch # creando nuevo branch
git branch # lisando los branches
# el branch actual sobre el que se está trabajando se señala con un asterisco al inicio
git checkout # checkout en files sirve para cambiar un archivo a su estado previo
#checkout en branches, para cambiar de branch, lo que hace es actualizar el working three con el
# del branch seleccionado, incluyendo los archivos y el history
# checkout se debe entender como checkout al ultimo snapshot de un archivo o branch
git checkout new-feature-branch # me cambia al nuevo branch
git checkout -b new-branch# para crear nuevo branch y cambiar a el inmediatamente, en un solo comando

# ejemplo 
# crear un nuevo branch , un nuevo archvo, agregarlo y commit
git checkout -b nnew-branch-feature
atom new_file.py
git add free_memory.py
git commit -m "comentario para nuevo file en nuevo branch sample"
git log -2 # el -2 nos muestra las ultimas dos acciones
        # entonces veriamos promero el commit dentro de master y luego un commit dentro del 
        # nuevo branch, agregando el nuevo file
# Trabajando con branches
git status
 it branch -d # borrar branches que no necesitamos mas
# merging
# es usual hacer un nuevo feature en un nuevo branch
#merge combina el branch con el hystory
git merge # toma los snapshots independientes y el history de un git branch (el actual) y lo combina
git merge new-branch-feature # suponiendo que estamos en el master branch, 
        #  combina el nuevo feature con el master branch
        # git usa dos algoritmos para hacer el merge, fastforward  three-way merge
        # se tata de que los cambios hecho en cada nuevo merge, pasen a ser parte nuevamente del 
        # proyceto original, por lo tanto el merge entre dos branches se hara a partir del 
        # punto donde hubo la divergencia
#conflictos
#merge conflict es cuando se hacen cambios en el mismo punto en el mismo archivo, 
# es decir se edita la misma linea por dos autores
git merge --abort # devuelve los archivos al estado original antes del commit

Command	                    Explanation & Link
git branch	                Used to manage branches
git branch <name> 	        Creates the branch
git branch -d <name>	    Deletes the branch
git branch -D <name>	    Forcibly deletes the branch
git checkout <branch> 	    Switches to a branch.
git checkout -b <branch>	Creates a new branch and switches to it.
git merge <branch> 	        Merge joins branches together.
git merge --abort	        If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action.
git log --graph --oneline	This shows a summarized view of the commit history for a repo.