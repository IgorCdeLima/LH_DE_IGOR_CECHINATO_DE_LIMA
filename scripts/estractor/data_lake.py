from datetime import datetime
from pathlib import Path
from scripts.estractor.csv_data_estractor import CsvDataEstractor
from scripts.estractor.sql_estractor import SqlEstractor


class DataLake:
    def __init__(self):
        self.today = datetime.today().strftime("%Y-%m-%d")
        self.file_csv_bkp = CsvDataEstractor()
        self.file_sql_bkp = SqlEstractor()
    
    # Extract data from transacoes.CSV file
    def csv_estractor(self):
       
        try:
            file_csv = self.file_csv_bkp.bkp_csv(self.today)
        except Exception as error:
            raise Exception(f"File transacoes.csv do not exist. error: {error}")
        
        return file_csv

    # Estract datas from banvic.sql
    def sql_estractor(self):
        try:
            address_table = self.file_sql_bkp.data_search(self.today)
        except Exception as error:
            raise UnboundLocalError(f"Files tables.csv do not exist. Error{error}")
        
        return address_table
