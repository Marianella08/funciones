def agregar_usuario(
dataset: dict
) -> dict:
    

    """
    Función para agregar un usuario y su información

    ---params---
    - dataset (dict): el diccionario vacio que tengo

    """
    dato = input("ingrese su nombre de usuario:")
    libro = input("ingrese el nombre del libro:")
    dataset[dato] = libro
    print("el ususario a sido agregado")
    
    
def actualizar_usuario(
    dataset: dict

) -> dict:

    """
    Función para renovar alguna información guardada de acerca de un usuario

    ---params---
    - dataset (dict): el diccionario vacio que tengo

    """
    dato1 = str(input("ingrese el usuario a actualizar: "))
    if dato1 in dataset:
        dato2 = input("ingrese el nuevo dato: ")
        dato3= input("Ahora ingrese el valor de este dato: ")
    dataset.update({dato2: dato3})
    
    
    
def eliminar_usuario(
    dataset: dict

) -> dict:

    """
    Función para eliminar la información guardada de un usuario

    ---params---
    - dataset (dict): el diccionario vacio que tengo

    """
    dato = input("ingrese el usuario a eliminar:")
    dataset.pop(dato)
    print("el dato a sido eliminado")


def visualizar_usuario(
    dataset: dict

) -> dict:

    """
    Función para mostrar la información guardada de acerca de un usuario

    ---params---
    - dataset (dict): el diccionario vacio que tengo

    """

    dato = input("ingrese el usuario que quiere visualizar:")
    x = dataset["dato"]
    print(x)
