from datetime import datetime
from pathlib import Path
from scripts.estractor.csv_data_estractor import CsvDataEstractor
from scripts.estractor.sql_estractor import SqlEstractor


class DataLake:

    
    
    def __init__(self):
        self.today = datetime.today().strftime("%Y-%m-%d")
        self.file_csv_bkp = CsvDataEstractor()
        self.file_sql_bkp = SqlEstractor()
    
    # Extrair os dados de nosso arquivo.CSV
    def csv_estractor(self):
        address = Path(fr"./data/{self.today}/csv")
        try:
            address.mkdir(parents=True, exist_ok=False)
            file_csv = self.file_csv_bkp.bkp_csv(address.resolve())
            print(f"new file transacoes.csv on date {self.today} in: {file_csv} ")
        except Exception as error:
            print(f"error: {error}")
            return error

        return file_csv
    

    # Extrair os dados de nosso arquivo.SQL e salvar por tabela
    def sql_estractor(self):
        try:
            address_table = self.file_sql_bkp.data_search(self.today)
            print(f"new file table.csv on date {self.today} in: ")
            for addres in address_table:
                print(addres)
        except Exception as error:
            print(f"{error}")
        
        return address_table
