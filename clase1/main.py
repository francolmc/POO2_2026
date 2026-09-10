# Crear clase Persona
class Persona:
    # Definir constructor
    def __init__(self, id:int, nombre:str, email:str):
        # Definir atributos
        self.id = id
        self.nombre = nombre
        self.email = email

    # Definicion de un metodo, el parametro self es necesario
    # para acceder a los atributos de la clase, como el caso
    # de nombre
    def saluda(self):
        return f"Hola!!! soy {self.nombre}"


# Instanciar o crear un objeto a partir de una clase
pedro = Persona(1, 'Pedro Prado', 'pedro@sucorreo.com')
print(pedro.saluda())
maria = Persona(2, "Maria Castro", 'maria@sucorreo.com')
print(maria.saluda())
rosa = maria # OJO: esto es una referencia
rosa.nombre = "Rosa Rojas"
print(rosa.saluda())
print(maria.saluda())