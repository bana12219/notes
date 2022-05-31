# lentitud de respuesta
#puede deberse a un tema de memoria, ram disco cpu
# ver que recursos es el que se está agotando

top # ver que procesos consumen más recursos
iotop # disk io usage
iftop # 

Macos ACtivity monitor
windows resource monitor / performance monitor
# tomar en cuenta dnde se está tardando
# al devolver los datos
#   si son datos de una funcion es el cpu
#   si son datos en una app ya corriendo puede ser en ram
#   datos de archivo, están en disco o en la red
# ara lecturas sobre red constantes hacer respaldo en  disco o cpu, es decir una cache
# web proxy es una tipo de cache de sitios, imagenes o videos
# DNS implementan una cache local para almacenar las direcciones ip
# swap espacio en disco para alojar info no tan recurrente evitando consumir demasiada ram
# memory leak, la memoria que no se necesita, no ha sido entregada
# si se tarda al arrancar quita programas al arranque

#slow web server

ab -n 500 site.com/ # herrameinta de apache para medir la transmision de peticiones  ( 500) al sitio
nice / renice # cambiar la prioridad de los procesos
pidof # para saber el process id del proceso  

for pid in $(pidof ffmepg); do renice 19 $pid; done # bajar la prioridad de los ffmpeg que estan haciendo lento el server
ps aux | less# ver los procesos que consumen y ubicar el que nos afecta
locate static/001.webm#ubicar el proceso
# entrar a la ubicacion a ver que hay
cd /srv/videos/satic/
ls
#ver que contiene la lista de archivos
grep ffmpeg *
# me despliega en que archivos se menciona ffmpeg

killall -STOP ffmpeg # detiene el proceso
# levantar uno a uno
for pid in $(pidof ffmepg); do while kill -CONT $pid; do sleep 1; done; done
# slow code
# escribir código fácil
#prifiler es una herramienta que mide los recursos qie el código está usando
cprofile # para python
gprof # java

# crear caches para el procesameinto de archivos de 
# manera que hacer el parse de un file sea mas rápido
# esta cache se calcula cada cuando debe ser refrescada en base a características como:
#       es informacion que se recopila diario?
#       el consumo de recursos
#       la cache se asa en archivos?
#             

time ./script.py "parametros" # me dice cuanto tiempo tarda en ejecutarse el comando
# real me da el tiempo que tarda en ejecutarse el comando
# user el tiempo que tarda la operacion en ejecutarse en el userspace
# test el tiempo gastado en hacer las operaciones de sistema
pprofile # me ayuda para medir el performance de un script en python
keycachegrid # gui para 
# clean code, best practices, algorithms, refactoring, operaciones paralelas, concurrencia
# multithreading, prograacion asíncrona
# CPU bound
executor# ejecuta cargas de trabajo en threads
Futures module # provee executores uno para threads y otro para processes
