from conector import Conector
import mysql

class MySQLConector(Conector):
    marcador_parametro = '%s'

    def __init__(self, host, usuario, clave, base_datos):
        super().__init__()
        self.host = host
        self.usuario = usuario
        self.clave = clave
        self.base_datos = base_datos

    def obtener_conexion(self):
        import mysq.connector
        return mysq.connector.connect(
            host = self.host,
            user = self.usuario,
            password = self.clave,
            database = self.base_datos
        )