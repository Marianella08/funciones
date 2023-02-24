def agregar_persona (
    diccionario : dict
    ) -> dict:
    
    """

    Parametos:
        diccionario (dict): el dicionario en el que se van a guardar los datos

    Returns:
        dict: te devuelve el mismo formato que entregaste en los parametros con la información actualizada
    """
    
    nom = input("ingrese su nombre como usuario: ")
    libro = input("ingrese su libro a prestar:")
    fecha = input("ingrese la fecha de prestamo del libro:")
    
    diccionario_interno = {
        "libro": libro,
        "fecha": fecha
    }
    
    if diccionario.get(nom) != None:
        diccionario[nom].append(diccionario_interno)
    else:
        diccionario[nom] = diccionario_interno
    
    return diccionario


    
def eliminar_persona(
    diccionario : dict
    ) -> dict:
    
    """

    Parametos:
        diccionario (dict): el dicionario en el que se van a guardar los datos

    Returns:
        dict: te devuelve el mismo formato que entregaste en los parametros con la información actualizada
    """
    
    usuario = str (input("ingrese el usuario a eliminar: "))
    diccionario.pop(usuario)
    return diccionario


#def actualizar_persona(
#    dicc:dict
#   ) -> dict:
    
    """

    Parametos:
        diccionario (dict): el dicionario en el que se van a guardar los datos

    Returns:
        dict: te devuelve el mismo formato que entregaste en los parametros con la información actualizada
    """
    nombre:str = str(input('\nIngresa el nombre del usuario que va a prestar el nuevo libro: '))
    libro:str = str(input(f'Ingresa el nuevo libro que presto el usuario {nombre}: '))
    fecha = str(input(f'Ingresa la fecha donde el usuario {nombre} presto el libro {libro}:  '))
    nombre = nombre.title()
    diccionario_interno= {
        "libro":libro,
        "fecha":fecha 
    }
    dicc[nombre].append(diccionario_interno)
    return dicc