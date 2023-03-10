class Triangulo():
    def __init__(self, nombre) -> None:
        self.nombre= nombre
        self.lado1 = int(input("ingrese el lado a:"))
        self.lado2 = int(input("ingrese el lado b:"))
        self.lado3 = int(input("ingrese el lado c:"))
        self.lados = [self.lado1, self.lado2, self.lado3]
        
        
    def ladoMayor(self):
        mayor = max(self.lados)
        print(f"la mayor longitud es {mayor}")
        
    def tipo_triangulo(self):
        conjunto_lados = set(self.lados)
        if len(conjunto_lados) == 3:
            print(f"{self.nombre} es un triangulo escaleno")
        elif len(conjunto_lados) == 2:
            print(f"{self.nombre} es un triangulo isoseles")
        else:
            print(f"{self.nombre} es un triangulo equilatero")



tri = Triangulo("Trilito")
tri.ladoMayor()
tri.tipo_triangulo()

        