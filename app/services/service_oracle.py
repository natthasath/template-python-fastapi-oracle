from decouple import config
from fastapi.responses import JSONResponse
import cx_Oracle
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

cx_Oracle.init_oracle_client(lib_dir=config("ORACLE_INSTANTCLIENT"))

def convert_none(*args, **kwargs):
    data = list(args)
    # data = [f'{e}' for e in args]
    for key, val in enumerate(data):
        if val is None:
            data[key] = ''
    # print(f'args={args}, kwargs={kwargs}')
    return data

class OracleService:
    def __init__(self):
        self.oracle_offset = 0
        self.oracle_maxnumrows = 20
        self.oracle_host = config("ORACLE_HOST")
        self.oracle_encoding = config("ORACLE_ENCODING")

        self.oracle_username = config("ORACLE_USERNAME")
        self.oracle_password = config("ORACLE_PASSWORD")
        self.oracle_dsn = config("ORACLE_DSN")
        self.oracle_service = config("ORACLE_SERVICE")

    def connection(self):
        try:
            conn = cx_Oracle.connect(
                self.oracle_username,
                self.oracle_password,
                self.oracle_dsn,
                encoding=self.oracle_encoding
            )
            return conn
        except cx_Oracle.Error as error:
            return JSONResponse(status_code=502, content={"message": "Failed Connect Database"})
        
    def get_data(self, data):
        if len(data) == 0:
            return JSONResponse(status_code=404, content={"message": "Resource not found"})
        else:
            return data
        
    def all_employees(self):
        conn = self.connection()
        query = "SELECT * FROM EMPLOYEES"
        cur = conn.cursor()
        cur.execute(query)
        column = [x[0] for x in cur.description]
        data = [dict(zip(column, row)) for row in cur.fetchall()]
        return self.get_data(data)
    
    def search_employees(self, department):
        conn = self.connection()
        query = "SELECT * FROM EMPLOYEES WHERE DEPARTMENT_ID = '" + department + "'"
        cur = conn.cursor()
        cur.execute(query)
        column = [x[0] for x in cur.description]
        data = [dict(zip(column, row)) for row in cur.fetchall()]
        return self.get_data(data)