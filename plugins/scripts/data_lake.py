from datetime import datetime
from scripts.csv_data_estractor import CsvDataEstractor
from scripts.sql_estractor import SqlEstractor
from scripts.exceptions.exception_program import ExceptionProgram

# melhorar o Exception aqui


class DataLake:
    def __init__(self):
        self.today = datetime.today().strftime("%Y-%m-%d")
        self.file_csv_bkp = CsvDataEstractor()
        self.file_sql_bkp = SqlEstractor()
    
    # Extract data from transacoes.CSV file
    def csv_estractor(self):
        file_csv = None
        try:
            file_csv = self.file_csv_bkp.bkp_csv(self.today)
        except Exception as error:
            raise ExceptionProgram(error)
        
        if file_csv is not None:
            return file_csv

    # Estract datas from banvic.sql
    def sql_estractor(self):
        address_table = None
        try:
            address_table = self.file_sql_bkp.data_search(self.today)
        except Exception as error:
            raise ExceptionProgram(error)
        
        if address_table is not None:
            return address_table
