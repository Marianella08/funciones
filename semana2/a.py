cantidad = int(input("ingrese su cantidad de palabras va a tener la lista: "))

lista = []
elista = []

def aceptar_palabras (
    npalabras: int,
    listas: list
):
    for i in range(npalabras):
      a = input(f"ingrese la palabra #{i+1}: ")
      listas.append(a) 
      
def negar_palabras (
    npalabras: int,
    listas: list,
    listas2: list
):
    for i in range(npalabras):
      a = input(f"ingrese la palabra a eliminar #{i+1}: ")
      listas.remove(a) 
      listas2.append(a) 

def mostrar_palabras (

    listas: list,
    listas2: list
):
    print("su lista termina algo asi:")
    print (listas) 
    print("su lista de eliminado termina algo asi:")
    print (listas2) 
      
aceptar_palabras (cantidad, lista)
ecantidad = int(input("ingrese su cantidad de palabras a eliminar de la lista: "))
negar_palabras(ecantidad, lista, elista)
mostrar_palabras(lista, elista)