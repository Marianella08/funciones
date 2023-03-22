#Toco exponer la biblioteca ayudad ;)

from fastapi import FastAPI
from pydantic import BaseModel

class personaBiblioteca(BaseModel):
    id:str
    nombre:str
    edad:int
    

class personaModificar(BaseModel):
    id:str
    nombre:str
    edad:int
    libros:dict

app = FastAPI ()

biblioteca = [
{
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
]

# registramos una función en mi app en ruta (endpoint)
# "/" ruta raiz
# Solo podemos tener una función por verbo en una ruta
#@app.get("/")
def hello_world_check(nombre:str):
    return {
        "titulo": "biblioteca Steam",
        "version": "v0.0.1"
    }
    
#@app.get("/personas")
def personas_all():
    return biblioteca


#@app.get("/personas/{id}")
def personas_one(id:str):
    return biblioteca[id]


#@app.post("/personas")
def personas_add(request:personaBiblioteca):
    biblioteca.append(request)
    return request


#@app.put("/personas")
def personas_modify(request:personaModificar):
    for i in biblioteca:
        print(i)
        if i.id == request.id:
            i.nombre = request.nombre
            i.edad = request.edad
            return 1
    return {"error": "Persona no encontrada"}


#@app.delete("/personas/{id}")
def personas_delete(id:str):
    for i in biblioteca:
        if i.id == id:
            print (i.id)
            return i
    return {"error": "persona no encontrada"}