class Equipo:
    equipos = {}  # Diccionario de clase para almacenar instancias de equipos.

    def __init__(self, equipoId, cargador, mouse):
        # Constructor de la clase Equipo, inicializa los atributos del equipo.
        self.equipoId = equipoId
        self.cargador = cargador
        self.mouse = mouse
        self.novedades = []  # Lista para almacenar novedades del equipo.
        self.ambientes = []  # Lista para almacenar ambientes del equipo.
        Equipo.equipos[equipoId] = self  # Almacena la instancia en el diccionario de clase.

    def crear_equipo():
        # Metodo estático para crear instancias de equipos.
        equipoId = input("Ingresa el ID del equipo: ")
        if equipoId in Equipo.equipos:
            print("El equipo ya existe.")
            return
        cargador = input("Ingresa el numero del cargador: ")
        mouse = input("Ingresa el numero del mouse: ")
        return Equipo(equipoId, cargador, mouse)

    def agregar_novedad(self, fecha, descripcion):
        # Metodo para agregar una nueva novedad al equipo.
        self.novedades.append({"fecha": fecha, "descripcion": descripcion})

    def mostrar_novedades(self):
        # Metodo para mostrar las novedades del equipo.
        if self.novedades:
            print(f"Novedades del equipo con ID {self.equipoId}:")
            for novedad in self.novedades:
                print(f"Fecha: {novedad['fecha']}, Descripcion: {novedad['descripcion']}")
        else:
            print("No hay novedades para este equipo.")

    def agregar_ambiente(self, ambiente):
        # Metodo para agregar un ambiente a la lista de ambientes del equipo.
        self.ambientes.append(ambiente)

    def mostrar_informacion(self):
        # Metodo para mostrar la información completa del equipo.
        print(f"Informacion del equipo con ID {self.equipoId}:")
        print(f"Cargador: {self.cargador}")
        print(f"Mouse: {self.mouse}")
        self.mostrar_novedades()
        if self.ambientes:
            print("Ambientes:")
            for ambiente in self.ambientes:
                print(ambiente)
        else:
            print("No hay ambientes asignados para este equipo.")


def agregar_equipo():
    equipo = Equipo.crear_equipo()
    if equipo:
        print("Equipo agregado correctamente.")


def agregar_novedad():
    equipoId = input("Ingresa el ID del equipo: ")
    if equipoId not in Equipo.equipos:
        print("El equipo no existe.")
        return
    fecha = input("Ingresa la fecha de la novedad: ")
    descripcion = input("Ingresa la descripcion de la novedad: ")
    Equipo.equipos[equipoId].agregar_novedad(fecha, descripcion)
    print("Novedad agregada correctamente.")


def mostrar_equipos_con_novedades():
    equipos_con_novedades = [equipo for equipo in Equipo.equipos.values() if equipo.novedades]
    if equipos_con_novedades:
        print("Equipos con novedades:")
        for equipo in equipos_con_novedades:
            print(f"ID: {equipo.equipoId}, Cargador: {equipo.cargador}, Mouse: {equipo.mouse}")
    else:
        print("No hay equipos con novedades.")


def eliminar_equipo():
    equipoId = input("Ingresa el ID del equipo a eliminar: ")
    if equipoId not in Equipo.equipos:
        print("El equipo no existe.")
        return
    del Equipo.equipos[equipoId]
    print("Equipo eliminado correctamente.")


def modificar_equipo():
    equipoId = input("Ingresa el ID del equipo a modificar: ")
    if equipoId not in Equipo.equipos:
        print("El equipo no existe.")
        return
    cargador = input("Ingresa el nuevo numero del cargador: ")
    mouse = input("Ingresa el nuevo numero del mouse: ")
    Equipo.equipos[equipoId].cargador = cargador
    Equipo.equipos[equipoId].mouse = mouse
    print("Equipo modificado correctamente.")


def agregar_ambiente():
    equipoId = input("Ingresa el ID del equipo: ")
    if equipoId not in Equipo.equipos:
        print("El equipo no existe.")
        return
    ambiente = input("Ingresa el ambiente a agregar: ")
    Equipo.equipos[equipoId].agregar_ambiente(ambiente)
    print("Ambiente agregado correctamente.")


def mostrar_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Agregar un nuevo equipo")
        print("2. Agregar una nueva novedad")
        print("3. Mostrar equipos con novedades")
        print("4. Eliminar un equipo")
        print("5. Modificar un equipo")
        print("6. Agregar un ambiente a un equipo")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_equipo()
        elif opcion == "2":
            agregar_novedad()
        elif opcion == "3":
            mostrar_equipos_con_novedades()
        elif opcion == "4":
            eliminar_equipo()
        elif opcion == "5":
            modificar_equipo()
        elif opcion == "6":
            agregar_ambiente()
        elif opcion == "7":
            break
        else:
            print("Opcion invalida. Por favor, selecciona una opcion valida.")


mostrar_menu()
