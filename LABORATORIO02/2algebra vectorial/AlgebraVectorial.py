import math
class AlgebraVectorial:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def producto_escalar(self):
        resultado = 0
        for i in range(len(self.a)):
            resultado = resultado + self.a[i] * self.b[i]
        return resultado
    def longitud(self, vector):
        suma = 0
        for numero in vector:
            suma = suma + numero ** 2
        return math.sqrt(suma)
    def perpendicular(self):
        producto = self.producto_escalar()
        return producto == 0
    def perpendicular_por_distancia(self):
        suma = []
        for i in range(len(self.a)):
            suma.append(self.a[i] + self.b[i])
        resta = []
        for i in range(len(self.a)):
            resta.append(self.a[i] - self.b[i])
        return self.longitud(suma) == self.longitud(resta)
    def paralela(self):
        for i in range(len(self.a)):
            for j in range(i + 1, len(self.a)):
                if self.a[i] * self.b[j] != self.a[j] * self.b[i]:
                    return False
        return True
    def proyeccion(self):
        producto = self.producto_escalar()
        longitud_b = self.longitud(self.b)
        resultado = []
        for numero in self.b:
            valor = (producto / longitud_b ** 2) * numero
            resultado.append(valor)
        return resultado
    def componente(self):
        producto = self.producto_escalar()
        longitud_b = self.longitud(self.b)

        return producto / longitud_b
a = [2, 3]
b = [3, -2]
algebra = AlgebraVectorial(a, b)
print("Vector a:", a)
print("Vector b:", b)
print("¿Son perpendiculares?", algebra.perpendicular())
print("¿Son perpendiculares usando longitudes?",
      algebra.perpendicular_por_distancia())
print("¿Son paralelos?", algebra.paralela())
print("Proyección de a sobre b:", algebra.proyeccion())
print("Componente de a en b:", algebra.componente())