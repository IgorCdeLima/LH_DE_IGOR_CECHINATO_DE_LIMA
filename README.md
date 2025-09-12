# Projeto Data Pipeline com Apache Airflow


Este projeto implementa um pipeline de dados utilizando **Apache Airflow** como orquestrador e **PostgreSQL** como Data Warehouse.

O objetivo é extrair dados de arquivos **CSV** (atualizados diariamente) e alimentar um **Data Lake** local e um **Data Warehouse** em PostgreSQL.


## Estrutura Inicial

* **docker-compose.yml**: sobe o banco PostgreSQL local.
* **dbdata/**: volume de dados persistente do banco.
* **sql/**: scripts SQL.
* **dags/**: DAGs do Airflow.
* **data/**: Data Lake local (arquivos CSV extraídos).
* **scripts/**: scripts Python auxiliares.
* **logs/**: logs do Airflow.

## Pré-requisitos

Antes de iniciar, é necessário ter instalado:

* **Python 3.11 ou superior**
* **Docker**
* **Docker Compose**

# Preparação do Ambiente Python

## 1. Windows 


## Instalação do Docker

1. Verifique se ele ja esta instalado
```cmd
docker --version
docker compose version
```
2. Se não esta instalado acesse a url: https://www.docker.com/products/docker-desktop  realize o login no site e faça download conforme seu sistema operacional ARM64 ou AMD64

3. Acesse o Docker-desktop e realize o Login conforme as credenciais do site

4. Caso o Docker-Descktop peça para a atualizar, atualize o WSL com o comando
```cmd
wsl --update
```
5. após concluir a instalação do docker. apenas deve rodar o arquivo setup.bat


## Estrutura do Projeto

```
0.PROJETO/
├── dbdata/              # Dados persistentes do PostgreSQL
├── dags/                # DAGs do Airflow
├── data/                # Data Lake local (arquivos CSV)
├── scripts/             # Scripts Python auxiliares
├── sql/                 # Scripts SQL para criação do banco
├── logs/                # Logs do Airflow
├── .gitignore           # Arquivos/pastas ignoradas pelo Git
├── docker-compose.yml   # Configuração Docker para PostgreSQL e Airflow
├── requirements.txt     # Dependências Python
├── main.py              # Script principal
└── README.md            # Este arquivo
```

## Extra

* atualização do caminho do banvic.sql no docker-compose.yml
 ```
 volumes: 
 -.sql/banvic.sql:/docker-entrypoint-initdb.d/banvic.sql
 ```
