from pathlib import Path 
import pandas as pd
import shutil

class CsvDataEstractor:

    static_address = Path(r"./csv/transacoes.csv")

    def __init__(self):
        pass

    # Create a backup
    def bkp_csv(self, new_address):

        try:

            file_bkp = Path(new_address / "transacoes.csv")
            shutil.copy(self.static_address.resolve(), file_bkp.resolve())
        except Exception as error:
            print(f"error: {error}")
            return 
        
        self._limpar_csv()
        return file_bkp.resolve()

    # Clean the file: transacoes.csv 
    def _limpar_csv(self):
        with open(self.static_address, "r") as file:
            header = file.readline().strip().split(",")
        csv_to_clean = pd.DataFrame(columns=header)
        csv_to_clean.to_csv(self.static_address, index=False )
        


    


   
