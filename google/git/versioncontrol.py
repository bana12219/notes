#version control
# nuevo empleo buscar, automation code:
# historical information
# configurations files
# Caso real: un script que valide que tienes todas las compus updated en firmware
# version control te permite hacer rollback en caso de emergencia
# Historical copies
# hacer una copia notificar y justificar el cambio
# Merges and differences
diff# para ver diferencias entre archivos, comparar archivos para detectar que lineas cambiaron
# diff revisa files o directories y te dice que lineas cambiaron
diff archivo1.py archivo2.py
#c change, a = added
diff -u # unified format
diff -u old_file.py newfile.py > change.diff
# el archivo resultante puede ser un diff_file o patch_file
# patch file toma el archivo generado por diff y se lo aplica al original
wdiff# highlits the words changed in files
patch # compara los archivos viejo y nuevo y aplica los cambios al original
# caso real revisar si una computadora tiene mucha carga y alarmar si la carga está muy alta
patch cpu_usage.py < cpu_usage.diff 
#patch te pone todos los cambios en el archivo, pero aun falta hacer el merge para ver cual es
# el efectivo
# antes de hacer la mezcla o bien si hay cambios de un colega sobre el mismo archivo,
# hacer una copia de respaldo (branch), 
cp archivoactual.py original.py
cp archivoactual.py fixed.py
# despues hacer los cambios necesarios para que funcione
#esto es como cuando bajas la version a local, haces copia, mezclas los cambios 
# y validas antes de subir los cambios
dif -u original.py fixed.py> current.diff
#ya que arreglaste los cambios, queda que el colega aplique el dif que resulto de tu mezcla
# con su local, esto mediante un patch

##Version control system
# nos permite saber quien hizo el cambio

diff
diff -u old_file.py newfile.py > change.diff
cp archivoactual.py original.py
cp archivoactual.py fixed.py
patch cpu_usage.py < cpu_usage.diff 

#caso real, coanfiguracion de un standby, en un version control system, guardas los 
# conig files para que cuando necesites poner en activo uno de los onhold 
# descargas la ultima version y ejecutas, así el DHCP server sigue respondiendo a la demanda
# 


diff # buscar las lineas que cambiaron entre dos archivos
    # variantes 
    # vimdiff para resaltar las lineas
    # dif pld new > diff  -este guarda las diferencias en otro file
patch # archivo que contiene las diferencias entre dos archivos, mas el contexto, es 
    #decir no solo te muestra las lineas con cambios, si no que integra los cambios 
    # en el antiguo file indicando que lineas cambian
# diff encuentra las lineas diferentes, patch pone las lineas deferentes en el old file
# indicando donde está el cambio 
patch oldfile < newdifffile.diff
    # lo que pasa es que diff encuentra que en linea 2 hay un cambio y patch pone la linea 2
    # dentro de oldfile 
commit # conjunto de modificaciones en uno o mas archivos versionados que son tratados como
    # un solo cambio, incluye tickets, bugs o issues fixed by the change
repository # conjunto de reursos compartidos por un grupo de usuarios
VCS # versionador de recursos permite hacer tracking

# GIT
# creado por linus torldvalsd
# primero le dices quien eres
git config --global user.email "yo@example"
git config --global user.name "yo"
# --global setea nuestras credenciales entodos los repos
git init #para nuevo repo en el current directory
         # se crea un dir .git, que almacena entreo otras cosas la info de cambios
         # cuando clonas el repo, se copia el git dir
git clone # para hacer una copia de uno existente
'''3 areas de un proyecto:
    working tree, git directory y stagging area
    snapshot
'''
#el area fuera del git directory es working tree
#working tree es la current version del proyecto es como unsandbox, contiene los archivos 
# versionados y los que aun no estan bajo control de versiones
#git directory es el directorio que contiene toda la config del repo
# working tree solo contiene la current version
'''
los archivos pueden ser tracked o untracked, que no son parte del snapshot
    el snapshot se produce cada que se hace un comit, que es como una 
    foto del estado del proyecto,los snapshot, hacen el history y se guardan en 
    working directory
Los archivos tracked tienen 3 estados, modified, stagged o commited
    modified es con cambios, estos pueden ser adding, modifiying o 
            deleting, solo son detectados por el git y cambiará de estado 
            solo hasta que se haga el add al staging area
    stagged los archivos que fueron added, entran a este estado que es ready for commit
            y serán parte del siguiente snapshot en history en git directory 
            cuado se haga el commit
'''
#ya que tienes configurado el git,
# 1 creas o copias tu primer archivo
cp ../scripts/file.py
#, este archivo no esta versionado, es decir esta en la carpeta pero no es parte del repo
# 2 agregas el archivo al repo
git add file.py
# ahora el archivo se agrego a la staging area, tambien conocida como index
# es un archivo manejado por git que va registrando que archivos y que cambios se van en el
# siguiente commit 
git status # nos da info del working tree y los cambios pendeintes
git commit -m "comantarios razon de cambio" #guarda los cambios
# loas archivos pueden tener 3 estados: modified, staged, commited
    #los archivos modificatos pasan a staged cuando les damos add
    # es decir están lostos para ser cimmited
    # para ser parte del siguiente snapshot
    # staged significa marcados para hacer tracking
    # committed es que ya son parte del repo
    ''' si no se hace git add, los cambios quedan marcados como not staged '''
# los cambios pueden estar Adding, modifying o deleting

#Git workflow
# si creamos un nuevo repo, como git config --global, 
# las credenciales están seteadas por defecto
# se pueden setear diferentes credenciales para cuando quieres subir a un repo publico 
git init
#git commit sin parametros lanza un editor
#nota importante esto sigue siendo git directory local, falta hacer push
#git push -u origin master

'''
Messages
'''
# incluir info importante, como ticket que atiende, 
# short summary del commit, linea blanca, descripcion detallada del cambio y 
# porque fue necesario, que resuelve

'''
provide a good commit messafe example # aprox 50 caracteres o menos

Parrafo de aproximadamente 72 caracteres de longitud, que describe detalles
sobre el cambio como que resuelve ...

se pueden agregar más parrafos si es necesario, links o recursos que sean últiles
'''
git log # muestra los messages

'''
Commit message style guide for Git

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
