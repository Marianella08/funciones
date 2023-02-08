import math
def arearectangulo(
    x:float,
    y:float
) -> float:
    """
    función que calcula el area de un rectangulo

    ---params---
    - x (float): es la base de mi rectangulo
    - y (float): es la altura de mi rectangulo

    ---return---
    - area (float): es el area de mi rectangulo
    """

    area = x*y
    return area



def dis_2_pts(
    x1:float,
    x2:float,
    y1:float,
    y2:float
) -> float:
    """
    función que calcula la distancia entre 2 

    ---params---
    - x1 (float): coordeneda X del punto inicial
    - x2 (float): coordeneda y del punto inicial
    - y1 (float): coordeneda X del punto final
    - y2 (float): coordeneda y del punto final

    ---return---
    - d (float): distancias presentes entre ambos puntos
    """

    x = math.pow(x1 -x2,2)
    y = math.pow(y1 -y2,2)
    d = math.sqrt(x+y)
    return d