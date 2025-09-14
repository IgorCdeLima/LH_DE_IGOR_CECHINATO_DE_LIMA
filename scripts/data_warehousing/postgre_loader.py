import psycopg2
from scripts.data_warehousing.csv_loader import CsvLoader
from scripts.data_warehousing.table_loader import TableLoader
from datetime import datetime
from scripts.config import Config
from psycopg2 import OperationalError


class PostgreLoader:

    def __init__(self, address_csv, address_tables):
        self.address_csv = address_csv
        self.address_tables = address_tables
        self.today = datetime.today().strftime("%Y-%m-%d\t%H:%M:%S")
        
        self.host = Config.HOST
        self.port = Config.PORT
        self.db_name = Config.DB_NAME
        self.user = Config.USER
        self.password = Config.PASSWORD



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
                            self.creater_table_transacoes(conn, self.address_csv)

                    print("Conection estabilished")

                    print(f"loading new data of the paths: ")
                    for address_table in self.address_tables:
                        print(f"{address_table}")
                    #self.sql_table_loader(conn, self.address_tables)

                    print(f"loading new data to path: {self.address_csv}")
                    self.csv_table_loader(conn, self.address_csv)                         
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
        csv_loader_tables.csv_loader()

    
    def creater_table_transacoes(self, conn, address_csv):
        
        table_transacoes = CsvLoader(conn, address_csv)
        table_transacoes.table_transacoes_creater()

        

