from funcionesT import *
import time

def programa(personas: dict):
    
    while True:
        print("-"*50)
        print(
        """
        Seleccione la acción deseada:
        1. registrar un nuevo usuario.
        2. actualizar un antiguo usuario.
        3. eliminar un usuario.
        4. visualizar usuarios.
        (x) salir
        """
        )
        seleccion = input("selección: ")
        
        if seleccion == "1":
            agregar_usuario(personas)
            
        if seleccion == "2":
            actualizar_usuario(personas)
        
        if seleccion =="3":
            eliminar_usuario(personas)
            
        if seleccion == "4":
            print(personas)
            time.sleep(1.2)
            
        if seleccion == "x":
            print("-"*50)
            break
        print("-"*50)