@echo off

@echo iniciando o programa Apache airflow
docker-compose up airflow-init -d

cls

@echo Subindo os containers
docker-compose up -d

@echo Operação finalizada
pause