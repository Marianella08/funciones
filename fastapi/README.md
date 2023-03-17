# FASTAPI
## creacion del entorno virtual
1. instalar la libreria del entorno virtual ````pip install virtualenv````
2. creacion de entorno virtula `````python -m virtualenv [NOMBRE]````
3. verificamos el python general ````pip freeze```` deben salir varias librerias
4. entro a mi entorno virtual (en WINDOWS desde GIT-BASH) ````source venv/Script/activate```` y sale el nombre de mi entorno virtual en mi linea de comandos

## Instalar FastAPI
1. instalación de FastAPI ```` pip install fastapi uvicorn````

## Creación de shemas
```python
from pydantic import BaseModel

class PersonaCreate(BaseModel):
    nombre :str
    edad: str
    ocupacion:str