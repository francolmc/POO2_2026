from models.libro import Libro
from repositories.libro_repository import LibroRepositorio
from database.connection import obtener_conexion, crear_tablas
from database.mysql_conector import MySQLConector
from database.sqlite_conector import SqliteConector

conexion_sqlite = SqliteConector(ruta_db='biblioteca.db')
conexion_mysql = MySQLConector(
    host='localhost',
    usuario = 'root',
    clave = 'masterdba',
    base_datos = 'ejemplo_biblioteca'
)

crear_tablas(conexion_mysql)

rayuela = Libro(id=1, isbn='123', titulo='Rayuela', copias_disponibles=5)
repositorio_libro = LibroRepositorio(conexion_mysql, conexion_mysql.marcador_parametro)
repositorio_libro.crear(rayuela)
