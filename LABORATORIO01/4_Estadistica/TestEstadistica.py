from Estadistica import Estadistica


datos = list(map(float, input(
    "Ingrese 10 números: "
).split()))

estadistica = Estadistica(datos)

print("El promedio es", estadistica.promedio())
print("La desviación estandard es", estadistica.desviacion())