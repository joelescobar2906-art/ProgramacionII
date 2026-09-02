import math
class Estadistica:

    def __init__(self, datos):
        self.__datos = datos

    def promedio(self):
        suma = 0

        for dato in self.__datos:
            suma += dato

        return suma / len(self.__datos)

    def desviacion(self):
        prom = self.promedio()
        suma = 0

        for dato in self.__datos:
            suma += (dato - prom) ** 2

        return math.sqrt(suma / (len(self.__datos) - 1))