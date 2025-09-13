from pathlib import Path 
import pandas as pd
import shutil
import os

class CsvDataEstractor:

    static_address = Path(r"./csv/transacoes.csv")

    def __init__(self):
        pass
        

    # Create a backup
    def bkp_csv(self, today):
        if os.path.exists(self.static_address.resolve()):

            new_address = Path(fr"./data/{today}/csv")
            new_address.mkdir(parents=True, exist_ok=False)

            try:

                file_bkp = Path(new_address / "transacoes.csv")
                shutil.copy(self.static_address.resolve(), file_bkp.resolve())
            except Exception as error:
                print(f"error: {error}")
                return error
        
            self._limpar_csv()

            print(f"new file transacoes.csv on date {today} in: {file_bkp} ")
            return file_bkp.resolve()
        
        else:
            print(f"arquive NotFound in path: {self.static_address}")

    # Clean the file: transacoes.csv 
    def _limpar_csv(self):
        if os.path.exists(self.static_address):
            with open(self.static_address, "r") as file:
                header = file.readline().strip().split(",")

            csv_to_clean = pd.DataFrame(columns=header)
            csv_to_clean.to_csv(self.static_address, index=False )
        else: 
             print(f"arquive NotFound in path: {self.static_address}")
        
        


    


   
