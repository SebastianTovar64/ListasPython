# Definición de la función saludar
def saludar():
    print("saludo")

# Definición de la función retornarnumero
def retornarNumero():
    return 1

# Llamada a la función saludar, imprime "saludo" pero no devuelve ningún valor
saludar()

# Llamada a la función retornarnumero, devuelve 1, pero este valor no se imprime
retornarNumero()

# Comprobación de si la función retornarnumero devuelve 1 e imprime un mensaje en consecuencia
if retornarNumero() == 1:
    print("devolvió un uno")
else:
    print("No devolvió un uno")

# Definición de la función raiz que calcula la raíz cuadrada de un número
def raiz(value):
    return value ** (1/2)

# Llamada a la función raiz con el valor 4 e impresión del resultado
print(f'La raíz cuadrada es: {raiz(4)}')

# Definición de la función validarsiexiste que verifica si un objeto es verdadero o falso y muestra un mensaje
def validarSiExiste(obj):
    if obj:
        print(f"{obj} is True")
    else:
        print(f"{obj} is False")

# Llamada a la función validarsiexiste con el argumento 1
validarSiExiste(1)

# Definición de la función f que suma los cuadrados de dos números
def f(x, y):
    return x**2 + y**2

# Llamada a la función f con valores 3 y 5, e impresión del resultado
resultado = f(3, 5)
print(f'El resultado es: {resultado}')

# Definición de la función compra que crea un diccionario con información de una compra
def compra(marca, cantidad, valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Llamada a la función compra con argumentos posicionales y su impresión
print(f'Lo comprado fue: {compra("AMD", 3, 2500000)}')

# Definición de la función compra con parámetros nominales y su llamada
def compra(marca, cantidad, valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Llamada a la función compra con argumentos nominales y su impresión
print(f'Lo comprado fue: {compra(marca="AMD", cantidad=3, valor=2500000)}')

# Definición de la función compra con un parámetro por defecto
def compra(marca, cantidad, valor=2500000):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Llamada a la función compra con valores proporcionados y uno por defecto
print(f'Lo comprado fue: {compra("AMD", 3)}')

# Definición de la función lista que modifica una lista mutable
def lista(arg, result=[]):
    result.append(arg)
    print(result)

# Llamada a la función lista con argumentos y una lista proporcionada como argumento
lista('domingo', [])

# Definición de la función lista_dias_semana que extiende una lista de días de la semana
def listaDiasSemana(result=None):
    if result is None:
        result = []
    result.extend(["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"])
    return result

# Llamada a la función lista_dias_semana para obtener una lista extendida con los días de la semana
result = listaDiasSemana()
print(result)

# Definición de una función lambda (anónima) que cuenta el número de palabras en una cadena
numeroPalabras = lambda t: len(t.strip().split())

# Llamada a la función lambda con una cadena y se imprime el número de palabras
print(numeroPalabras("hola, esto es una prueba con lambda"))

# Definición de una función lambda (anónima) que realiza la operación AND en dos valores
operadorand = lambda x, y: x & y

# Bucle anidado que muestra el resultado de la operación AND entre valores 0 y 1
for i in range(2):
    for j in range(2):
        print(f"{i} & {j} = {operadorand(i, j)}")
