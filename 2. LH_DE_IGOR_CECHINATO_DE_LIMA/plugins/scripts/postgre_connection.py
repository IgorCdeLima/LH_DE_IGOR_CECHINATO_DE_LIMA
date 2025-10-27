import psycopg2
from datetime import datetime
from scripts.info import Info
from scripts.exceptions.exception_program import ExceptionProgram


class PostgreConnection:

    def __init__(self):
        self.conn = None
        self.host = Info.HOST
        self.port = Info.PORT
        self.db_name = Info.DB_NAME
        self.user = Info.USER
        self.password = Info.PASSWORD



    def __enter__(self):
        today = datetime.today().strftime("%Y-%m-%d\t%H:%M:%S")
        print(f"Initializing the connection to Data Warehousing on {today}")
        # connects to postgreSql Docker
        try:
            self.conn =  psycopg2.connect(
                host= self.host,
                port= self.port,
                dbname= self.db_name,
                user= self.user,
                password= self.password
                )
            print("Conection estabilished")

        except Exception as error:
            raise ExceptionProgram(error)
        return self.conn
       

    def __exit__(self,exc_type, exc_val, exc_tb):
        today = datetime.today().strftime("%Y-%m-%d\t%H:%M:%S")
        try: 
            if exc_type:
                if self.conn:
                    self.conn.rollback()
                    print("Rollback executed due to error")
                raise ExceptionProgram(exc_val)
        finally:
            if self.conn:
                self.conn.close()
                print(f"Closing the connection to Data Warehousing on {today}")
        
        

        
       
        

        

