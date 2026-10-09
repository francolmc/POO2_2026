from models.socio import Socio
from repositories.socio_repository import SocioRepository

class SocioService:
    def __init__(self, conexion):
        self.__conexion = conexion
        self.__respositorio = SocioRepository(conexion)

    def CrearSocio(self, socio: Socio):
        try:
            socio_buscado = self.__respositorio.buscar_por_numero_socio(socio.numero_socio)
            if socio_buscado is None:
                self.__respositorio.crear(socio)
            else:
                print("Error: el socio con ese numero ya existe.")
        except:
            print("Los datos no son correctos.")

    def EditarSocio(self, socio: Socio):
        try:
            socio_buscado = self.__respositorio.buscar_por_numero_socio(socio.numero_socio)
            if socio_buscado:
                if socio.numero_socio is None:
                    socio.numero_socio = socio_buscado.numero_socio
                if socio.nombre is None:
                    socio.nombre = socio_buscado.nombre
                self.__respositorio.actualizar_socio(socio)
            else:
                print("Error: el socio a editar no existe.")
        except:
            print("Los datos no son correctos.")

    def MostrarTodos(self):
        try:
            socios = self.__respositorio.todos()
            return socios
        except:
            print("Hay problemas con la base de datos")

    def buscar_por_nombre(self, nombre: str):
        try:
            socios = self.__respositorio.buscar_por_nombre(nombre)
            return socios
        except:
            print("Hay problemas con la base de datos")