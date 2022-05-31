#paso 1 entender el problema
#generar un reporte que informa que usuarios se conectan a que servidores.
#el imput es una lista de eventos que son registrados en un server
#la clase evento contiene la fecha, usuario, maquina, tipo de evento 
# el output puede ser nombre de server, y la lista de usuarios por server por pag
# el otro puede ser el nombre de server: lista de usuarios separados por coma
#paso2 research, ver que recursos tenemos a la mano
# los usuarios pueden estar logged in y logged out, y nos estan pidiendo solo current logged
# se deben analizar los eventos e orden cronológico
#   1.Sortear la lista por fecha
            #numbers.sort() ordena ascendente
            #sorted(names) ordena alfabetico
            #ordenar por atributo de string, nombre
            #sorted(names, key=len)
            #python tiene 2 formas de organizar: sort y sorted, 
    #tomar del evento la fecha creando un metodo get_event_date
#   2.Estrategia: Tomar los eventos por fecha, usuario, maquina/server, tipo evento [logged in, logged out]
            #usar un set para ir almacenando loggins y loggouts (add/pop) del usuario por máquina,
            #faltaría asociarlo con el server
            #usar un dictionary key:server, value: set user logged
            #el script va a ir generando el reporte a partir de las entradas
            #dos funciones, una que genera el dict y otra que lo imprime
#   3.Planning: procesar eventos, ordenarlos cronológica, guardar los eventos en un dictionaryde sets
    #generar dos funciones, una guardar el dictionary y otra print

################
#Code Beginning
################
#defining the helper function we'll use to sort the lista
def get_event_date(event):
    """Esta función se usa como parámetro para la funcion de ordenacion de la lista"""
    return event.date

def current_users(events):
    """Ordenacion de eventos por orden cronológico"""
    events.sort(key=get_event_date)
    #dictionay que almacena por servidor el set de eventos de usuarios loggeados
    machines={}
    #iterar los eventos
    for event in events:
        #ver si la maquina está en el dict, si no agregarla
        if event.machine not in machines:
            machines[event.machine]= set()
        # hacer in y out segun la accion del usuario
        #nota aqui puedes mejorar la logica y los datos guardados
        if event.type=="login":
            machines[event.machine].add(event.user)
        elif event.type=="logout":
            machines[event.machine].remove(event.user) 
    return machines

def generate_report(machines):
    """genera el reporte a partir de los datos procesados de loggeo de usuarios"""
    for machine,users in machines.items():
        #filtrar solo las maquinas que tengan usuarios logeados, no imprimir las que no
        if len(users)>0:
            user_list= ", ".join(users)
            print("{ma}: {usr}".format(ma=machine,usr=user_list))


class Event:
    def __init__(self,event_date,event_type,machine_name,user):
        self.date=event_date
        self.type=event_type
        self.machine=machine_name
        self.user=user



lista= [2,3,4,5]
dicti={}
dicti.update({1:lista})
