# Generar una clase una clase inventario que pueda recibir items o agregar items
# donde contenga un metodo que muestre lo que los items hacen.
# Considerar una clase Item y sub-clases a partir de ella.
# Como por ejemplo: Arma, Pocion, Armadura, etc.
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, descripcion:str, nivel:int):
        super().__init__()
        self.descripcion = descripcion
        self.nivel = nivel

    @abstractmethod
    def mostrar(self):
        pass

class Arma(Item):
    def __init__(self, descripcion, nivel):
        super().__init__(descripcion, nivel)

    def mostrar(self):
        return f"Soy un Arma, especificamente: {self.descripcion}"

class Pocion(Item):
    def __init__(self, descripcion, nivel):
        super().__init__(descripcion, nivel)

    def mostrar(self):
        return f"Soy una Poción, especificamente: {self.descripcion}"

class Armadura(Item):
    def __init__(self, descripcion, nivel):
        super().__init__(descripcion, nivel)

    def mostrar(self):
        return f"Soy una Armadura, especificamente: {self.descripcion}"

class Inventario:
    def __init__(self):
        self.__lista_items = []

    def agregar_item(self, item:Item):
        self.__lista_items.append(item)

    def mostrar_contenido(self) -> list:
        return self.__lista_items


# Usar las clases y generar el comportamiento de tener items y agregar a mi inventario.
# Items disponibles
armadura = Armadura('Armadura nivel 2', 100)
pocion = Pocion('Pocion nivel 2, para restaurar el 50%', 50)
arma = Arma("Arma nivel 4, nivel de daño 25%", 25)

# Crear mi inventario y agregar items
mi_inventario = Inventario()
mi_inventario.agregar_item(armadura)
mi_inventario.agregar_item(pocion)
mi_inventario.agregar_item(arma)

# Mostrar los items de mi invetario
contenido = mi_inventario.mostrar_contenido()
for item in contenido:
    print(item.mostrar())
