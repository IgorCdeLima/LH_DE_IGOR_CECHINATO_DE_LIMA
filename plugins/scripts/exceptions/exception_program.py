from psycopg2 import ProgrammingError, OperationalError
from psycopg2.errors import UndefinedTable, IntegrityError
import logging
from pathlib import Path
from scripts.info import Info

class ExceptionProgram(Exception):
    
    def __init__(self, error, today):

        caminho = Path(Info.BASE_LOG / 'error' / today /'log_error.log')
        self.create_logger(caminho)
        self.exception_program(error)

    def create_logger(self,caminho):

        log_error = logging.getLogger("ProgramError")
        log_error.setLevel(logging.ERROR)
        log_format = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')


        bash = logging.StreamHandler()
        bash.setLevel(logging.ERROR)

        file = logging.FileHandler(caminho, 'a')
        file.setLevel(logging.ERROR)


        bash.setFormatter(log_format)
        file.setFormatter(log_format)

        if not log_error.hasHandlers():
            log_error.addHandler(bash)
            log_error.addHandler(file)
            
    
    def exception_program(self, error):

        if isinstance(error, FileNotFoundError):
            raise FileNotFoundError(f"search error. File not found in: {error}") from error
        elif isinstance(error, RuntimeError):
            raise RuntimeError(f"error in program execution: {error}") from error
        elif isinstance(error, (ValueError, TypeError)):
            raise ValueError(f"error in the value or type of the object: {error}")
        elif isinstance(error, FileExistsError):
            raise FileExistsError(f"exist in path, error:{error}") from error
        elif isinstance(error, ProgrammingError):
            raise ProgrammingError(f"error in sql command: {error}") from error
        elif isinstance(error, UndefinedTable):
            raise UndefinedTable(f"error in search the table:{error}") from error
        elif isinstance(error, IntegrityError):
            raise IntegrityError(f"integraty error inserting data: {error}") from error
        elif isinstance(error, UnboundLocalError):
            raise UnboundLocalError(f"error in variable: {error}") from error
        elif isinstance(error, OperationalError):
            raise OperationalError(f"Data Warehousing connection error:\n {error}\nVerify Data Warehousing credentials or initialize it") from error
        elif isinstance(error, OSError):
            raise OSError(f"memory error or disk full, or file corruption: {error}") from error
        elif isinstance(error, PermissionError):
            raise PermissionError(f"Read permission error: {error}")
        else: 
            raise Exception(f"Unexpected error: {error}") from error