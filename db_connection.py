import pyodbc
from decouple import config

def connection():
    direccion_servidor = config("SERVER")
    nombre_bd = config("DB_NAME")
    nombre_usuario = config("USER")
    password = config("PASSWORD")
    try:
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + 
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
        # print("conexión exitosa")
        return con
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)
        return None

