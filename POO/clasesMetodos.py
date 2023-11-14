#EJERCICIO 1
class Persona:
    def __init__(self, nombre, edad):
        # Inicializa los atributos del objeto
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        # Imprime un mensaje de saludo utilizando los atributos del objeto
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona("Sebastian", 17)
# Llama al metodo saludar de la instancia
persona1.saludar()

#EJERCICIO 2
class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        # Llama al constructor de la clase base para inicializar nombre y edad
        super().__init__(nombre, edad)
        # Inicializa el nuevo atributo cargo
        self.cargo = cargo
    
    def trabajar(self):
        # Imprime un mensaje indicando el nombre, edad y cargo del empleado
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años, estoy trabajando como {self.cargo}.")

# Crear una instancia de la clase Empleado
empleado1 = Empleado("Sebastian", 17, "Desarrollador")
# Llama al metodo trabajar de la instancia
empleado1.trabajar()
#init se utiliza para inicializar los atributos del objeto
#self referirse al objeto actual en una clase
