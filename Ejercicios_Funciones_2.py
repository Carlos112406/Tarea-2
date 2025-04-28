import math


def volumen_solido(r1: float, r2: float, h: float) -> float:
    volumen_hemisferio = (2/3) * math.pi * (r1 ** 3)
    volumen_cono = (1/3) * math.pi * (r2 ** 2) * h
    volumen_total = volumen_hemisferio + volumen_cono
    return volumen_total


r1: float = 3.0
r2: float = 4.0

# Caso 1: h = 9/2 (como float)
h_decimal: float = 9 / 2
volumen_decimal: float = volumen_solido(r1, r2, h_decimal)
print(f"Volumen con h = 9/2 (float 4.5): {volumen_decimal:.2f}")

# Caso 2: h = 9//2 (como int)
h_entero: int = 9 // 2
volumen_entero: float = volumen_solido(r1, r2, h_entero)
print(f"Volumen con h = 9//2 (entero 4): {volumen_entero:.2f}")

