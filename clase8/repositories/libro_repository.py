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

    def buscar_por_isbn(self, isbn:str):
        cursor = self.__conexion.cursor()
        cursor.execute("""
        SELECT isbn, titulo, copias_disponible FROM libros WHERE isbn = ?
        """, (isbn,))
        registro = cursor.fetchone()
        if registro is None:
            return None
        return Libro(registro[0], registro[1], registro[2])

    def actualizar_libro(self, libro:Libro):
        cursor = self.__conexion.cursor()
        cursor.execute("""
        UPDATE libros SET
            titulo = ?,
            copias_disponible = ?
        WHERE
            isbn = ?
        """, (libro.titulo, libro.copias_disponibles, libro.isbn))
        self.__conexion.commit()
        return cursor.rowcount > 0

    def eliminar(self, isbn):
        cursor = self.__conexion.cursor()
        cursor.execute("DELETE FROM libros WHERE isbn = ?", (isbn,))
        self.__conexion.commit()
        return cursor.rowcount > 0
