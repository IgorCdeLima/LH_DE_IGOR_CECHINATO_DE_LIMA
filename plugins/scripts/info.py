from pathlib import Path
import os


class Info:

    BASE_DIR = Path(os.getenv('PIPELINE_BASE_DIR', Path(__file__).parents[2]))
    CSV_SOURCE = BASE_DIR / 'dags' / 'csv' / 'transacoes.csv'
    SQL_SOURCE = BASE_DIR / 'dags' /  'sql' / 'banvic.sql'
    DATA_LAKE_DIR = BASE_DIR / 'dags/' 'data'

    HOST = "localhost"
    PORT = 55432
    DB_NAME = "banvic"
    USER = "data_engineer"
    PASSWORD = "v3rysecur&pas5w0rd"