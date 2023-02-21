from basicos.functions import arearectangulo

altura = float(input(" ingresa la altura del rectangulo: "))
base = float(input("ingresa la base del rectangulo: "))
result = arearectangulo(base,altura)
print(f"El area del rectangulo es {result}")
