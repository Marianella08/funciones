lista_u = ["David", "Omar"]
lista_p= ["Felipe"]

listasedades1 = [14, 18, 17, 13, 11, 14, 19]
listasedades2 = [15, 12, 16, 9, 18, 20, 20]


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



def agregar2(
    lista: list,
    lista2: list,
    c = "hey"
) -> list:
    personas = lista +lista2
    personas.append(c)
    print(personas)
    
agregar(lista_u, lista_p)


def algun_mayor(
    lista: list,
    lista2: list
) -> list:
    listas = lista +lista2
    mayores = 0
    total = 0
    for i in listas:
        total += 1
        if i >= 18:
         mayores += 1
         
    print(f"En total son {mayores} de edad, de {total} personas en total")

algun_mayor (listasedades1, listasedades2)
    