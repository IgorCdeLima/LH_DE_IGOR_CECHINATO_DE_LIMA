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
* Editor de código (ex.: VSCode)

## Instalação do Ambiente Python

1. Crie um ambiente virtual:

```bash
python -m venv venv
```

2. Ative o ambiente virtual:

* Windows:

```bash
venv\Scripts\activate
```

* Linux/Mac:

```bash
source venv/bin/activate
```

3. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```
## Instalação do Docker

1. Verifique se ele ja esta instalado
```bash
docker --version
docker compose version
```
2. Se não esta instalado acesse a url: https://www.docker.com/products/docker-desktop  realize o login no site e faça download conforme seu sistema operacional

3. Acesse o Docker-desktop e realize o Login conforme as credenciais do site

4. Abra seu terminal use o comando: 
```bash
wsl --version
```
5. Se necessário atualize o WSL 
```bash
wsl --update
```
6. Reinicie seu máquina 

## Instalação e Inicialização do PostgreSQL via Docker

1. Subir o container do PostgreSQL:

```bash
docker compose up -d
```

2. Verifique se o container está rodando:

```bash
docker ps
```

3. Acesse o banco de dados:

```bash
docker exec -it airflow_project-db-1 psql -U data_engineer -d banvic
```

> Nota: Ajuste o nome do container caso seja diferente do definido no `docker-compose.yml`.

## Como rodar o Apache Airflow

1. Inicialize os serviços do Airflow (assumindo que está configurado via Docker Compose):

```bash
docker compose up -d
```

2. Acesse a interface web do Airflow:

```
http://localhost:8080
```

3. Crie e visualize DAGs, configure tarefas e agende pipelines.

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

## Como rodar o projeto

1. Ative o ambiente virtual Python.
2. Suba os containers Docker (`docker compose up -d`).
3. Execute os scripts Python ou DAGs do Airflow conforme a lógica do projeto.

## Extra

* Atualizar dependências Python:

```bash
pip freeze > requirements.txt
```

* Backup de dados PostgreSQL:

```bash
docker exec -t airflow_project-db-1 pg_dumpall -c -U data_engineer > backup.sql
```

* Logs do Airflow são armazenados na pasta `logs/`.

---
