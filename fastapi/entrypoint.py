from fastapi import FastAPI

app = FastAPI ()

biblioteca = {
    "1":{
        "nombre":"Isa",
        "edad":"15",
        "libros":[
            {
            "libro":"5am",
            "fecha":"13/3/2023",
            "estado":"prestado"
        },
            {
            "libro":"100 años de soledad",
            "fecha":"13/5/2023",
            "estado":"prestado"
        },
        ]
    },
    "2":{
        "nombre":"Mary",
        "edad":"14",
        "libros":[
            {
            "libro":"habtios atomicos",
            "fecha":"13/3/2023",
            "estado":"prestado"
        },
            {
            "libro":"poesia y mitos",
            "fecha":"13/5/2023",
            "estado":"prestado"
        },
        ]
    }
}


# registramos una función en mi app en ruta (endpoint)
# "/" ruta raiz
# Solo podemos tener una función por verbo en una ruta
@app.get("/{nombre}")
def hola(nombre:str):
    return biblioteca[nombre]
