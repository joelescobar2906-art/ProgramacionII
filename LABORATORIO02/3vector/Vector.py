import math
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, otro):
        return Vector(
            self.x + otro.x,
            self.y + otro.y,
            self.z + otro.z
        )
    def __mul__(self, valor):
        if isinstance(valor, Vector):
            return self.x * valor.x + self.y * valor.y + self.z * valor.z
        return Vector(
            self.x * valor,
            self.y * valor,
            self.z * valor
        )
    def __rmul__(self, valor):
        return self * valor
    def longitud(self):
        return math.sqrt(
            self.x ** 2 +
            self.y ** 2 +
            self.z ** 2
        )
    def normal(self):
        largo = self.longitud()
        return Vector(
            self.x / largo,
            self.y / largo,
            self.z / largo
        )
    def producto_vectorial(self, otro):
        x = self.y * otro.z - self.z * otro.y
        y = self.z * otro.x - self.x * otro.z
        z = self.x * otro.y - self.y * otro.x
        return Vector(x, y, z)
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
print("Vector a:", a)
print("Vector b:", b)
print("Suma:", a + b)
print("Multiplicación por escalar:", 2 * a)
print("Longitud de a:", a.longitud())
print("Normal de a:", a.normal())
print("Producto escalar:", a * b)
print("Producto vectorial:", a.producto_vectorial(b))