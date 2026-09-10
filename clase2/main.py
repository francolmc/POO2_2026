# Concepto de encapsulamiento
class Persona:
    # Definir constructor
    def __init__(self, id:int, nombre:str, email:str):
        # Definir atributos
        self.id = id
        self.nombre = nombre
        self.__email = None # Definir un atributo como privado
        self.asignar_email(email) # asignamos el email de forma controlada

    # Metodo para manipular valor de __email (atributo privado)
    def asignar_email(self, email:str):
        if "@" not in email:
            raise ValueError("El formato del correo no es valido")
        else:
            self.__email =email

    # Este metodo me permite mostrar el valor de __email (atibuto privado)
    def obtener_email(self):
        return self.__email

    def saluda(self):
        return f"Hola!!! soy {self.nombre}"

pedro = Persona(1, 'Pedro Prado', 'pedrosucorreo.cl')
print(pedro.obtener_email())