import pandas as pd
from pathlib import Path
from scripts.info import Info

class SqlEstractor:

    def __init__(self):
        self.static_address = Info.SQL_SOURCE
        self.data_lake = Info.DATA_LAKE_DIR
    
    # Searching for data in the table
    def data_search(self, today):
        try:
            # checking for the existence of the banvic.sql file
            if not self.static_address.resolve().exists():
                raise FileNotFoundError

            reading_data = False
            address_tables = []
            table_num = 0
            header = []
            row = []
            new_table = Path(fr"{self.data_lake}/{today}/sql")

            if new_table.exists():
                raise FileExistsError
            
            # address of tables
            new_table.mkdir(parents=True, exist_ok=False)

                # creating name_table.csv
            tables = {
                1 : new_table / 'agencias.csv',
                2 : new_table / 'clientes.csv',
                3 : new_table /'colaborador_agencia.csv',
                4 : new_table / 'colaboradores.csv',
                5 : new_table /'contas.csv',
                6 : new_table / 'proposta_credito.csv'
            }


            with open(self.static_address, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()

                    if "COPY" in line:

                        table_num += 1
                        reading_data = True

                        start = line.find("(")+1
                        end = line.find(")")
                        header = line[start:end].split(",")
                        
                        file_name = str(tables.get(table_num))
                        if file_name is None:
                            break

                        continue

                    if r"\." in line:

                        address_tables.append(file_name)

                        pd.DataFrame(row, columns=header).to_csv(file_name, index=False)

                        header = []
                        row = []
                        reading_data = False
                        
                    if reading_data:
                        row.append(line.split("\t"))

            for address in address_tables:
                if Path(address).exists():
                    print(f"new file create on date {today} in: {address}")
                else:
                    print(f"Create File error on date {today} in: {address}")

            return address_tables
        
        except Exception:
            raise
        


