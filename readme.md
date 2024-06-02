Para rodar:

- Para qualquer alteração é necessário recriar o container:
* docker-compose down --rmi all

- E após isso é necessário criar o container que instala todas as depedências:
* docker-compose up --build

Posteriormente:

- É preciso criar os bancos:

* docker cp initialize_databases.py api_1:/app/initialize_databases.py

* docker exec -it api_1 python /app/initialize_databases.py 
