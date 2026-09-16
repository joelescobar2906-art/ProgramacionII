from EcuacionLineal import EcuacionLineal


a, b, c, d, e, f = map(float, input(
    "Ingrese a, b, c, d, e, f: "
).split())

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX())
    print("y =", ecuacion.getY())
else:
    print("La ecuación no tiene solución")