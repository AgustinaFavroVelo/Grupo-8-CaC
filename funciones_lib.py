#aca defino todas las funciones que voy a importar
#importo json y las otras funciones que faltan
from general import buscar_por_titulo, buscar_por_autor, buscar_por_editorial, buscar_por_año
import json
import proyecto_libreria

libreria = proyecto_libreria.obtenerDatos()

# AGREGAR LIBRO
def agregar_libro():
    print("Agregar Libro")
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    año = int(input("Ingrese el año de publicacion del libro: "))
    stock = int(input("Ingrese el stock del libro: "))
    libro = {
        'autor': autor,
        'editorial': editorial,
        'año': año,
        'stock': stock,
    }
    libreria.update(libro)
    with open('libros.json', 'w') as file:
        json.dump(libreria, file, indent=2)
    print("Libro agregado exitosamente.")

# Function to read data from a saved file (should be called in the corresponding book search function)
def leer_datos():
    try:
        with open('libros.json', 'r') as archivo:
            libreria = json.load(archivo)
    except FileNotFoundError:
        libreria = {}

# ELIMINAR LIBRO DE DIC
def eliminar_libro():
    titulo = input("Ingrese el libro que desea eliminar: ")
    found = False

    for libro in libreria:
        if libro['titulo'] == titulo:
            libro[titulo].remove('titulo')
            found = True
            break

    if found:
        with open('libros.json', 'w') as file:
            json.dump(libreria, file, indent=2)
        print("Libro eliminado exitosamente.")
    else:
        print("El libro no se encontró en la librería.")

# BUSCAR LIBRO
def buscar_libro():
    opcion = ''
    print("""Menu: \n1. Buscar por título \n2. Buscar por autor \n3. Buscar por editorial\n4. Buscar por año de publicación \n5. Salir""")
    
    while True:
        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            buscar_por_titulo()
        elif opcion == 2:
            buscar_por_autor()
        elif opcion == 3:
            buscar_por_editorial()
        elif opcion == 4:
            buscar_por_año()
        elif opcion == 5:
            print("Saliendo del menú...")
            break
        else:
            print("Opción invalida. Intente de nuevo.")

# MENU PRINCIPAL
def menu_principal():
    print("*" * 20)
    print("Gestión de Librería")
    print("*" * 20)

    libreria = proyecto_libreria.obtenerDatos()

    while True:
        print("""MAIN MENU: \n1. Agregar libro \n2. Eliminar Libro \n3. Buscar libro  \n4. Salir""")
        opcion_principal = int(input("Ingrese su opción: "))

        if opcion_principal == 1:
            agregar_libro()
        elif opcion_principal == 2:
            eliminar_libro()
        elif opcion_principal == 3:
            buscar_libro()
        elif opcion_principal == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Ingrese una opción válida")

menu_principal()