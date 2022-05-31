# manejar hilos que nunca se cierran correctmente causa memory crashes
# estados que  no se anticipan como sw funcionando mal, fallas en hw, 
# disecciona y aisla el problema 
# comienza por los errores más sencillos
# encuentra el scope
# si tratas de reproducir el problema en otra computadorea,  no es el programa si no la máquina
#           encontraste el scope
# intenta con otro usuario, si no se repite, entonces es un problema con un usuario, 
#       en una máquina en un proceso, intenta con otro programa para ver si tambien falla
# 


"""LOGS"""
Internal server error  500
ssh webserver
# /var/logs    en linux
# console app en macos
# event viwer en windows
# errores comunes
# permission deneid
# conection refused
# not such file
# para correr el log en modo debug:
    strace mas comando en linux
    dtruss  en macos
    process monitor en windows 

# wrapper para resolver probleas de compatibilidad entre scopes
# watch dog para sber cuando un programa está corriendo y cuendo no

"""
PREGUNTAS COMUNES 
que intentas hacer?
que pasos seguiste?
que esperabas que ocurriera?
cual es la salida actual?

"""
#solving server internal error
netstat -nlp | grep :80 # n para dir ip en vez de nombres de dominio, 
                        #l los sockets que escuchan la conecction
                        #p process id
                        #| grep :80 para filtrar solo los de puerto 80

sudo service service _name reload



#deugging techniques

"""
code crash
     una razon común para que una aplicaicon falle es la falta o falla de meoria, por eso es impotante entender como funciona
     cada proceso tiene asignada una porcion de memoria pero puede acceder a parte de la memoria fuera de la que tienen asignada
      
      
    ***ACCESING INVELID MEMORY    signifia que el proceso intenta acceder a una porcion de memoria del sistema que no 
        le ha sido asignada 
    *** SEGMENTATION FAULT / GENERAL PROTECTION FAULT  es cuando el proceso está intentando escribir en una porción 
        que no le ha sido asignada, pasa más con programas escritos en lenguajes tipo c o c+ donde la gestión e memoria 
        queda a cargo del developer. Un programa en c escribe en una ubicacion fuera del segmento que le fue asignado 
        y cuando la applicaicon intenta leerla crashea, estos erores son tipo: 
                * out of range
                * variable no initialized
                * index out of bound exceptions
        la manera de saber que está pasando es implementar una buena técnica de debuging, 
        algunas  distribuciones como debian y ubuntu usan debugging symbols como nombres de variables etc, 
        para la hora de hacer debugging, estos vienen en paquetes separados así puedes descargarlos para 
        usarlos en applicaciones como segfaulting
        esto nos permite al momento de que un app crashea saber que es lo que falla dentro del
        la llamada a la funcio o libreria adicional a las herramientas de la aplicaión
         microsoft genera estos symbolos en un PDB file separado
    *** Undefined Behavior, es cuando el prorma aestá haciendo algo que no es válido en el lenguaje de programación.
        esto puede deberse a un cambio de compilador y como cada so asigna memoria a los procesos
        incluso la versi{on de las librerías en uso, un programa que corre bien 
        en windows podría causar problemas al ser cambiado a linux
        VALGRIND me dice si el código está haciendo invaido incluso si no crashea, me dice
        si no inicialia variables etc para linux y amacos
         doctor os
    una vez identificas el problema, puedes componerlo o bien dejarlo que lo compongan en 
    versiones siguientes. si es un hotfix, puedes arreglarlo o llamar 
    al developer para que lo solucione


"""

"""
     Unhandled errors o exceptions
     los programas de alto nivel como java o python manejan mejor la memoria
     aun así existen errores que pueden ser logicosy deben ser manejados correctamente
     IndexError
     DiviionByZero
     estos errores pueden ocurrir dado que se asumen condiciones como 
     presentes, por ejemplo, que un recurso siempre va a estar disponible

     Traceback ; muestra la linea de las funcoines que se ejecutaban cuando 
     ocurrio la exception

     Para hacer debug de éste tipo de exceptions existen tecnicas como 
     
     ***printf debbuging que es mostrar mensajes que me vayan diciendo que va fallando
        lo mejor es hacerlo de manera que sea facil habilitar y desabilitar  la impresión de éstos
        mensajes paraello se usan logging modules en algunos lenguajes.
         se puede especificar el nivel de debuggeo  como
         logg, debug, error
        la idea es cachar el error y dar un mensaje significativo sobre la razon
"""


"""
Corefiles
    es un archivo que guarda toda la informacion relacionada co un crash
    con el crash para que posteriormente pueda ser debuggeado
    es una especie de snapshot del crash cuando ocurre, para ser 
    analizado posteriormente.
    para generar éstos corefiles, se le debe decir al SO que queremos que sean generados
"""
ulimit -c unlimited
./example
"""
    ulimit -c le dice al SO que queremos que esos corefiles sean generados
    unlimited, le dice que no importa el tamaño de esos corefiles 
    el archivo se genera en donde fue ejecutado
"""
"""
    gdb me ayuda a interpretar el corefile 
    backtrace para interpretar la linea de la traza
    gdb es un debuger
"""
"""
PDB3 para debugear python

"""

"""
Postmortems, documentan el incidente, en el se explone, que paso, que lo causó, que impacto tuvo, como se diagnostico
 como se arregló (short term)y como evito que se repita (long term)

"""

"""
Memory Leak
    La memria desocupada no se libera, garbage collector
    para ello monitorear la cantidad de memoria que consumen las funciones
"""

"""
Memory profilers
Valgrind 
"""

"""
Automatizacion de monitoreo de recursos
"""
#Network se refiere a la elocidad de respuesta
"""
Se debe cuidar la latencia y ancho de banda
"""
iftop # monitorear el ancho de banda
"""
Traffic Shapping 
     Me permite saber que app está consumiendo el ancho de banda
     marca los packetes enviados por prioridades para evitar que una app consuma todo

"""
uxterm 
"""
Scroll buffer: me permite ver lo que ejecuté y si output
"""


"""
No dejes pendientes, porque creas Deuda Tecnica, que es el trabajo 
que va quedando pendiente cuando optas por una solucion rapida en vez de 
una duradera