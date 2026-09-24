from models.libro import Libro
from repositories.libro_repository import LibroRepositorio
from database.connection import obtener_conexion, crear_tablas

rayuela = Libro("978-0-2", "Rayuela", 2)

crear_tablas()

conexion = obtener_conexion()
respositorio_libro = LibroRepositorio(conexion)
respositorio_libro.crear(rayuela)
