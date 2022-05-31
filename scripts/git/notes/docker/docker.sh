#detener servicios
sudo service docker stop
sudo service rabbitmq-server stop
sudo service mysql stop
#lanzar imagenes
#sudo docker run -p puerto_interno:puerto externo --name nombre_instancia --network red nombremagen:version
sudo docker run -p 8888:8888 --name uds-config-server --network uds-network uds-config-server:v1
sudo docker run -p 8761:8761 --name uds-eureka-server --network uds-network uds-eureka-server:v1
sudo docker run -p 3306:3306 --name uds-mysql-latest --network uds-network -e MYSQL_ROOT_PASSWORD=31y0_*PU3d0.31 -e MYSQL_DATABASE=uds_productos_db -e MYSQL_USER=anaDMIN -e MYSQL_PASSWORD=34y0_*PU3d0.34 mysql:latest --character-set-server=utf8 --collation-server=utf8_general_ci
docker stop $(docker ps -q)


    .\mvnw clean package
     
    docker build -t config-server:v1 .
    docker network create spring-microservicios
    docker run -p 8888:8888 --name config-server --network springcloud config-server:v1

    docker pull postgres:12-alpine
    docker run -p 5432:5432 --name microservicios-postgres12 --network springcloud -e POSTGRES_PASSWORD=sasa -e POSTGRES_DB=db_springboot_cloud -d postgres:12-alpine
    docker logs -f microservicios-postgres12

    docker stop $(docker ps -q)
    docker rm $(docker ps -a -q)

docker rmi $(docker images -a -q)
