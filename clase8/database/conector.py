from abc import ABC, abstractmethod

class Conector(ABC):
    """
    Esto es un contrato para la conexion con cualquier motor
    de base de datos.
    """
    @abstractmethod
    def obtener_conexion(self):
        pass