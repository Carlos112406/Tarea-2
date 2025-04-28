import math


def area_vagon(h: float, b: float, r: float) -> float:
    area_rectangulo = h * b
    area_ruedas = 2 * math.pi * (r ** 2)
    area_total = area_rectangulo + area_ruedas
    return area_total


h: float = 5.0   
b: float = 10.0  
r: float = 1.5   

area = area_vagon(h, b, r)
print(f"El area del vagón es: {area:.2f} m**2")
