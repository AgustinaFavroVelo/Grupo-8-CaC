import json

# Titulo del programa
print("*" * 20)
print("Gestión de Librería")
print("*" * 20)

# FUNCION PARA OBTENER DATOS DESDE JSON
def obtenerDatos():
    try:
        with open("libros.json", "r") as archivo:
            libreria = json.load(archivo)
    except FileNotFoundError:
        libreria = []
    return libreria

libreria = obtenerDatos()

#ESCRIBO TODAS LAS FUNCIONES ACÁ
# Function : Buscar x titulo
def buscar_por_titulo():
    try:
        titulo = input("Ingrese el titulo del libro: ")
        found= False
        for libro in libreria:
            if libro['titulo'] == titulo: 
                print("Informacion del libro:")
                print("Titulo:", titulo)
                print("Autor:", libro['autor'])
                print("Editorial:", libro['editorial'])
                print("Año de publicación:", libro['año'])
                print("Stock:", libro['stock'])
                found = True
                break
        if not found:
            print("El libro no está en la libreria")
    except:
        print("Aún no se ingresaron libros")

# Function : buscar x autor
def buscar_por_autor():
    autor = input("Ingrese el autor del libro: ")
    libros_encontrados = []

    for libro in libreria:
        if libro['autor'].lower() == autor.lower():
            libros_encontrados.append(libro['titulo'])

    if libros_encontrados:
        print("Libros encontrados por autor", autor + ":")
        for titulo in libros_encontrados:
            print(titulo)
    else:
        print("No se encontraron libros del autor", autor + ".")

# Function : Buscar por editorial
def buscar_por_editorial():
    editorial = input("Ingrese la editorial del libro: ")
    libros_encontrados = []

    for libro in libreria:   
        if libro['editorial'].lower() == editorial.lower():
            libros_encontrados.append(libro['titulo'])

    if libros_encontrados:
        print("Libros encontrados de la editorial", editorial + ":")
        for titulo in libros_encontrados:
            print(titulo)
    else:
        print("No se encontraron libros de la editorial", editorial + ".")

# Function: buscar x año de public.
def buscar_por_año():
    año = int(input("Ingresa el año de publicación del libro: "))
    libros_encontrados = []

    for libro in libreria:
        if libro['año'] == str(año):
            libros_encontrados.append(libro['titulo'])  #agrego titulo del libro a la lsta

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
        'titulo': titulo,
        'autor': autor,
        'editorial': editorial,
        'año': año,
        'stock': stock,
    }
    libreria.append(libro)  #agrego libro (dic) a libreria que es una lista 
    with open('libros.json', 'w') as file:
        json.dump(libreria, file, indent=2)
    print("Libro agregado exitosamente.")

# ELIMINAR LIBRO DE DIC
def eliminar_libro():
    titulo = input("Ingrese el libro que desea eliminar: ")
    found = False

    for libro in libreria:
        if libro['titulo'] == titulo: #si el titulo dle libro coincide con el titulo ingresado
            libreria.remove(libro)   #se remueve/elimina el libro de la libreria
            found = True    #calculo que la bandera es para controlar las iteraciones, no falla
            break

    if found:
        with open('libros.json', 'w') as file:
            json.dump(libreria, file, indent=2)
        print("Libro eliminado exitosamente.")
    else:
        print("El libro no se encontró en la librería.")

# BUSCAR LIBRO
def buscar_libro():
    while True:
        print("""Opciones de busqueda: \n1. Buscar por título \n2. Buscar por autor \n3. Buscar por editorial\n4. Buscar por año de publicación \n5. Salir""")
        opcion = input("Ingresa una opción: ")
        if opcion == '1':
            buscar_por_titulo()
        elif opcion == '2':
            buscar_por_autor()
        elif opcion == '3':
            buscar_por_editorial()
        elif opcion == '4':
            buscar_por_año()
        elif opcion == '5':
            print("Saliendo del menú...")
            break
        else:
            print("Opción invalida. Intente de nuevo.")

#ASI DESPUES LAS LLAMO EN EL MENÚ PPAL
def menu_principal():
    """Muestra menu ppal"""
    while True:
        print("""MENÚ: \n 1. AGREGAR LIBRO \n 2. ELIMINAR LIBRO \n 3. BUSCAR LIBRO \n 4. SALIR""")
        opcion_principal = int(input("Ingrese una opción: "))
        if opcion_principal == 1:
            agregar_libro()
        elif opcion_principal == 2:
            eliminar_libro()
        elif opcion_principal == 3:
            buscar_libro()
        elif opcion_principal == 4:
            print("Saliste del programa")
            break
        else:
            print("Ingresa una opcion valida")
        break

menu_principal()


