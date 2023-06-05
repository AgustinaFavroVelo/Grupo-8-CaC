#primero, poner la libreria online (diccionario) vacía
libreria={}
#organizar con funciones las 3 opciones principales: agregar libro, eliminar libro y buscar libro
def menu_principal():
    """Mostrar manú principal"""
    opcion_principal =" "
    print ("""MENÚ PRINCIPAL: \n 1.AGREGAR LIBRO \n 2.ELIMINAR LIBRO \n 3.BUSCAR LIBRO \n 4.SALIR""")
    while opcion_principal !=4:
        if opcion_principal == 1:
            agregar_libro()                   #abajo estan todas las funciones que llamé acá
        elif opcion_principal ==2:
            eliminar_libro()
        elif opcion_principal ==3:
            buscar_libro()
        else:
            print( "Ingrese una opción válida")
        break
menu_principal()

#FUNCION AGREGAR LIBRO AL DICCIONARIO           
def agregar_libro():
    titulo= input("Ingrese el título del libro: ")
    autor= input("Ingrese el/la autor/a del libro: ")
    editorial= input("Ingrese la editorial del libro: ")
    año= input("Ingrese año de publicación del libro: ")
    stock= input("Ingrese la cantidad de libros en stock: ")
    #se crea una clave para el valor ingresado por input y se guarda asi dentro del dic "libro".
    libro= {
    'autor': autor,
    'editorial': editorial,
    'año': año,
    'stock': stock,
    }
    libreria[titulo]= libro #la libreria ahora tiene un nuevo libro 
    print("Libro agregado correctamente.")

#FUNCION ELIMINAR LIBRO
def eliminar_libro():
    titulo= input("Ingrese el título del libro que desea eliminar: ")
    if titulo in libreria: #si el titulo que se ingresó esta en la libreria:
        del libreria[titulo] #se elimina el libro que tiene ese nombre
        print("Libro eliminado correctamente.")
    else: 
        print("El libro no está en la librería.")

#FUNCION BUSCAR LIBRO
def buscar_libro():
    opcion= ''
    print("""Menú de busqueda: n\ 1. Buscar libro por título n\ 2. Buscar libro por autor/a n\ 3. Buscar libro por editorial n\ 4. Buscar libro por año de publicación n\ 5. Salir """)
    while opcion !=5: #mientras la opción no sea 5, entonces...
        opcion = int(input("Ingrese una opcion: "))
    if opcion ==1:
        buscar_por_titulo()  #se invocan las funciones que vamos a definir después, mas abajito
    elif opcion ==2:
        buscar_por_autor()
    elif opcion==3:
        buscar_por_editorial()
    elif opcion ==4:
        buscar_por_año()
    elif opcion==5:
        print("Saliendo del menú de búsqueda...")
    else:
        print("Opción inválida. Por favor ingrese una opción válida")
    #OPCION 1: por titulo
    def buscar_por_titulo():
        titulo= input("Ingrese el título del libro: ")
        if titulo in libreria:
            print("Información del libro:")
            print("Titulo:", titulo, 
                  "Autor/a:", libreria[titulo['autor']],  #llamo y escribo el autor dentro del titulo dentro de libreria
                  "Editorial:" , libreria[titulo['editorial']],
                  "Año de publicación:", libreria[titulo['año']],
                  "stock:", libreria[titulo['stock']]
                  )
        else:
            print("El libro no está en la librería")
    #OPCION 2: por autor
    def buscar_por_autor():
        autor= input("Ingrese el/la autor/a del libro: ")
        libros_encontrados=[]
        for titulo, libro in libreria.items():
            if libro['autor'] == autor:
                libros_encontrados.append(titulo) #para agregar info a lista
        if libros_encontrados:
            print("Libro encontrado por autor/a" + autor + ".")
            for titulo in libros_encontrados:
                print('-', titulo)
        else: 
            print("No se encontraron los libros del autor/a" +autor+ ".")
    #OPCION 3: por editorial
    def buscar_por_editorial():
        editorial= input("Ingrese la editorial del libro: ")
        libros_encontrados= []
        for titulo, libro in libreria.items():
            if libro['editorial'] == editorial:
                libros_encontrados.append(titulo) #agrego este titulo que se encuentra por autor a la lista
        if libros_encontrados:
            print("Estos son los libros encontrados de la editorial " +editorial+ ".")
            for titulo in libros_encontrados:
                print("-" , titulo)
        else:
            print("No se encontraron libros de la editorial " +editorial + ".")
    #OPCION 4: por año de publicacion
    def buscar_por_año():
        año= input("Ingrese año de publicación del libro: ")
        libros_encontrados=[]
        for libro in libreria.items():
            if libro['año'] == año:
                libros_encontrados.append(año) #agrego este titulo que se encuentra por año a la lista
        if libros_encontrados:
            print("Estos son los libros encontrados por año de publicacion " +año + ".")
            for titulo in libros_encontrados:
                print("-", titulo)
    print("Decidiste salir del programa")
