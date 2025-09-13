import pandas as pd

class CsvLoader:

    def __init__(self, conn, address_csv):
        self.cur = conn.cursor()
        self.address_csv = address_csv
    
    def csv_loader(self):
        try:
            print(f"endereço do csv: {self.address_csv}")
            self.cur.execute(f"""
                SELECT * FROM public.clientes;
            """)
        except Exception as error:
            print(f"error: {error}\nnão foi encontrar a tabela")



        row = self.cur.fetchall()
        cols  = [desc[0] for desc in self.cur.description]
        file = pd.DataFrame(row, columns=cols)
        print(file.to_string())

        print("\ninserções de transacoes.csv condluidas")   
        self.cur.close()



