from models.socio import Socio

class SocioRepository:
    def __init__(self, conexion):
        self.__conexion = conexion

    def crear(self, socio:Socio):
            cursor = self.__conexion.cursor()
            cursor.execute("""
            INSERT INTO socios VALUES (?, ?)
            """, (socio.numero_socio, socio.nombre,))
            self.__conexion.commit()
    
    def buscar_por_numero_socio(self, numero_socio:int):
        cursor = self.__conexion.cursor()
        cursor.execute("""
        SELECT numero_socio, nombre FROM socios WHERE numero_socio = ?
        """, (numero_socio,))
        registro = cursor.fetchone()
        if registro is None:
            return None
        return Socio(registro[0], registro[1])

    def actualizar_socio(self, socio:Socio):
        cursor = self.__conexion.cursor()
        cursor.execute("""
        UPDATE socios SET
            nombre = ?
        WHERE
            numero_socio = ?
        """, (socio.nombre, socio.numero_socio))
        self.__conexion.commit()
        return cursor.rowcount > 0

    def eliminar(self, numero_socio):
        cursor = self.__conexion.cursor()
        cursor.execute("DELETE FROM socios WHERE numero_socio = ?", (numero_socio,))
        self.__conexion.commit()
        return cursor.rowcount > 0

    def todos(self):
        cursor = self.__conexion.cursor()
        cursor.execute(
            "SELECT numero_socio, nombre FROM socios"
        )
        todos = cursor.fetchall()
        socios = []
        if len(todos) > 0:
            for item in todos:
                socios.append(
                    Socio(item[0], item[1])
                )
        return socios

    def buscar_por_nombre(self, nombre: str):
        cursor = self.__conexion.cursor()
        cursor.execute(
            "SELECT numero_socio, nombre FROM socios WHERE nombre LIKE ?",
            (f"%{nombre}%",)
        )
        todos = cursor.fetchall()
        socios = []
        if len(todos) > 0:
            for item in todos:
                socios.append(
                    Socio(item[0], item[1])
                )
        return socios
