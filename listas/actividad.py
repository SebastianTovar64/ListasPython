# Crear listas para almacenar los datos de los aprendices y sus edades.
aprendices = []
edades = []

# Solicitar los datos de los aprendices y sus edades por teclado y llenar las listas.
n = int(input("¿Cuántos aprendices deseas ingresar? "))
for i in range(n):
    nombre = input("Nombre del aprendiz: ")
    edad = int(input("Edad del aprendiz: "))
    aprendices.append(nombre)
    edades.append(edad)

# Imprimir las listas de aprendices y edades.
print("Lista de Aprendices:", aprendices)
print("Lista de Edades:", edades)

# Encontrar el aprendiz con la mayor edad.
maxEdad = max(edades)
indiceMaxEdad = edades.index(maxEdad)
print(f"El aprendiz con la mayor edad es {aprendices[indiceMaxEdad]} con {maxEdad} años.")

# Insertar el nombre de la instructora en la posición 1.
instructora = input("Ingrese el nombre de la instructora de primero: ")
aprendices.insert(0, instructora)
print(aprendices)


# Contar cuántos aprendices tienen 18 años.
conteoEdad = edades.count(18)
print(f"Hay {conteoEdad} aprendices que tienen 18 años.")

# Agregar un aprendiz 'x' al final de la lista.
aprendices.append("Dahiana")

# Borrar el nombre de la instructora de la lista si existe.
if instructora in aprendices:
    aprendices.remove(instructora)
    print(f"Se eliminó a {instructora} de la lista de aprendices.")
else:
    print(f"{instructora} no se encontró en la lista de aprendices.")
    print(aprendices)

# Indicar un dato a buscar en la lista de aprendices.
datobuscar = input("Ingrese un nombre para buscar en la lista de aprendices: ")
if datobuscar in aprendices:
    print(f"{datobuscar} está en la lista de aprendices.")
else:
    print(f"{datobuscar} no está en la lista de aprendices.")

# Mostrar los primeros 10 aprendices de la lista.
print("Los primeros 10 aprendices son:", aprendices[:10])

# Mostrar los 10 últimos aprendices de la lista.
print("Los 10 últimos aprendices son:", aprendices[-10:])

# Mostrar del elemento 10 al elemento 20 si existen suficientes elementos.
if len(aprendices) >= 20:
    print("Del elemento 10 al elemento 20:", aprendices[9:19])
else:
    print("No hay suficientes elementos para mostrar del 10 al 20.")
