class SerVivo():
    sentido_listas = ["olfato", "vista", "tacto", "gusto", "oido"]
    
    def __init__ (self, nombre):
        self.nombre= nombre
        
    def sentidos(self):
        print(self.sentido_listas)
        
    def movimiento(self):
        print(f"{self.nombre} se esta moviendo")
    
    def sonido(self,):
        print(f"{self.nombre} esta haciendo sonido")
        
        
class Persona(SerVivo):
    def movimiento(self):
        print(f"{self.nombre} esta caminando")
        
    def sonido(self):
        print(f"{self.nombre} esta hablando o, tal vez, gritando")

class Gato(SerVivo):
    def movimiento(self):
        print(f"{self.nombre} se esta merodeando")
        
    def sonido(self):
        print(f"{self.nombre} esta maullando")

class Perro(SerVivo):
    def movimiento(self):
        print(f"{self.nombre} se esta trotando")
    
    def sonido(self):
        print(f"{self.nombre} esta ladrando")
        
P = Persona("Albino")
P.movimiento()
P.sonido()
P.sentidos()

g = Gato("Diablo")
g.movimiento()
g.sonido()
g.sentidos()

Pr = Persona("kira")
Pr.movimiento()
Pr.sonido()
Pr.sentidos()