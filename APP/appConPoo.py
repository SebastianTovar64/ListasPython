class Equipo:
    def __init__(self, equipoId, cargador, mouse):
        # Constructor de la clase Equipo, inicializa los atributos del equipo.
        self.equipoId = equipoId
        self.cargador = cargador
        self.mouse = mouse
        self.novedades = []  # Lista para almacenar novedades del equipo.
        self.ambientes = []  # Lista para almacenar ambientes del equipo.

    def agregar_novedad(self, fecha, descripcion):
        # Metodo para agregar una nueva novedad al equipo.
        self.novedades.append({"fecha": fecha, "descripcion": descripcion})

    def mostrar_novedades(self):
        # Método para mostrar las novedades del equipo.
        if self.novedades:
            print(f"Novedades del equipo con ID {self.equipoId}:")
            for novedad in self.novedades:
                print(f"Fecha: {novedad['fecha']}, Descripción: {novedad['descripcion']}")
        else:
            print("No hay novedades para este equipo.")

    def agregar_ambiente(self, ambiente):
        # Metodo para agregar un ambiente a la lista de ambientes del equipo.
        self.ambientes.append(ambiente)

    def mostrar_informacion(self):
        # Metodo para mostrar la informacion completa del equipo.
        print(f"Información del equipo con ID {self.equipoId}:")
        print(f"Cargador: {self.cargador}")
        print(f"Mouse: {self.mouse}")
        self.mostrar_novedades()
        if self.ambientes:
            print("Ambientes:")
            for ambiente in self.ambientes:
                print(ambiente)
        else:
            print("No hay ambientes asignados para este equipo.")


equipos = {}  # Diccionario para almacenar todos los equipos.

def agregar_equipo():
    # Funcion para agregar un nuevo equipo al diccionario 'equipos'.
    equipoId = input("Ingresa el ID del equipo: ")
    if equipoId in equipos:
        print("El equipo ya existe.")
        return
    cargador = input("Ingresa el número del cargador: ")
    mouse = input("Ingresa el número del mouse: ")
    equipos[equipoId] = Equipo(equipoId, cargador, mouse)
    print("Equipo agregado con éxito.")

def agregar_novedad():
    # Funcion para agregar una novedad a un equipo existente.
    equipoId = input("Ingresa el ID del equipo: ")
    if equipoId in equipos:
        fecha = input("Ingresa la fecha de la novedad: ")
        descripcion = input("Ingresa una descripción de la novedad: ")
        equipos[equipoId].agregar_novedad(fecha, descripcion)
        print("Novedad agregada con éxito.")
    else:
        print("Equipo no encontrado.")

def buscar_equipo():
    # Funcion para buscar un equipo por su ID y mostrar su informacion.
    equipoId = input("Ingresa el ID del equipo que deseas buscar: ")
    if equipoId in equipos:
        equipos[equipoId].mostrar_informacion()
    else:
        print("Equipo no encontrado.")

def mostrar_equipos_con_novedades():
    # Funcion para mostrar la informacion de equipos que tienen novedades.
    equipos_novedades = [equipoId for equipoId, equipo in equipos.items() if equipo.novedades]
    if equipos_novedades:
        print("Equipos con novedades:")
        for equipoId in equipos_novedades:
            equipos[equipoId].mostrar_informacion()
            print()
    else:
        print("No hay equipos con novedades.")

def eliminar_equipo():
    # Funcion para eliminar un equipo del diccionario 'equipos'.
    equipoId = input("Ingresa el ID del equipo que deseas eliminar: ")
    if equipoId in equipos:
        del equipos[equipoId]
        print("Equipo eliminado con éxito.")
    else:
        print("Equipo no encontrado.")

def modificar_equipo():
    # Funcion para modificar ciertos atributos de un equipo existente.
    equipoId = input("Ingresa el ID del equipo que deseas modificar: ")
    if equipoId in equipos:
        equipo = equipos[equipoId]
        campo = input("Ingresa el campo que deseas modificar (cargador, mouse): ")
        nuevoValor = input("Ingresa el nuevo valor del campo: ")
        setattr(equipo, campo, nuevoValor)
        print("Equipo modificado con éxito.")
    else:
        print("Equipo no encontrado.")

def agregar_ambiente():
    # Funcion para agregar un ambiente a la lista de ambientes de un equipo.
    equipoId = input("Ingresa el ID del equipo al que deseas agregar un ambiente: ")
    if equipoId in equipos:
        equipo = equipos[equipoId]
        ambiente = input("Ingresa el ambiente que deseas agregar: ")
        equipo.agregar_ambiente(ambiente)
        print("Ambiente agregado con éxito.")
    else:
        print("Equipo no encontrado.")

# Bucle principal del programa
while True:
    print("\nOpciones:")
    print("1. Agregar equipo")
    print("2. Agregar novedad")
    print("3. Buscar equipo por ID")
    print("4. Mostrar equipos con novedades")
    print("5. Eliminar Equipo")
    print("6. Modificar equipo")
    print("7. Agregar a qué ambiente pertenece")
    print("8. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_equipo()
    elif opcion == "2":
        agregar_novedad()
    elif opcion == "3":
        buscar_equipo()
    elif opcion == "4":
        mostrar_equipos_con_novedades()
    elif opcion == "5":
        eliminar_equipo()
    elif opcion == "6":
        modificar_equipo()
    elif opcion == "7":
        agregar_ambiente()
    elif opcion == "8":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
