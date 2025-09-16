import psycopg2
from scripts.csv_loader import CsvLoader
from scripts.table_loader import TableLoader
from datetime import datetime
from scripts.info import Info
from psycopg2 import OperationalError


class PostgreLoader:

    def __init__(self, address_csv, address_tables):
        self.address_csv = address_csv
        self.address_tables = address_tables
        self.today = datetime.today().strftime("%Y-%m-%d\t%H:%M:%S")
        
        self.host = Info.HOST
        self.port = Info.PORT
        self.db_name = Info.DB_NAME
        self.user = Info.USER
        self.password = Info.PASSWORD



    def connect_postgresql(self):
        print(f"Initializing the connection to Data Warehousing on {self.today}")

        # connects to postgreSql Docker
        try:
            with psycopg2.connect(
                host= self.host,
                port= self.port,
                dbname= self.db_name,
                user= self.user,
                password= self.password
                ) as conn:
                    print("Conection estabilished")

                    # checks if the transactions table exists, if not it is created
                    self.creater_table_transacoes(conn, self.address_csv)

                    # inserts data into the tables agencies, clients, agency_collaborator, collaborators, accounts, credit_proposals
                    print(f"loading new data of the paths: ")
                    for address_table in self.address_tables:
                        print(f"{address_table}")
                    self.sql_table_loader(conn, self.address_tables)
                    print("Data Loaded in tables agencias, clientes, colaborador_agencia, colaboradores, contas, propostas_credito")

                    # Inserts data into the transactions table
                    print(f"loading new data to path: {self.address_csv}")
                    self.csv_table_loader(conn, self.address_csv)
                    print("Data Loaded")

                    conn.commit()      

        except OperationalError as error:
            raise OperationalError(f"Data Warehousing connection error:\n {error}\nVerify Data Warehousing credentials or initialize it")
        except Exception as error:
            raise Exception(f"Unexpected error: {error}")
        

        print(f"closing the connection to Data Warehousing on {self.today}") 


    def sql_table_loader(self, conn, address_tables):
        sql_loader_table = TableLoader(conn, address_tables)
        sql_loader_table.table_loader()
        

    def csv_table_loader(self, conn, address_csv):

        csv_loader_tables = CsvLoader(conn,address_csv)
        csv_loader_tables.transacao_table()

    
    def creater_table_transacoes(self, conn, address_csv):
        table_transacoes = CsvLoader(conn, address_csv)
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT EXISTS(
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                            AND table_name = 'transacoes'
                        )
                        """)
                exist_transacoes = cur.fetchone()[0]

                cur.execute("""
                    SELECT EXISTS(
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                            AND table_name = 'contas'
                        )
                        """)
                exist_contas = cur.fetchone()[0]
                
                if (exist_transacoes is False) and (exist_contas is True):
                    table_transacoes.table_transacoes_creater()
        except OperationalError as error:
            raise OperationalError(f"Data Warehousing connection error:\n {error}\nVerify Data Warehousing credentials or initialize it")
        except Exception as error:
            raise Exception(f"Unexpected error: {error}")
        
        
       
        

        

