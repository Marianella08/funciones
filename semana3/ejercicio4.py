class Cuenta():
    def __init__(self, titular, cantidad =0) -> None:
        self.titular = titular
        self.cantidad = cantidad
        
    def mostrar(self):
        print(f"En el titular '{self.titular}' tiene: {self.cantidad} en la cuenta")
        
    def ingresar(self, cantidad):
        if cantidad != 0:
         self.cantidad = self.cantidad + cantidad
        else:
            pass
        
    def retirar(self, cantidad):
        self.cantidad = self.cantidad - cantidad
        
mary = Cuenta("Mary",10)
mary.ingresar(10)
mary.retirar(30)
mary.mostrar()