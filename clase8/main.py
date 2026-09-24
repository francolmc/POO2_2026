from models.libro import Libro
from repositories.libro_repository import LibroRepositorio
from database.connection import obtener_conexion, crear_tablas

# rayuela = Libro("978-0-2", "Rayuela", 2)

crear_tablas()

conexion = obtener_conexion()

respositorio_libro = LibroRepositorio(conexion)
# respositorio_libro.crear(rayuela)
rayuela = respositorio_libro.buscar_por_isbn("978-0-2")
print(rayuela.titulo, rayuela.copias_disponibles)
# rayuela.copias_disponibles = 5
# respositorio_libro.actualizar_libro(rayuela)

# respositorio_libro.eliminar("978-0-2")