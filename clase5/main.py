
# Clase abstracta
# Para definir una clase abstracta debo importar la libreria para ello
from abc import ABC, abstractmethod

# De este modo defino que Item será una clase abstracta
class Item(ABC):
    def __init__(self, descripcion:str, nivel:int):
        super().__init__()
        self.descripcion = descripcion
        self.nivel = nivel

    @abstractmethod
    def mostrar(self):
        pass
