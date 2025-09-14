from psycopg2 import ProgrammingError, errors
import pandas as pd


class CsvLoader:

    CHUNKSIZE = 1

    def __init__(self, conn, address_csv):
        self.conn = conn
        self.address_csv = address_csv


    def table_transacoes_creater(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""        
                CREATE TABLE IF NOT EXISTS public.transacoes(
                    cod_transacao   int PRIMARY KEY,
                    num_conta       bigint  NOT NULL,
                    data_transacao  timestamp with time zone NOT NULL,
                    nome_transacao  character varying(255) NOT NULL,
                    valor_transacao numeric(15,2) NOT NULL
                );
                    """)
                print("table public.transacoes was created")

            with self.conn.cursor() as cur:
                cur.execute("""
                            ALTER TABLE public.transacoes
                            ADD CONSTRAINT  fk_transacoes_contas
                            FOREIGN KEY(num_conta)
                            REFERENCES public.contas (num_conta);
                    """)
                print(f"table public.transacoes was configured with the foreign key num_conta from the table public.contas")          

        except errors.UndefinedTable as error:
            raise errors.UndefinedTable(f"the tables public.contas or public.transacoes does not exist")
        except ProgrammingError as error:
            raise ProgrammingError(f"error in sql command: {error}")
        except Exception as error:
            raise Exception(f"Unexpected error: {error}")
        
        print("Table public.transacoes was created and configured")
        


    def transacao_table(self):
        print("Inserting data into the proposta_credito table ")
        try:
            with self.conn.cursor() as cur:
                for chunk in pd.read_csv(self.address_csv, chunksize=self.CHUNKSIZE):
                    chunk.columns = chunk.columns.str.strip()  
                    for index, row in chunk.iterrows():
                        data = {
                            'cod_transacao' : int(row['cod_transacao']),
                            'num_conta' : int(row['num_conta']),
                            'data_transacao' : row['data_transacao'],
                            'nome_transacao' : row['nome_transacao'],
                            'valor_transacao' : row['valor_transacao']
                            }
                        cur.execute(
                                """INSERT INTO public.transacoes(cod_transacao,num_conta,data_transacao,nome_transacao,valor_transacao) 
                                VALUES (%(cod_transacao)s, %(num_conta)s, %(data_transacao)s, %(nome_transacao)s, %(valor_transacao)s) 
                                ON CONFLICT (cod_transacao) DO NOTHING
                                RETURNING cod_transacao;
                                """, data)
                            
                        result = cur.fetchone()
                        if result:
                            print(f"Inserted line: {data['cod_transacao']}")
                        else:
                            print(f"line not inserted: {data['cod_transacao']}")

        except errors.UndefinedTable as error:
            raise errors.UndefinedTable(f"the table public.transacoes does not exist")
        except ProgrammingError as error:
            raise ProgrammingError(f"error in sql command: {error}")
        except FileNotFoundError as error:
            raise FileNotFoundError(f"error searching the path: {error}")
        except errors.IntegrityError as error:
            raise errors.IntegrityError(f"integraty error inserting data: {error}")
        except Exception as error:
            raise Exception(f"Unexpected error: {error}")
        
        print("insertion completed in the propostas_credito table")



