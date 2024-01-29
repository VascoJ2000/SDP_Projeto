# SDP_Projeto
Projeto de Sistemas Distribuídos e Paralelos

Requere ficheiro .env com as seguintes chaves:

* SECRET_KEY - Chave para encryptar JWT
* CRYPT_KEY - Chave para encryptar mensagens


* DB_LOAD_BALANCER_IP - IP do load balancer dos servidores da Data Layer
* DB_LOAD_BALANCER_PORT - Porta do load balancer dos servidores da Data Layer
* BL_LOAD_BALANCER_IP - IP do load balancer dos servidores da Business Layer
* BL_LOAD_BALANCER_PORT - Porta do load balancer dos servidores da Business Layer


* DB_HOST - Database host ip
* DB_PORT - Database host port
* DB_USER - Database user username
* DB_PASSWORD - Database user password
* DB_NAME - Database name

Dependencias:

* Flask
* dotenv
* mysql.connector
* bcrypt
* pyjwt
