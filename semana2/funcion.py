lista_u = ["David", "Omar"]
lista_p= ["Felipe"]

def agregar(
    lista: list
) -> list:
    persona = input("ingrese un nombre: ")
    lista.append(persona)
    print(lista)
    
def eliminar(
    lista: list
) -> list:
    persona = input("ingrese el nombre a eliminar: ")
    lista.remove(persona)
    print(lista)
    
def visualizar(
    lista: list
) -> list:
    print("tu lista esta así")
    print(lista)

agregar(lista_u)
eliminar(lista_u)
visualizar(lista_u)

agregar(lista_p)
eliminar(lista_p)
visualizar(lista_p)