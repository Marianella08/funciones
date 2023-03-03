class Persona():
    def __init__ (self, nombre,id):
        self.nombre= nombre
        self.id= id
        self.info ={
            "id": self.id,
            "nombre": self.nombre,
            "libros": []
        }
        
    def __str__(self):
        cantidad_libros = len(self.info["libros"])
        return f"{self.id}:{self.nombre} = tiene {cantidad_libros} prestados"
    
    def agregar(self,libro, fecha):
        libro_prestados={
            "nombre": libro,
            "fecha": fecha,
            "Estado": "prestado"
        }
        self.info["libros"].append(libro_prestados)
        
    def agregar(self,libro, fecha):
        libro_prestados={
            "nombre": libro,
            "fecha": fecha,
            "Estado": "prestado"
        }
        self.info["libros"].remove(libro_prestados)
    
    
    def visualizar(self):
        print(self.info["libros"])
    
    def devolver(self, libro):
        for i in self.info["libros"]:
            if i["nombre"] == libro:
                print("si está")
                i["estado"] = "devuelto"
                
        
        
p1 = Persona("1", "juancho")
print(p1)
p1.agregar("1","1")
p1.agregar("2","2")
p1.agregar("3","3")
print(p1)
p1.visualizar()
p1.devolver("1")
p1.visualizar()
