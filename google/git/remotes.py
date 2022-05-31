#remotes
# distributed systems, cada developer tiene su copia localdel repo
#github tiene extrafeatures como bug tracking, wikis, task management
#otros son bitbucket, gitlab
#clonando el repositorio remoto
git clone  https://github.com/
#cd repo
#ls
# editar el archivo readme para subir el cambio
git commit -a -m "aregando readme a stagging area" # hacere add para agregarlo al stagging area
# enviar los cambios al repositorio remoto
git push # todos los cambios del snapshot y enviarlos al repo remoto
#pide username y pasword
# para no estar poniendo las credenciales se hace un ssh para que github reconozca la compu
# otra opcikon es credential helper
# para el credential helper
git config --global credential.helper cache # se vuelven a meter las 
                #credenciales y guarda la sesion por 15 min
git pull # para bajar los cambios remotos al repo local

""" remote repository"""
# tener un repositorio remoto te permite colaborar con equipos distribuidos, 
# cada integrante sube su codigo para compartirlo d¿con el resto, igualmente se pueden tener branches
# y git te puede ir informando cuando sea tiempo de descargar o actualizar tu version
# ara descagar los cambios haces pull, es bueno hacerlo periodicamente para evitar 
# conflictos con tus cambios locales
# si tratas de hacer un push (suir cambios) el procedimeitno: 
#       pull para bajar cambios,
#       merge para resolver conflictos con tu version local
#       push para subir us cambios y que estén disponibles para el equipo
# al trabajar con remote se agregan nuevas faces 
#       mdify ----
#       stage     |- del ciclo local
#       commit----
#       fetch  (pull)cambios del repo remoto
#       merge manual de los cambios remotos y locales
#       push de los cambios al repo remoto
# formas de coneccion soportadas
#       http para accesso de solo lectura, es decir permite clonar pero no hacer push
#       https provee al gual que ssh metodos de autenticacion de usuario y por ende hacer push
#       ssh
git clone # hacer una copia local del repositorio remoto, 
          # git le pone por defecto el nombre original del repo remoto
git remote -v # para ver la configuracion original del repo, 
          # me da las url asociadas con el repo remoto, voy a ver 2 una para fetch y otra para push
          # las url pueden ser las mismas o puedes tener 
          # http para fetch y https / ssh para push
# los remotos tienen un nombre asignado, por defecto su nombre es origin, para poder hacer track
# a mas de un remoto en el mismo git, puesto que podemos colaborar a mas de un equipo 
git remote show origin # me da la info completa del repositorio, como branches ...
# remote branches son usados por git para mantener una copia de los datos guardados en el repo remoto
git branch -r # me da la info del repo remoto que estamos usando o siguiendo
git status # sirve tambien para los repos remotos, ademas de la info normal, me dice por ejemplo si 
           # mi version está actualizada
'''
fetching new changes (hay un cambio remoto)
primero hacer un 
'''
git remote show origin # para saber si nuestra version local está desactualizada de la remota
git fetch # para sincronizar los datos locales y remotos (contrastar la informacion y detectar los cambios)
git log origin/master # para ver el log de cambios que se han hecho 
            # ahí vemos que el remoto apunta a una nueva version de un commit qu alguien hizo
            # el local apunta a la version anterior del master
git status # para confirmar que hay cambios 
git merge origin/master # para hacer el merge de nuestro repo con el remoto
#fetch solo te permite ver los cambios que hubieron
# merge te permite integrar los cambios al branch local
'''
updating local repository
'''
git pull# actualiza el repo local descargando los cambios remotos
        # el outpu dice cuantos archivos se actualizan y cuantos cambios hay
        # pull incluye el fetch y merge
        # primero git hace fetch y despues merge
git log -p -1 # para ver los cambios del pull
        # el pull nos dice incluso si hay un nuevo branch
git checkout experimental # para cambiar al branch experimental, 
                        # el contenido se copia en el working tree
git remote update # para hacer pull sin merge automatico al local branch

'''
oull hace merge automatico
fetch descarga remote updates como objetos y referencias de un remote branch
push para enviar los cambios
'''

'''
pusll-merge-push workflow
 que pasa si al enviar el remote tiene cambios ya ?

'''
"""1 flujo normal sin cambios remotos"""
git add -p # para ver los cambios que hicimos y aceptarlos
y # para aceptar y hacer staging
git commit -m "rename parameters " # ara subirlos en repo local
git push # para subirlos al remoto
"""2 flujo con cambios en remoto"""
git add -p # para ver los cambios que hicimos y aceptarlos
y # para aceptar y hacer staging
git commit -m "rename parameters " # ara subirlos en repo local
# si tratamos de subir aqui va a fallar por que hay cambios remotos, debemos 
# primero sincronzar el repo local con el remoto
git pull# descarga pero al hacer el merge encuentra un conflicto 
        # porque se modiicó el mismo archivo en las mismas lineas 
git log --graph --online --all# nos muestra de manera semi grafica los commits 
                    #y las posiciones en el arbol
# si se mueatran cambios en el tree master branch, oigin/ master branch y experimental branch
#   es hora de hacer un tree-way merge, esto es porque nuestro cambio afecta a el 
#   master, y a las dos ramas actuales que dependen del master
git log -p origin/master # revisar antes del merge que cambios hizo alguien mas en el archivo
'''aqui haces los cambios correspondientes para resolver el conflicto y repites los pasos'''
git add -p # para ver los cambios que hicimos y aceptarlos
y # para aceptar y hacer staging
git commit -m "integrate both changes rename parameters and change conditionals" # ara subirlos 
            #en repo local
git push


#nota se recomienda indicar el nombre de la variables a la que se envia el dat para tener
#codig mas claro
def check_disk (disk, mingb,min_percent):
    pass

check_disk(disk="/", mingb=2,min_percent=10)


""" pushin remote branches"""
#una best practices es hacer un nuevo branch para cada nuevo feature, 
git cheackout -b refactor# os permite hacer cambios entre branches, creando el branch
# atom  para hacer el cambio
git commit -a -m "Nuevo feature en branch nuevo "

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

git log --graph --online
#se muestra el merge de los branches
# ahora repetir para hacer merge entree el branch (refactor) y master
git checkout master
git merge refactor
git push --delete origin refactor
git branch -d refactor
git push
'''pull request sample
hacemos un cambio a un archivo py para agregar una nueva funcion, entonces debemos subir el cambio
'''
git commit -a -m 'Add a simple netwok connectivity check' # primero en local
#revisar si alguien mas no ha subido cambios en  remoto
    # se puede hacer en automatico con git pull, que hace un merge automatico si hace falta
    # o manual, git fetch busca en origin/ master por defecto
git fetch
# hacemos rebase para unir nuestro branch con master
git rebase origin/master
#si hay conflicto lo arregalmos y hacemos commit, rebase nuevamente
git log --graph --online #para ver el merge

"""BEST PRACTICES COLABORATION"""
# siempre synchronize el branchantes de empezar a rabajar
# trata de no hacer cambios muy largos que modifiquen muchas cosas lo mas pequeños selfcontained
# cambios muy signifiativos hacerlos en unbranch separado
# regurarly merge changes en el master desde el feature branch
# tener la ultima version del project en el master y la version estable en uno separado
# No rebase en repos remotos; rebase es util pero se debe usar con precaución 
#           porque sobrescribe el history es recomendable solo en local
# Hacer buenos comentarios 




