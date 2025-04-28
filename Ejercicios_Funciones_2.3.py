import math

# Función para el área de un rectángulo
def area_rectangulo(a: float, b: float) -> float:
    return a * b

# Función para el área de un círculo
def area_circulo(r: float) -> float:
    return math.pi * (r ** 2)

# Función que suma dos números reales
def suma(x: float, y: float) -> float:
    return x + y


def area_carro(a1: float, b1: float, a2: float, b2: float, r1: float, r2: float) -> float:
    area1 = area_rectangulo(a1, b1)
    area2 = area_rectangulo(a2, b2)
    rueda1 = area_circulo(r1)
    rueda2 = area_circulo(r2)

    area_total = suma(suma(area1, area2), suma(rueda1, rueda2))
    return area_total


a1: float = 4.0
b1: float = 10.0
a2: float = 2.0
b2: float = 6.0
r1: float = 1.5
r2: float = 1.2

area = area_carro(a1, b1, a2, b2, r1, r2)
print(f"El área lateral total del carro es: {area:.2f} m**2")
