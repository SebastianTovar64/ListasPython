# Creamos un diccionario vacio llamado "equipos" para almacenar informacion de los equipos y sus novedades.
equipos = {}

# La funcion "agregarEquipo" permite agregar un equipo al diccionario "equipos" con su ID, cargador y mouse.
def agregarEquipo():
    equipoId = input("Ingresa el ID del equipo: ")
    if equipoId in equipos:
        print("El equipo ya existe.")
        return
    cargador = input("Ingresa el numero del cargador: ")
    mouse = input("Ingresa el numero del mouse: ")
    equipos[equipoId] = {"cargador": cargador, "mouse": mouse, "novedades": []}
    print("Equipo agregado con exito.")

# La funcion "agregarNovedad" permite agregar una novedad a un equipo existente, especificando fecha y descripcion.
def agregarNovedad():
    equipoId = input("Ingresa el ID del equipo: ")
    if equipoId in equipos:
        fecha = input("Ingresa la fecha de la novedad: ")
        descripcion = input("Ingresa una descripcion de la novedad: ")
        equipos[equipoId]["novedades"].append({"fecha": fecha, "descripcion": descripcion})
        print("Novedad agregada con exito.")
    else:
        print("Equipo no encontrado.")

# La funcion "buscarEquipo" permite buscar un equipo por su ID y muestra su informacion, incluyendo novedades si las tiene.
def buscarEquipo():
    equipoId = input("Ingresa el ID del equipo que deseas buscar: ")
    if equipoId in equipos:
        equipo = equipos[equipoId]
        print(f"Informacion del equipo con ID {equipoId}:")
        print(f"Cargador: {equipo['cargador']}")
        print(f"Mouse: {equipo['mouse']}")
        if equipo['novedades']:
            print("Novedades:")
            for novedad in equipo['novedades']:
                print(f"Fecha: {novedad['fecha']}, Descripcion: {novedad['descripcion']}")
        else:
            print("No hay novedades para este equipo.")
    else:
        print("Equipo no encontrado.")

# La funcion "mostrarEquiposConNovedades" muestra una lista de equipos que tienen novedades registradas.
def mostrarEquiposConNovedades():
    equiposNovedades = [equipo for equipo in equipos.values() if equipo['novedades']]
    if equiposNovedades:
        print("Equipos con novedades:")
        for equipoId in equiposNovedades:
            equipo = equipos[equipoId]
            print(f"Equipo ID: {equipoId}")
            print(f"Cargador: {equipo['cargador']}")
            print(f"Mouse: {equipo['mouse']}")
            print("Novedades:")
            for novedad in equipo['novedades']:
                print(f"Fecha: {novedad['fecha']}, Descripcion: {novedad['descripcion']}")
            print()
    else:
        print("No hay equipos con novedades.")

# Este bucle permite al usuario seleccionar acciones como agregar equipo, agregar novedad, buscar equipo, mostrar equipos con novedades y salir.
while True:
    print("\nOpciones:")
    print("1. Agregar equipo")
    print("2. Agregar novedad")
    print("3. Buscar equipo por ID")
    print("4. Mostrar equipos con novedades")
    print("5. Salir")
    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        agregarEquipo()
    elif opcion == "2":
        agregarNovedad()
    elif opcion == "3":
        buscarEquipo()
    elif opcion == "4":
        mostrarEquiposConNovedades()
    elif opcion == "5":
        break
    else:
        print("Opcion no valida. Por favor, selecciona una opcion valida.")
