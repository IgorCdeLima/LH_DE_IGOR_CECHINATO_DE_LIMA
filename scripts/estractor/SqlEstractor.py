import pandas as pd
from pathlib import Path

class SqlEstractor:

    static_addres = Path(r"./sql/banvic.sql")

    def __init__(self):
        pass
    
    # Searching for data in the table
    def data_search(self, today):

        reading_data = False
        address_tables = []

        # name of tables
        name_table = ["agencias.csv", "clientes.csv", "colaborador_agencia.csv", "colaboradores.csv", "contas.csv", "proposta_credito.csv"]
        table_num = 0

        header = []
        row = []

        try:
            # address of tables
            new_table = Path(fr"./data/{today}/sql")
            new_table.mkdir(parents=True, exist_ok=False)
            
            # creating name_table.csv
            with open(self.static_addres, "r", encoding="utf-8") as file:
                    for line in file:
                        line = line.strip()

                        if "COPY" in line:

                            table_num += 1
                            reading_data = True

                            start = line.find("(")+1
                            end = line.find(")")
                            header = line[start:end].split(",")

                            if table_num == len(name_table):
                                break
                            
                        if r"\." in line:
                            file_name = fr"{new_table.resolve()}/{name_table[table_num]}"
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
            return
    
        return address_tables

                        

