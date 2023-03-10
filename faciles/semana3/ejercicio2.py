class Robot():
    def __init__ (self, ejeY =0, ejeX =0):
        self.ejeY= ejeY
        self.ejeX= ejeX
        
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
        
tobor = Robot()
tobor.arriba(5)
tobor.posicion()