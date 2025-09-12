from datetime import datetime
from pathlib import Path
import pandas as pd
from scripts.estractor.CsvDataEstractor import CsvDataEstractor


class DataLake:

    today = datetime.today().strftime("%Y-%m-%d")
    file_bkp = CsvDataEstractor()
    
    def __init__(self):
        pass
    
    # Extrair os dados de nosso arquivo.CSV
    def csv_estractor(self):
        address = Path(fr"./data/{self.today}/csv")
        try:
            address.mkdir(parents=True, exist_ok=False)
            file_csv = self.file_bkp.bkp_csv(address.resolve())
            print(f"new addres to csv file on date {self.today}: {file_csv} ")

        except Exception as error:
            print(f"error: {error}")
            return

    # Extrair os dados de nosso arquivo.SQL e salvar por tabela
    def sql_estractor():
        pass