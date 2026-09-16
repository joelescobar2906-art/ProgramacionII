import math
class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distancia(self, punto=None, y=None):
        if isinstance(punto, MiPunto):
            x2 = punto.getX()
            y2 = punto.getY()
        else:
            x2 = punto
            y2 = y
        dx = self.__x - x2
        dy = self.__y - y2
        return math.sqrt(dx ** 2 + dy ** 2)
punto1 = MiPunto()
punto2 = MiPunto(10, 30.5)
print("Punto 1:", punto1.getX(), punto1.getY())
print("Punto 2:", punto2.getX(), punto2.getY())
print("Distancia:", punto1.distancia(punto2))
print("Distancia usando coordenadas:", punto1.distancia(10, 30.5))