from models.libro import Libro

class LibroRepositorio:
    def __init__(self, conexion):
        self.__conexion = conexion

    def crear(self, libro:Libro):
        cursor = self.__conexion.cursor()
        cursor.execute("""
        INSERT INTO libros VALUES (?, ?, ?)
        """, (libro.isbn, libro.titulo, libro.copias_disponibles,))
        self.__conexion.commit()

    