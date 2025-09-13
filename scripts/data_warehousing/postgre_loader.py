import psycopg2
from scripts.data_warehousing.csv_loader import CsvLoader
from scripts.data_warehousing.table_loader import TableLoader
from datetime import datetime
from scripts.config import Config


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
            conn = psycopg2.connect(
                host= self.host,
                port= self.port,
                dbname= self.db_name,
                user= self.user,
                password= self.password
            )
        except Exception as error:
            print(f"error: {error}, verify credentials to connect to the ware housing")
            return error
        
        if conn:
            try:
                self.sql_table_loader(conn, self.address_tables)
                self.csv_table_loader(conn, self.address_csv)
            except Exception as error:
                print(f"error:{error}")

        print(f"closing the connection to Data Warehousing on {self.today}")
        conn.close()


    def sql_table_loader(self, conn, address_tables):
        sql_loader_table = TableLoader(conn, address_tables)
        sql_loader_table.table_loader()
        

    def csv_table_loader(self, conn, address_csv):

        csv_loader_tables = CsvLoader(conn, address_csv)
        csv_loader_tables.csv_loader()

        
        

