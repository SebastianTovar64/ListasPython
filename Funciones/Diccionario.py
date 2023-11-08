# Declaración de un diccionario
diccionario = dict()  # Se crea un diccionario vacío utilizando la función dict()
# Diccionario vacío inicializado con llaves
diccionario = {}  # Otra forma de crear un diccionario vacío utilizando llaves
# Diccionario inicializado con valores
Diccionario = {'nombre': 'Sebastian', 'edad': 17}  # Un diccionario inicializado con pares clave-valor

# Accediendo a los elementos de un diccionario
print(Diccionario['nombre'])  # Imprime el valor asociado a la clave 'nombre'
print(Diccionario.get('nombre', 'No existe'))  # Intenta obtener el valor asociado a 'nombre' o imprime 'No existe' si no existe

# Agregar datos al diccionario después de creado
calificaciones = {
    'nombre': 'Sebastian',
    'notafinal': 5.0
}
calificaciones.update({"Rosa": 3.7, "German": 4.8})  # Agrega nuevos pares clave-valor al diccionario calificaciones

# Técnicas de iteración
calificaciones = {
    'Laura': 5.0,
    'Marlon': 5.0,
    'Nicolas Fierro': 4.5,
    'Dahiana': 2.5
}

print("Iterar por clave")
for i in calificaciones.keys():  # Recorre las claves del diccionario
    print(i)

print("Iterar por valor")
for j in calificaciones.values():  # Recorre los valores del diccionario
    print(j)

nombres = ['Laura', 'Sebastian', 'Nicolas Fierro']
edades = ['16', '17', '60']

for n, e in zip(nombres, edades):  # Combina las listas nombres y edades utilizando zip
    print('Tu nombre es {0} y tu edad {1}.'.format(n, e))  # Imprime los nombres y edades combinados

# Operaciones sobre los diccionarios
dicaleatorio = {x: x**2 for x in (2, 4, 6)}  # Crea un nuevo diccionario con valores al cuadrado

print(dicaleatorio)

# Imprimir números en reversa
print("Números en reversa")
for i in reversed(range(1, 10, 2)):  # Imprime números en orden inverso
    print(i)

# Borrar un elemento del diccionario
del calificaciones['Laura']  # Elimina el elemento con la clave 'Rosa' del diccionario calificaciones

for i, j in calificaciones.items():
    print(i, j)
