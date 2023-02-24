from funciones23 import *
import time

def programa(personas):
    while True:
        print("-" * 50)
        print(
            """
            Seleccione una acción.
            1. registrar usuario.
            3. eliminar usuario.
            4. visualizar usuarios
            (x) salir
            """
        )

        seleccion = input("selección: ")
        if seleccion == "1":
            agregar_persona(personas)
        
#        if seleccion == "2":
#            actualizar_persona(personas)
        
        if seleccion =="3":
            eliminar_persona(personas)
            
        if seleccion == "4":
            print(personas)
            time.sleep(1.2)
            
        if seleccion == "x":
            break
        print("-" * 50)