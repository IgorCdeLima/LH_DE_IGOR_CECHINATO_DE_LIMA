from pathlib import Path
import os


class Config:

    BASE_DIR = Path(os.getenv('PIPELINE_BASE_DIR', './'))
    CSV_SOURCE = BASE_DIR / 'csv' / 'transacoes.csv'
    SQL_SOURCE = BASE_DIR / 'sql' / 'banvic.sql'
    DATA_LAKE_DIR = BASE_DIR / 'data'

    HOST = "localhost"
    PORT = 55432
    DB_NAME = "banvic"
    USER = "data_engineer"
    PASSWORD = "v3rysecur&pas5w0rd"