from psycopg2 import ProgrammingError, OperationalError
from psycopg2.errors import UndefinedTable, IntegrityError
import logging
from pathlib import Path
from scripts.info import Info
from datetime import datetime
import sys


class ExceptionProgram(Exception):
    
    def __init__(self, error):

        today = datetime.today().strftime("%Y-%m-%d")
        caminho = Path(Info.BASE_LOG / 'error' / today )
        caminho.mkdir(parents=True, exist_ok=True)
        caminho_log = Path(caminho / 'log_error.log')
        self.logger(caminho_log, error)
        

    def logger(self,caminho, error):
        log_error = logging.getLogger("ProgramError")

        log_error.setLevel(logging.ERROR)
        log_format = logging.Formatter('[%(levelname)s] -  %(asctime)s  -  %(name)s: %(message)s')


        bash = logging.StreamHandler()
        bash.setLevel(logging.ERROR)

        file = logging.FileHandler(caminho, 'a')
        file.setLevel(logging.ERROR)


        bash.setFormatter(log_format)
        file.setFormatter(log_format)

        if not log_error.hasHandlers():
            log_error.addHandler(bash)
            log_error.addHandler(file)
        
        self.exception_program(error, log_error)
            
    
    def exception_program(self, error, log):
        
        msg_error = {
            FileNotFoundError : "search error. File not found in: {}",
            RuntimeError : "error in program execution: {}",
            ValueError :  "error in the value or type of the object: {}",
            TypeError :  "error in the value or type of the object: {}",
            FileExistsError : "exist in path, error:{}",
            ProgrammingError : "error in sql command: {}",
            UndefinedTable : "error in search the table:{}",
            IntegrityError : "integraty error inserting data: {}",
            UnboundLocalError : "error in variable: {}",
            OperationalError : "Data Warehousing connection error:\n {}\nVerify Data Warehousing credentials or initialize it",
            OSError : "memory error or disk full, or file corruption: {}",
            PermissionError : "Read permission error: {}"        
            }
        msg = msg_error.get(type(error), "Unexpected error: {}")
        log.error(msg.format(error))
        sys.exit(1)