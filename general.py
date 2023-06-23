import json
import proyecto_libreria

# Cargar data de la libreria
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
        print("No books found from publisher", editorial + ".")

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


while True:
    option = input("Enter an option: ")
        # Search for a book
    print("OPCIONES DE BUSQUEDA:")
    print("1. Buscar por titulo")
    print("2. Buscar por autor")
    print("3. Buscar por editorial")
    print("4. Buscar por año de publicación")
    print("5. Salir del menú")
    search_option = input("Ingrese una opcion de busqueda: ")
        
    if search_option == "1":
        buscar_por_titulo()
    elif search_option == "2":
        buscar_por_autor()
    elif search_option == "3":
        buscar_por_editorial()
    elif search_option == "4":
        buscar_por_año()
    elif option == "5":
        # Exit
        print("saliendo del programa.")
        break
else:
    print("Opción inválida. Intente de nuevo")
