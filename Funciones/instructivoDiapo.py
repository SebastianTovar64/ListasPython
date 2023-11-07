# Instructivo: Diccionarios y Funciones en Python

#Definición de Diccionarios

#Los diccionarios son estructuras de datos que almacenan informacion en forma de pares clave-valor. Cada clave es unica y se utiliza para acceder al valor asociado. Puedes declarar diccionarios con llaves {} o con la funcion dict().

#Declaración de un Diccionario

#Diccionario vacio inicializado con llaves:
diccionario = {}
calificaciones = {} #lo defini para que no saliera error :)

# Diccionario inicializado con valores:
diccionario = {'nombre': 'Sandra', 'edad': 44}

#Accediendo a los Elementos de un Diccionario

#Puedes acceder a los valores de un diccionario utilizando la clave correspondiente:
print(diccionario['nombre'])
print(diccionario.get('nombre', 'No existe'))
#Agregar Datos a un Diccionario después de Creado

#Puedes agregar datos a un diccionario utilizando el metodo update():
calificaciones.update({"Rosa": 3.7, "German": 4.8})

#Tecnicas de Iteracion en Diccionarios

#Puedes recorrer un diccionario utilizando bucles for y las siguientes tecnicas:

#Iterar por pares clave-valor:
for clave, valor in calificaciones.items():
    print(clave, valor)

#Iterar por claves:

print("Técnicas por clave")
for clave in calificaciones.keys():
    print(clave)

#Iterar por valores:

print("Iterar por valor")
for valor in calificaciones.values():
    print(valor)

#Operaciones en Diccionarios

#Crear un diccionario con comprension:

dicaleatorio = {x: x**2 for x in (2, 4, 6)}

#Imprimir numeros en reversa:

print("Números en reversa")
for i in reversed(range(1, 10, 2)):
    print(i)

#Borrar un elemento del diccionario:

del(calificaciones['Rosa'])

#Definicion de Funciones

#Las funciones en Python permiten agrupar codigo con dos objetivos principales: evitar la repeticion de segmentos de codigo y reutilizar el código en distintas situaciones.

#Estructura de una Funcion

#Definir una funcion:

def saludar():
    print("saludo")

#Definir una funcion con retorno:

def retornarnumero():
    return 1

#Llamar a funciones:

saludar()
numero = retornarnumero()

#Funciones con Parametros

#Puedes definir funciones que tomen argumentos:

def raiz(value):
    return value ** (1/2)

def validarsiexiste(obj):
    if obj:
        print(f"{obj} is True")
    else:
        print(f"{obj} is False")

#Funciones con Parametros Posicionales

#Puedes crear funciones que tomen argumentos de posicion:

def compra(marca, cantidad, valor):
    return {
        'marca': marca,
        'cantidad': cantidad,
        'valor': valor * cantidad
    }


#Funciones con Parametros Nominales

#Tambien puedes utilizar argumentos con nombre al llamar a una funcion:

print(f'Lo comprado fue: {compra(marca="AMD", cantidad=3, valor=2500000)}')

#Parametros por Defecto

#Puedes asignar valores predeterminados a los parametros de una funcion:

def compra(marca, cantidad, valor=2500000):
    return {
        'marca': marca,
        'cantidad': cantidad,
        'valor': valor * cantidad
    }


#Modificando Parametros Mutables

#Hay que tener en cuenta que al modificar parametros mutables, puedes tener efectos inesperados. Para evitarlos, puedes hacer lo siguiente:

def listalimpia(arg, result=None):
    if result is None:
        result = []
    result.append(arg)


#Funciones Anonimas (Lambda)

#Las funciones lambda son pequeñas funciones anonimas con una unica sentencia y retorno implicito. Se utilizan para operaciones simples:

numero_palabras = lambda t: len(t.strip().split())

operadorand = 0 #lo defini para que no saliera error :)

for i in range(2):
    for j in range(2):
        print(f"{i} & {j} = {operadorand(i, j)}")

operadorand = lambda x, y: x & y

