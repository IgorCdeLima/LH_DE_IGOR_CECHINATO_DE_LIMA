from psycopg2 import ProgrammingError, errors


class CsvLoader:

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
        
    def csv_loader(self):
        try:
            with open(self.address_csv, "r", encoding="utf-8", newline='') as transacoes:
                with self.conn.cursor() as cur:   
                    for i, line in enumerate(transacoes):
                        line = line.split(",")
                        if i == 0:
                            pass
                        elif i > 10:
                            break
                        else:
                            data = {
                                'cod_transacao' : int(line[0]),
                                'num_conta' : int(line[1]),
                                'data_transacao' : str(line[2]),
                                'nome_transacao' : str(line[3]),
                                'valor_transacao' : float(line[4])
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






