class SerVivo():
    sentido_listas = ["olfato", "vista", "tacto", "gusto", "oido"]
    
    def __init__ (self, nombre, ejeY=0, ejeX=0):
        self.nombre= nombre
        self.ejeY= ejeY
        self.ejeX= ejeX
        
    def sentidos(self):
        print(self.sentido_listas)
        
    def movimiento(self):
        print(f"{self.nombre} se esta moviendo")
    
    def sonido(self,):
        print(f"{self.nombre} esta haciendo sonido")
        
        
        
    def arriba(self, Y):
        self.ejeY = self.ejeY + Y
        
    def abajo(self, Y):
        self.ejeY = self.ejeY - Y
    
    def izquierda(self, X):
        self.ejeX = self.ejeX - X
    
    def derecha(self, X):
        self.ejeX = self.ejeX + X
        
    def posicion(self):
        print(f"el ejeY es: {self.ejeY}, y el ejeX es: {self.ejeX}")
        
        
class Persona(SerVivo):
    def movimiento(self):
        print(f"{self.nombre} esta caminando")
        
    def sonido(self):
        print(f"{self.nombre} esta hablando o, tal vez, gritando")
        
    def arriba(self, Y):
        self.ejeY = self.ejeY + Y +2
        
    def abajo(self, Y):
        self.ejeY = self.ejeY - Y -2
    
    def izquierda(self, X):
        self.ejeX = self.ejeX - X -2
    
    def derecha(self, X):
        self.ejeX = self.ejeX + X +2
        

class Gato(SerVivo):
    def movimiento(self):
        print(f"{self.nombre} se esta merodeando")
        
    def sonido(self):
        print(f"{self.nombre} esta maullando")
        
    def arriba(self, Y):
        self.ejeY = self.ejeY + Y +3
        
    def abajo(self, Y):
        self.ejeY = self.ejeY - Y -3
    
    def izquierda(self, X):
        self.ejeX = self.ejeX - X -1
    
    def derecha(self, X):
        self.ejeX = self.ejeX + X +1

class Perro(SerVivo):
    def movimiento(self):
        print(f"{self.nombre} se esta trotando")
    
    def sonido(self):
        print(f"{self.nombre} esta ladrando")
        
    def arriba(self, Y):
        self.ejeY = self.ejeY + Y +3
        
    def abajo(self, Y):
        self.ejeY = self.ejeY - Y -3
    
    def izquierda(self, X):
        self.ejeX = self.ejeX - X -3
    
    def derecha(self, X):
        self.ejeX = self.ejeX + X +3
        
P = Persona("Albino")
P.movimiento()
P.sonido()
P.sentidos()
P.arriba(5)
P.posicion()

g = Gato("Diablo")
g.movimiento()
g.sonido()
g.sentidos()
g.arriba(5)
g.posicion()

Pr = Perro("kira")
Pr.movimiento()
Pr.sonido()
Pr.sentidos()
Pr.arriba(5)
Pr.posicion()