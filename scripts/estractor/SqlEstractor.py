import pandas as pd
from pathlib import Path

class SqlEstractor:

    static_addres = Path(r"./sql/banvic.sql")

    def __init__(self):
        pass
    
    # Procurar os novos dados
    def data_search(self, today):

        reading_data = False

        name_table = ["agencias.csv", "clientes.csv", "colaborador_agencia.csv", "colaboradores.csv", "contas.csv", "proposta_credito.csv"]
        table_num = 0

        header = []
        row = []

        new_table = Path(fr"./data/{today}/sql")
        new_table.mkdir(parents=True, exist_ok=False)
        

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
                        continue
                    if r"\." in line:
                        file_name = fr"{new_table.resolve()}/{name_table[table_num]}"
                        print("--------------------------------------------\n")
                        print(file_name)
                        print("--------------------------------------------\n")


                        file_writer = pd.DataFrame(row,columns=header) 

                        print(file_writer)
                        print("\n\n\n")
                        file_writer.to_csv(file_name, index=False)

                        
                        header = []
                        row = []
                        reading_data = False
                        
                    if reading_data:
                        row.append(line.split("\t"))

        print("Processo acabado")

                        

