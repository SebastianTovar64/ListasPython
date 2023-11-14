#EJERCICIO 1
class Figura:
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        # Inicializa los atributos específicos de la clase Rectangulo
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Calcula y devuelve el área del rectángulo
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        # Inicializa el atributo específico de la clase Circulo
        self.radio = radio

    def calcular_area(self):
        # Calcula y devuelve el área del círculo
        return 3.1416 * (self.radio ** 2)

# Crear instancias de las clases Rectangulo y Circulo
rectangulo = Rectangulo(5, 3)
circulo = Circulo(2)

# Imprimir el área de cada figura
print(rectangulo.calcular_area())  # Salida: 15
print(circulo.calcular_area())  # Salida: 12.5664

#EJERCICIO 2
class Fruta:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        pass

class Manzana(Fruta):
    def comer(self):
        return "Comiendo una manzana."

class Naranja(Fruta):
    def comer(self):
        return "Pelando y comiendo una naranja."

class Platano(Fruta):
    def comer(self):
        return "Pelando y comiendo un plátano."

frutas = [Manzana("Sebastian"), Naranja("Laura"), Platano("Marlon")]

for fruta in frutas:
    print(fruta.nombre + ": " + fruta.comer())
