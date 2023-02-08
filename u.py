def arearectangulo(
    x:float,
    y:float
) -> float:
    """
    función que calcula ela rea de un rectangulo

    ---params---
    - x (float): es la base de mi rectangulo
    - y (float): es la altura de mi rectangulo

    ---return---
    - area (float): es el area de mi rectangulo
    """

    area = x*y
    return area

altura = float(input(" ingresa la altura del rectangulo: "))
base = float(input("ingresa la base del rectangulo: "))
result = arearectangulo(base,altura)
print(f"El area del rectangulo es {result}")