# Herencia y sobreescritura de metodos.
class Persona:
    def __init__(self, id:int, nombre:str, email:str):
        self.id = id
        self.nombre = nombre
        self.__email = None
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email:str):
        if "@" not in email:
            raise ValueError("El formato del correo no es valido")
        else:
            self.__email =email

    def saluda(self):
        return f"Hola!!! soy {self.nombre}"

# La clase hija Socio hereda de Persona
class Socio(Persona):
    def __init__(self, id, nombre, email, numero_socio):
        # Llamado al constructor de la clase padre de cual heredo
        # Es importante entregar los parametros que requiere el constructor
        # de la clase padre
        super().__init__(id, nombre, email)
        self.numero_socio = numero_socio

    # Polimorfismo: estamos sobreescribiendo el metodo saluda()
    # para que actue segun el socio.
    def saluda(self):
        base = super().saluda() # Reutilizamos el saludo del padre
        return base + ", socio de la biblioteca"


class Bibliotecario(Persona):
    def __init__(self, id, nombre, email, turno):
        super().__init__(id, nombre, email)
        self.turno = turno

    def saluda(self):
        base = super().saluda()
        return base + f", turno {self.turno}"

pedro = Socio(1, 'Pedro Prado', 'pedro@email.com', 12345)
print(pedro.saluda())
juanita = Bibliotecario(1, 'Juanita Rojas', 'juanita@biblio.com', 'tarde')
print(juanita.saluda())