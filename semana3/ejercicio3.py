class alumno():
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    
    def aprobado(self, nota):
        if nota >= 65 and nota <= 100 :
            print(f"el/la estudiante {self.nombre} a aprobado")
        elif nota <=64 and nota >= 0:
            print(f"el/la estudiante {self.nombre} a reprobado")
        else:
            print(f"{nota} no es una nota valida")
            
juan = alumno("mary")
juan.aprobado(69)

        