import pandas as pd

class TableLoader:

    def __init__(self, conn, address_tables):
        self.cur = conn.cursor()
        self.addres_tables = address_tables

    def table_loader(self):
        

        try:
            for addres in self.addres_tables:
                print(f"endereço das tabelas {addres}")
            self.cur.execute(f"""
                SELECT nome FROM agencias;
            """)
        except Exception as error:
            print(f"error: {error}\nnão foi possivel concetar aos arquivos tables")   


        row = self.cur.fetchall()
        cols  = [desc[0] for desc in self.cur.description]
        file = pd.DataFrame(row, columns=cols)

        print(file.to_string())
        self.cur.close()