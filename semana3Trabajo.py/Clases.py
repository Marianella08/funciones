class Persona():
    def __init__ (self, nombre,id):
        self.nombre= nombre
        self.id= id
        self.info ={
            "ID": self.id,
            "Nombre": self.nombre,
            "Libros": []
        }
        
    def __str__(self):
        cantidad_libros =len(self.info["libros"])
        return f"{self.id}:{self.nombre} = tiene {cantidad_libros} prestados"
    
    def agregar(self,libro, fecha):
        libro_prestados={
            "Nombre": libro,
            "Fecha": fecha,
            "Estado": "prestado"
        }
        self.info["Libros"].append(libro_prestados)
    
    
    def Visualizar(self):
        print(self.info["libros"])
        
    def Devolver(self, libro):
        for i in self.info["libros"]:
            if i["nombre"] == libro:
                print("si está")
                i["estado"] = "devuelto"
        
        
p1 = Persona("1", "juancho")
print(p1)
p1.agregar_libro("1","1")
p1.agregar_libro("2","2")
p1.agregar_libro("3","3")
print(p1)
p1.visualizar_libros()
p1.devolver_libro("1")
p1.visualizar_libros()
