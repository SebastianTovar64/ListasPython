#EJERCICIO 1
class Animal:
    def __init__(self, nombre):
        # Inicializa el atributo 'nombre' del objeto
        self.nombre = nombre

    def hacerSonido(self):
        # Este método no tiene implementación en la clase base Animal
        pass

class Perro(Animal):
    def hacerSonido(self):
        # Implementacion especifica para la clase Perro
        print("Guau")

class Gato(Animal):
    def hacerSonido(self):
        # Implementación especifica para la clase Gato
        print("Miau")

# Crear instancias de las clases Perro y Gato
perro = Perro("Firulais")
gato = Gato("Garfield")

# Llamar al metodo hacerSonido de cada instancia
perro.hacerSonido()  # Salida: Guau
gato.hacerSonido()  # Salida: Miau


#EJERCICIO 2
class Vehiculo:
    def __init__(self, marca):
        # Inicializa el atributo 'marca' del objeto
        self.marca = marca

    def encender_motor(self):
        # Imprime un mensaje indicando que el motor está encendido
        print("Motor encendido.")

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        # Llama al constructor de la clase base Vehiculo
        super().__init__(marca)
        # Inicializa el atributo 'modelo' específico de la clase Coche
        self.modelo = modelo

    def conducir(self):
        # Imprime un mensaje indicando que se está conduciendo el coche
        print(f"Conduciendo {self.marca} {self.modelo}.")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo):
        # Llama al constructor de la clase base Vehiculo
        super().__init__(marca)
        # Inicializa el atributo 'modelo' específico de la clase Motocicleta
        self.modelo = modelo

    def conducir(self):
        # Imprime un mensaje indicando que se está conduciendo la motocicleta
        print(f"Montando {self.marca} {self.modelo}.")

# Crear instancias de las clases Coche y Motocicleta
coche = Coche("Toyota", "Corolla")
motocicleta = Motocicleta("Harley-Davidson", "Sportster")

# Llamar a los métodos de las instancias
coche.encender_motor()  # Salida: Motor encendido.
coche.conducir()  # Salida: Conduciendo Toyota Corolla.

motocicleta.encender_motor()  # Salida: Motor encendido.
motocicleta.conducir()  # Salida: Montando Harley-Davidson Sportster.
