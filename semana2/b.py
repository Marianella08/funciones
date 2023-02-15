oracion = input("ingrese una oración: ")
dic_ora = {}
dic_ora[oracion] = []

def añadir(
    palabra: str
):
    dic_ora[oracion].append(
        {
         "palabra": palabra,
         "longitud": len(palabra)
        }
    )
    
for i in oracion.split(" "):
    añadir(i)
    
print(dic_ora)