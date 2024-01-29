# SDP_Projeto
Projeto de Sistemas Distribuídos e Paralelos

Requere ficheiro .env com as seguintes chaves:

* SECRET_KEY - Chave para encryptar JWT
* CRYPT_KEY - Chave para encryptar mensagens
* DB_LOAD_BALANCER_IP - Porta do load balancer dos servidores da Data Layer
* BL_LOAD_BALANCER_IP - Porta do load balancer dos servidores da Business Layer

Dependencias:

* Flask
* dotenv
* mysql.connector
* bcrypt
* pyjwt
