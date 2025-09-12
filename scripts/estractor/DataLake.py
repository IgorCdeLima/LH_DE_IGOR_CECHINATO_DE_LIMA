from datetime import datetime
from pathlib import Path
from scripts.estractor.CsvDataEstractor import CsvDataEstractor
from scripts.estractor.SqlEstractor import SqlEstractor


class DataLake:

    today = datetime.today().strftime("%Y-%m-%d")
    file_csv_bkp = CsvDataEstractor()
    file_sql_bkp = SqlEstractor()
    
    def __init__(self):
        pass
    
    # Extrair os dados de nosso arquivo.CSV
    def csv_estractor(self):
        address = Path(fr"./data/{self.today}/csv")
        try:
            address.mkdir(parents=True, exist_ok=False)
            file_csv = self.file_csv_bkp.bkp_csv(address.resolve())
            print(f"new addres to csv file on date {self.today}: {file_csv} ")

        except Exception as error:
            print(f"error: {error}")
            return

    # Extrair os dados de nosso arquivo.SQL e salvar por tabela
    def sql_estractor(self):
        self.file_sql_bkp.data_search(self.today)
