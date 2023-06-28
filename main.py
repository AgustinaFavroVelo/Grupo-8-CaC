import json
from proyecto_libreria import libreria, buscar_libro,  buscar_por_titulo, buscar_por_autor, buscar_por_editorial, buscar_por_año, agregar_libro, eliminar_libro

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