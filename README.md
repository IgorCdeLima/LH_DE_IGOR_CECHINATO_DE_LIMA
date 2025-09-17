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

* **Python 3.11 ou superior (não recomendado Python 3.13)**
* **Docker**
* **autalizar o WSL**

## Instalação do Docker

1. Verifique se ele ja esta instalado

```bash
docker --version
docker compose version
```
2. Se não esta instalado acesse a url: https://www.docker.com/products/docker-desktop  realize o download conforme seu sistema operacional ARM64 ou AMD64

3. Acesse o Docker-desktop e atualize o WSL

```bash
wsl --update
```
4. após concluir a instalação e atualização do docker caso necessário, inicie o Docker e ele ficara rodando em background

5. Encontre a pasta LH_DE_IGOR_CECHINATO_DE_LIMA 

6. para linux/mac rode o setup.sh para o linux setup.bat

7. Acesse o site de nosso Apache Airflow:  https://localhost:8080  

8. Na aba dags procure por LH_DE_IGOR_CECHINATO_DE_LIMA e ative ela


## Estrutura do Projeto

```
0.PROJETO/
├── dbdata/              # Dados persistentes do PostgreSQL
├── csv                  # Arquivo csv utilizado na exportação dos dados
├── dags/                # DAGs do Airflow
├── data/                # Data Lake local (arquivos CSV)
├── plugins/             # Scripts Python auxiliares
├── sql/                 # Scripts SQL para criação do banco
├── logs/                # Logs do Airflow
├── config               # Configurações do docker / requirements.txt
├── docker-compose.yaml  # Configuração Docker para PostgreSQL e Airflow
└── README.md            # Este arquivo
```

## Extra

* atualização do caminho do banvic.sql no docker-compose.yml
 ```
 volumes: 
 -.sql/banvic.sql:/docker-entrypoint-initdb.d/banvic.sql
 ```
