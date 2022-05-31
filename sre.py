incorporar aspectos de software engineering  y aplicarlas a infraestructura y problemas de operación
production rediness review:
design
build/ test
release
Operate
#####################################
engagement
analisis
improvements y refactoring
training
onboarding
Improvement


### 
reliebility, se necesita el 100% realmente, porque esto sale más caro
los usuarios pueden soportar una mala experiencia de usuario si eso te permite ahorrar
el 100% de SLAs en clous Saas, iaas o paas,  si existiera se garantiza cuando el SLA no se conoce
un single layer no soporta el 100% 
no depende de una ola layery se pueden dar fallas en cascada, por ejemplo si tienes el 100% asegurado en la 
DB, tienes tambien otros factores como 

SLA service level agreement, el servicio que el ofrece el proveedor de servicio, 
SLO service level objective, la calidad de servicio que esperas darle al usuario
SLI service level indicator, la forma de medir el SLO


error budget

es el complemento del SLO
front     90 -10
back      97 -3
analytics 99 -1 

dealing with failure
Infraestructure - resilience: network clustering, storage, and security
application
people
Mind set
Se trata de corregir la mentalidad de invertir solo hasta que las cosas se rompen, 
es decir es una cultura de la previsión y optimización
ver que fallo y corregirlo

Aceptar el error 
    medir, SLI, SLO
    postmortems
Implementar cambios graduales
    pasos pequeños para ser rápido y reducir el costo de error
tooling y automatizacion

SRE resuelve con software

SRE Job description
    Systems o Software experience
    Infraestructure automation expertise
    Problem solving
    verbal and written comunication
Google
SRE es una disciplina qie incorpora aspectos de SW engineering y los aplica 
a infraestructura y operaciones, para crear systemas de software escalables y confiables

Minimum qualifications:

    Experiencia en Computer Science
    Experiencia en uno o varios:
        Java, Python, Go, Perl, Ruby
    Experiencia con Unix/Linux OS internals y administration (filesystems, inodes y systems calls) o 
    redes(tcp, routing, network, topologies, hardware, SDN)
    Experiencia analizando Troubleshooting systems


AWS

Reliability es key de well architected framewrok, que implica la habilidad de un systema 
para recuperarse de infraestructure o service disruptions, adquirir recursos de manera dinámica 
para responder a la demada, mitigar disruptions como misconfigurations o issues de red 

Aceptar error como natural:
    Probar recovery procedures
    recuperacion automatica
    escalado horizontal

mide todo
cambios graduales y automatizacion
reducir los silos en la organización


Ganando resiliencia y reliability en AWS

Account - costos , politicas, gobierno, organizations
Region - ubicacion geografica
Edge locations
AZ - datacenters físicos

linking services
AWS Managed services

Network resilience - 
   direct connect para la VPC ejemplo resiliencia del datacenter corporativo en la nube
Subnets - ELB
Resiliencia across regions, AZ, AWS managed services

Resiliencia entre cuentas, peering- transient hubs

health checking para monitorear la resiliencia

Global accelerators
Disaster recovery para  multiregion y multi-availability zone resilience
Global accelerators derecciona el tráfico a endpoints optimos  sobre la red global de AWS
logra  60% de better performance

 elb por regions
 reducir delays en la red que hagan que el servicio no se use

SLA- 
service commitment, 5-9, 2-9, succesful requests
definitios, como se va a medirservice credits
exclusions, que circunstancias no se cubren en las clausulas del contrato

Amazon global services s3
durable object storage amazon se compromete de lo contrario eres candidato a creditos de servicio
Amazon Service S3  
    de 0 - terabytes para resizing
    S3 standard, standard IA, One Zone ia, y glacier diseñados para 9 9's al año
    s3 standar diseñado para 2 9's 
    de 99.9 a 99.0 de reliabiliti = 10 % de service credits (error budget)
    menos de 99.0 a 95.0= 25% service credits
    menos de 95.0= 100% de service credits
    exclusions. causas ajenas o fuera de control razonable, que sea culpa del usuairio 

RDS Dynamo DB
    SQL VS No SQL 

SQL                                         NoSQL Dynamo DB
Scale up                                    scale out
HA Multimaster o read replicas              Resiliencia y sharding replication
multi AZ y Cross Regional replication       Multi Az y cross regional replication
Asynchronous  y async for read replicas     Consistency models 
99.95%
menos de 99.95 hasta 99.0= 10% de créditos
menos de 99.0 hasta 95.0 = 25%
menos de 95% = 100% de créditos

exclusions:
    estandar
    Ignorar la RDS user guide y no seguir los prinipios de operaciones
    bugs inerentes a la operacion



Multi Az deployments
single primary in 1 AZ  y standby node in 2da Az 
synchronous update to keep in sync
compute network o storage failure con failover automatico sobre el standby side
read replicas en la misma az, y failover en otras az
cross region para otra replica en otra az que pueda ser promovida a una standalone db dado el caso

Dynamo DB
4 9's y 2 9's para standar SLA
global tables con 3 9's 
menos de 99.999 a 99.0 = 10%
menos de 99.0%  a 95% = 25%
menos de 95% = 100%

standar SLA 
menos de 99.99%  a 99.0 = 10
menos de 99  a 95 = 25%
menos de 95% = 100%

 dynamo 1 replica en 2 regiones
 cada replica tiene un replica set de 3 replicas en 2 az


Fault tolerant computation en AWS  lambda y ec2

99.99 %
de 99.99 a 99.0 = 10%
99 a 95  =30%
menos de 95= 100%

exclusions. relacionado con sw o tecnologias y configuracion agena a la de la instancia


para resiliencia un EC2 puede tener varias eni (elastic network interface) una en casda az, 
una elastic ip adress,  y un ebs con snapshots en  diferentes S3

el ebs con réplica en otra region al igual que la ami 
se debe configurar el so para lograr éstas configuraciones
 entonces tienes una ec2 con 2 eni en diferentes az, un ebs  con snapshot en s3 global y respaldo 
 del s3  y ami en otra region

lambda
 99.95% pero calculado por requests
 de 99.95 a 99.0 = 10%
 de 99.0 a 95.0 25%
 menos de 95% = 100%

 Exclusiones
    derivados de sw  y configuracion ajena a lambda
    no seguir las best practices

triger externo,
contenedor por az en 3 az dentro de la VPC
un versionador de control
una cola de delays
un proxy config para issues con connection tables
rds proxy para consumo rds



resilience

core resilience principles for AWS - Load Balancing and AutoScaling



target group, elb listeners de la app  y red para que el elb redirecciones¿ 
y el asg haga autoscaling in and out

Autoscaling para EC2 y lambda
ASG 
mantiene  la cantidad de instancias , 
escala manual o programada, escala por demanda, predictive AutoScaling
se le dice la ami y un launch template
capacidad mínima y deseada y máxima
escalado mediante el elb
lambda es vent driven entonces el escalado es automatico



para lamnbda se usa SQS queue, kinesis stream, Dynamo DB stream, evento source Mapping
synchronous, y asynchronous  trigger

eks  99.95 
ecs 99.99



ECS capacity provider 
task manager


k8 Architecture

control plane y data plane
kube apiserver, etcd
cluster Autoscaler
scheduler
k8 Master nodes
en aws VPC

kubelet/ kube proxy 
en cluster Autoscaling group 
con nodos administrados o worker nodes en la VPC, publica o privada 
en 3 az


k8 objectsd
1 cluster, un nodo master y varios workers 
pueden ser varios clusters virtuales backed en el mismo nodo físico 
piliticas, namespaces
replicaset
kube api server

replica set varios pods en el mismo cluster en una VPC

Load balancing 
como nginx

 3 tier application
 resilience en microservices app
 

Appmesh para la comunicacion entre servicios
state:
microservices
container 
service config
user sesion
app data
health endpoints no van directo a la db, si no que consultan el estado de la db
    que se refresca usando otro endpoint

para la comunicacion entre ms usar random timeout 
usar un circuit breaker state



