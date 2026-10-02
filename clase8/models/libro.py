class Libro:
    def __init__(self, id:int, isbn:str, titulo:str, copias_disponibles:int):
        self.id = id
        self.isbn = isbn
        self.titulo = titulo
        self.copias_disponibles = copias_disponibles

    def esta_disponible(self):
        if self.copias_disponibles > 0:
            return True
        else:
            return False

# Notese, que aqui no hay ninguna linea de SQL.# Notese, que aqui no hay ninguna linea de SQL.

    def __repr__(self):
        return f"Libro(id={self.id}, isbn='{self.isbn}', titulo='{self.titulo}', copias_disponibles={self.copias_disponibles})"