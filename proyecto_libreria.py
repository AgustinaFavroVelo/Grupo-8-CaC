import json
import funciones_lib

# FUNCION PARA OBTENER DATOS DESDE JSON
def obtenerDatos():
    try:
        with open("libros.json", "r") as file:
            libreria = json.load(file)
            print (libreria)
    except FileNotFoundError:
        libreria = {}
    return libreria

# Titulo del programa
print("*" * 20)
print("Gestión de Librería")
print("*" * 20)

libreria = obtenerDatos()

def menu_principal():
    """Muestra menu ppal"""
    while True:
        print("""MENÚ: \n 1. AGREGAR LIBRO \n 2. ELIMINAR LIBRO \n 3. BUSCAR LIBRO \n 4. SALIR""")
        opcion_principal = int(input("Ingrese una opción: "))
        if opcion_principal == 1:
            funciones_lib.agregar_libro()
        elif opcion_principal == 2:
            funciones_lib.eliminar_libro()
        elif opcion_principal == 3:
            funciones_lib.buscar_libro()
        elif opcion_principal == 4:
            print("Saliste del programa")
            break
        else:
            print("Ingresa una opcion valida")
        break

menu_principal()