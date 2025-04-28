# ejercicio 1
def cantidad_carne(N, M, K):
    """
    Calcula la cantidad de carne de aves en kilos.
    N: número de gallinas (6 kg cada una)
    M: número de gallos (7 kg cada uno)
    K: número de pollitos (1 kg cada uno)
    """
    carne_total = (N * 6) + (M * 7) + (K * 1)
    return carne_total


print("Ejercicio 1 - Carne de aves:", cantidad_carne(2, 3, 5))


# ejercicio 2
def calcular_vueltas(B, P, M, H):
    """
    Calcula las vueltas que debe recibir al comprar pan, leche y huevos.
    B: billete entregado
    P: cantidad de panes ($300 cada uno)
    M: cantidad de bolsas de leche ($3300 cada una)
    H: cantidad de huevos ($350 cada uno)
    """
    precio_total = (P * 300) + (M * 3300) + (H * 350)
    vueltas = B - precio_total
    return vueltas


print("Ejercicio 2 - Vueltas:", calcular_vueltas(10000, 2, 1, 5))


# ejercicio 3
def calcular_pago_prestamo(P):
    """
    Calcula cuánto se debe pagar después de dos meses con interés compuesto mensual.
    P: cantidad de pesos prestados
    Interés anual: 3%
    """
    tasa_mensual = 0.03 / 12
    meses = 2
    monto_final = P * (1 + tasa_mensual) ** meses
    return monto_final


print("Ejercicio 3 - Pago préstamo:", calcular_pago_prestamo(10000))


# ejercicio 4
def contagios(C, D):
    """
    Calcula el número de contagiados después de D días.
    C: número actual de contagiados
    Cada día los contagios se duplican
    """
    total_contagiados = C * (2 ** D)
    return total_contagiados


print("Ejercicio 4 - Contagios:", contagios(100, 5))
