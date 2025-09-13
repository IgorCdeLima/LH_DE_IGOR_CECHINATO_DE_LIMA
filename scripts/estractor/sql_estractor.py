import pandas as pd
from pathlib import Path
import os
from scripts.config import Config

class SqlEstractor:

    def __init__(self):
        self.static_address = Config.SQL_SOURCE
        self.data_lake = Config.DATA_LAKE_DIR
    
    # Searching for data in the table
    def data_search(self, today):

        # checking for the existence of the banvic.sql file
        if os.path.exists(self.static_address.resolve()):
            reading_data = False
            address_tables = []

            # name of tables
            table_num = 0

            header = []
            row = []

            try:
                # address of tables
                new_table = Path(fr"{self.data_lake}/{today}/sql")
                new_table.mkdir(parents=True, exist_ok=False)
                # creating name_table.csv
                with open(self.static_address, "r", encoding="utf-8") as file:
                        for line in file:
                            line = line.strip()

                            if "COPY" in line:

                                table_num += 1
                                reading_data = True

                                start = line.find("(")+1
                                end = line.find(")")
                                header = line[start:end].split(",")

                                match table_num:
                                    case 1:
                                        file_name = fr"{new_table.resolve()}/agencias.csv"
                                    case 2:
                                        file_name = fr"{new_table.resolve()}/clientes.csv"
                                    case 3:
                                        file_name = fr"{new_table.resolve()}/colaborador_agencia.csv"
                                    case 4:
                                        file_name = fr"{new_table.resolve()}/colaboradores.csv"
                                    case 5:
                                        file_name = fr"{new_table.resolve()}/contas.csv"
                                    case 6:
                                        file_name = fr"{new_table.resolve()}/proposta_credito.csv"
                                    case _:
                                        break

                            if r"\." in line:

                                address_tables.append(file_name)

                                try:
                                    file_writer = pd.DataFrame(row,columns=header) 
                                    file_writer.to_csv(file_name, index=False)
                                except Exception as error:
                                    print(f"error: {error}")

                                header = []
                                row = []
                                reading_data = False
                                
                            if reading_data:
                                row.append(line.split("\t"))
            except Exception as error:
                print(f"error: {error}")
                return error
            
            print(f"new file tables.csv on date {today} in: ")
            for addres in address_tables:
                print(addres)
            return address_tables
        else:
            raise FileNotFoundError(f"SQL file not found: {self.static_address}")

