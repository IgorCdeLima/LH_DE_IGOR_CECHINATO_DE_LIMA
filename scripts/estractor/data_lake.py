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
       
        try:
            file_csv = self.file_csv_bkp.bkp_csv(self.today)
        except Exception as error:
            raise UnboundLocalError("File transacoes.csv do not exist")
        
        return file_csv
            
    

    # Extrair os dados de nosso arquivo.SQL e salvar por tabela
    def sql_estractor(self):
        try:
            address_table = self.file_sql_bkp.data_search(self.today)
        except Exception as error:
            raise UnboundLocalError("Files tables.csv do not exist")
        
        return address_table
