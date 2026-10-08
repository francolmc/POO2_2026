from .conector import Conector
import sqlite3

class SqliteConector(Conector):
    # Modificador para parametros
    marcador_parametros = '?'

    def __init__(self, ruta_db='biblioteca.db'):
        super().__init__()
        self.__ruta_db = ruta_db

    def obtener_conexion(self):
        return sqlite3.connect(self.__ruta_db)