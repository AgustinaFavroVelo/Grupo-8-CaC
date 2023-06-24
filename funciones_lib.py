#aca defino todas las funciones que voy a importar
#importo json y el main
import json
import proyecto_libreria

libreria = proyecto_libreria.obtenerDatos()

# Function : Buscar x titulo
def buscar_por_titulo():
    try:
        titulo = input("Ingrese el titulo del libro: ")
        if titulo in libreria:
            libro = libreria [titulo]
            print("Informacion del libro:")
            print("Titulo:", titulo)
            print("Autor:", libro['autor'])
            print("Editorial:", libro['editorial'])
            print("Año de publicación:", libro['año'])
            print("Stock:", libro['stock'])
        else:
            print("El libro no está en la librería.")
    except:
        print("Aún no se ingresaron libros")

# Function : buscar x autor
def buscar_por_autor():
    autor = input("Ingrese el autor del libro: ")
    libros_encontrados = []

    for titulo, libro in libreria.items():
        if libro['autor'] == autor:
            libros_encontrados.append(titulo)

    if libros_encontrados:
        print("Libros encontrados por autor", autor + ":")
        for titulo in libros_encontrados:
            print(titulo)
    else:
        print("No se encontraron libros del autor", autor + ".")

# Function : Buscar por editorial
def buscar_por_editorial():

    editorial = input("Ingrese el año de publicación: ")
    libros_encontrados = []

    for titulo, libro in libreria.items():   
        if libro['editorial'] == editorial:
            libros_encontrados.append(titulo)

    if libros_encontrados:
        print("Libros encontrados de la editorial", editorial + ":")
        for titulo in libros_encontrados:
            print(titulo)
    else:
        print("No se encontraron libros de la editorial", editorial + ".")

# Function: buscar x año de public.
def buscar_por_año():
    año = int(input("Enter the publication year of the book: "))
    libros_encontrados = []

    for titulo, libro in libreria.items():
        if libro['año'] == str(año):
            libros_encontrados.append(titulo)

    if libros_encontrados:
        print("Libros publicados en el año", año, ":")
        for titulo in libros_encontrados:
            print(titulo)
    else:
        print("No se encontraron libros publicados en", año)

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
        print("OPCIONES DE BUSQUEDA:")
        print("1. Buscar por titulo")
        print("2. Buscar por autor")
        print("3. Buscar por editorial")
        print("4. Buscar por año de publicación")
        print("5. Salir del menú")
        opcion = input("Ingrese una opcion de busqueda: ")

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