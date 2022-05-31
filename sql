ALTER USER 'uds_zipkin_user'@'localhost' IDENTIFIED WITH mysql_native_password BY '34y0_*PU3d0.34';
caching_sha2_password
sha256_password
mysql_old_password
mysql_native_password
mysql_clear_password

Server-side plugin 	authentication_pam
Client-side plugin 	mysql_clear_password
------------------------------------------------------
Server-side plugin 	authentication_windows
Client-side plugin 	authentication_windows_client
------------------------------------------------------
Server-side plugin names 	authentication_ldap_sasl, authentication_ldap_simple
Client-side plugin names 	authentication_ldap_sasl_client, mysql_clear_password
------------------------------------------------------
Server-side plugin 	mysql_no_login
Client-side plugin 	None
------------------------------------------------------
Server-side plugin 	auth_socket
Client-side plugin 	None, see discussion
------------------------------------------------------

------------------------------------------------------
sudo docker run -p 9411:9411 --name uds-zipkin-server --network uds-network -e RABBIT_ADDRESSES=uds-rabbit-server:5672 -e STORAGE_TYPE=mysql -e MYSQL_DB=uds_zipkin_log_db -e MYSQL_USER=uds_zipkin_user -e MYSQL_PASS=34y0_*PU3d0.34 -e MYSQL_HOST=uds-mysql-latest -e MYSQL_TCP_PORT=3306 uds-zipkin-server:v1

sudo docker run -p 9411:9411 --name uds-zipkin-server --network uds-network -e RABBIT_ADDRESSES=uds-rabbit-server:5672 -e STORAGE_TYPE=mysql -e MYSQL_DB=uds_zipkin_log_db -e MYSQL_USER=uds_zipkin_user -e MYSQL_PASS=34y0_*PU3d0.34 -e MYSQL_HOST=uds-mysql-latest -e MYSQL_TCP_PORT=3306 uds-zipkin-server:v1

sudo docker run -p 9411:9411 --name uds-zipkin-server --network uds-network -e RABBIT_ADDRESSES=uds-rabbit-server:5672 -e STORAGE_TYPE=mysql -e MYSQL_DB=uds_zipkin_log_db -e MYSQL_USER=uds_zipkin_user2 -e MYSQL_PASS=34y0_*PU3d0.34 -e MYSQL_HOST=uds-mysql-latest -e MYSQL_TCP_PORT=3306 uds-zipkin-server:v1

sudo docker run -p 9411:9411 --name uds-zipkin-server --network uds-network -e RABBIT_ADDRESSES=uds-rabbit-server:5672 -e STORAGE_TYPE=mysql -e MYSQL_DB=uds_zipkin_log_db -e MYSQL_USER=uds_zipkin_user3 -e MYSQL_PASS=34y0_*PU3d0.34 -e MYSQL_HOST=uds-mysql-latest -e MYSQL_TCP_PORT=3306 uds-zipkin-server:v1

sudo docker run -p 9411:9411 --name uds-zipkin-server --network uds-network -e RABBIT_ADDRESSES=uds-rabbit-server:5672 -e STORAGE_TYPE=mysql -e MYSQL_DB=uds_zipkin_log_db -e MYSQL_USER=uds_zipkin_user4 -e MYSQL_PASS=34y0_*PU3d0.34 -e MYSQL_HOST=uds-mysql-latest -e MYSQL_TCP_PORT=3306 uds-zipkin-server:v1

sudo docker run -p 9411:9411 --name uds-zipkin-server --network uds-network -e RABBIT_ADDRESSES=uds-rabbit-server:5672 -e STORAGE_TYPE=mysql -e MYSQL_DB=uds_zipkin_log_db -e MYSQL_USER=uds_zipkin_user5 -e MYSQL_PASS=34y0_*PU3d0.34 -e MYSQL_HOST=uds-mysql-latest -e MYSQL_TCP_PORT=3306 uds-zipkin-server:v1

sudo docker run -p 9411:9411 --name uds-zipkin-server --network uds-network -e RABBIT_ADDRESSES=uds-rabbit-server:5672 -e STORAGE_TYPE=mysql -e MYSQL_DB=uds_zipkin_log_db -e MYSQL_USER=uds_zipkin_user9 -e MYSQL_HOST=uds-mysql-latest -e MYSQL_TCP_PORT=3306 uds-zipkin-server:v1 --illegal-access=warn
sudo docker run -p 9411:9411 --name uds-zipkin-server --network uds-network -e RABBIT_ADDRESSES=uds-rabbit-server:5672 -e STORAGE_TYPE=mysql -e MYSQL_DB=uds_zipkin_log_db -e MYSQL_USER=uds_zipkin_user10 -e MYSQL_HOST=uds-mysql-latest -e MYSQL_TCP_PORT=3306 uds-zipkin-server:v1 --illegal-access=warn
