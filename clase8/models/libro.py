class Libro:
    def __init__(self, isb:str, titulo:str, copias_disponibles:int):
        self.isbn = isb
        self.titulo = titulo
        self.copias_disponibles = copias_disponibles

    def esta_disponible(self):
        if self.copias_disponibles > 0:
            return True
        else:
            return False

# Notese, que aqui no hay ninguna linea de SQL.