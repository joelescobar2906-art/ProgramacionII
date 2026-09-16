import math
def promedio(datos):
    suma = 0

    for dato in datos:
        suma += dato

    return suma / len(datos)
def desviacion(datos):
    prom = promedio(datos)
    suma = 0

    for dato in datos:
        suma += (dato - prom) ** 2

    return math.sqrt(suma / (len(datos) - 1))

datos = list(map(float, input(
    "Ingrese 10 números: "
).split()))
print("El promedio es", promedio(datos))
print("La desviación estandard es", desviacion(datos))