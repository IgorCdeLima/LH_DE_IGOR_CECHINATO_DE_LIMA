from pathlib import Path 
import pandas as pd
import shutil
from scripts.info import Info
from scripts.exceptions.exception_program import ExceptionProgram
import logging

class CsvDataEstractor:

    def __init__(self):
        self.static_address = Info.CSV_SOURCE
        self.data_lake = Info.DATA_LAKE_DIR
        
    # Create a transacoes.csv in Data Lake
    def bkp_csv(self, today):
        try: 
            if self.static_address.resolve(strict=True):
                new_address = Path(self.data_lake / today /'csv')
                new_address.mkdir(parents=True, exist_ok=False)
                csv_file = Path(new_address.resolve() / 'transacoes.csv')
                shutil.copy(self.static_address.resolve(), csv_file)
                self._clean_csv()
                print(f"new file transacoes.csv on date {today} in: {csv_file.resolve()} ")
                return str(csv_file.resolve())
        except Exception as error:
            raise ExceptionProgram(error, today)
        
    # Clean the file: transacoes.csv 
    def _clean_csv(self):

        try: 
            with open(self.static_address, "r") as file:
                header = file.readline().strip().split(",")

            csv_to_clean = pd.DataFrame(columns=header)
            csv_to_clean.to_csv(self.static_address, index=False )
        except Exception as error:
            raise ExceptionProgram(error)
    


   
