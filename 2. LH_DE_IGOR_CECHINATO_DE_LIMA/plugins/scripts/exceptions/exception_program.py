from psycopg2 import ProgrammingError, OperationalError
from psycopg2.errors import UndefinedTable, IntegrityError


class ExceptionProgram(Exception):
    
    def __init__(self, error):
        self.error = error
        self.msg_error = {
            FileNotFoundError : "search error. File not found in: {}",
            RuntimeError : "error in program execution: {}",
            ValueError :  "error in the value or type of the object: {}",
            TypeError :  "error in the value or type of the object: {}",
            FileExistsError : "File exist in path. Error:{}",
            ProgrammingError : "error in sql command: {}",
            UndefinedTable : "error in search the table:{}",
            IntegrityError : "integraty error inserting data: {}",
            UnboundLocalError : "error in variable: {}",
            OperationalError : "Data Warehousing connection error:\n {}\nVerify Data Warehousing credentials or initialize it",
            OSError : "memory error or disk full, or file corruption: {}",
            PermissionError : "Read permission error: {}",        
            }
        self.msg = self.msg_error.get(type(error), "Unexpected error: {}").format(error)
        super().__init__(self.msg) 
    
    def __str__(self):
        return f"[{type(self.error).__name__}] {self.msg}"

 