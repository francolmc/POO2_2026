from database.sqlite_conector import SqliteConector
from database.connection import crear_tablas
from models.socio import Socio
from services.socios_service import SocioService

conector = SqliteConector() # No le entregamos nada, asumimos el valor pode defecto
conexion = conector.obtener_conexion()

crear_tablas(conector)

servicio_socio = SocioService(conexion)

while True:
    print("Menu:")
    print("1- Mostrar los socios")
    print("2- Crear un socio")
    print("3- Editar un socio")
    print("4- Eliminar un socio")
    print("5- Buscar un socio")
    print("6- Salir de la aplicacion")

    opcion = int(input("Ingresar la opcion: "))

    if opcion == 1:
        print("Opcion para mostrar todos los socios")
    elif opcion == 2:
        print("Registro de un socio")
        numero_socio = int(input("Ingrese el numero de socio: "))
        nombre = input("Ingrese el nombre del socio: ")
        socio = Socio(numero_socio, nombre)
        servicio_socio.CrearSocio(socio)
    elif opcion == 3:
        print("Modifcar socio")
        numero_socio = int(input("Ingrese el numero de socio: "))
        nombre = input("Ingrese el nombre del socio: ")
        socio = Socio(numero_socio, nombre)
        servicio_socio.EditarSocio(socio)
    elif opcion == 4:
        print("Opcion para eliminar un socio")
    elif opcion == 5:
        print("Opcion para buscar un socio")
    elif opcion == 6:
        break
    else:
        print("Ingrese una opcion correcta.")