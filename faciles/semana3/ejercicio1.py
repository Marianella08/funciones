class Coche():
    def __init__(self, matricula, marca, kilometros, gasolina) -> None:
        self.matricula = matricula
        self.marca = marca
        self.kilometros = kilometros
        self.gasolina = gasolina
        
    def avanzar(self, km):
        self.gasolina = self.gasolina - km
        self.kilometros  = self.kilometros + km
    
    
        
mary = Coche("URAQT3", "aaa", 10, 25)
mary.avanzar(45)
if mary.gasolina < 0:
        print(f"esa no es gasolina suficiente, te quedaste a los {mary.kilometros + mary.gasolina}")
print(mary.kilometros)
print(mary.gasolina)
