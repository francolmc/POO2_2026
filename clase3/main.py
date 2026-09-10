# Concepto de propiedad
class Persona:
    # Definir constructor
    def __init__(self, id:int, nombre:str, email:str):
        # Definir atributos
        self.id = id
        self.nombre = nombre
        self.__email = None # Definir un atributo como privado
        self.email = email # asignamos el email de forma controlada

    # Definir una propiedad email de lectura
    @property
    def email(self):
        return self.__email

    # Definir la propiedad email de asignacion
    @email.setter
    def email(self, email:str):
        if "@" not in email:
            raise ValueError("El formato del correo no es valido")
        else:
            self.__email =email

    def saluda(self):
        return f"Hola!!! soy {self.nombre}"

pedro = Persona(1, 'Pedro Prado', 'pedro@sucorreo.cl')
print(pedro.email)
pedro.email = "prado@sucorreo.com"
print(pedro.email)