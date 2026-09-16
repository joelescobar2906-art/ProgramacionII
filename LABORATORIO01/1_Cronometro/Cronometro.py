import time

class Cronometro:
    def __init__(self):
        self.__inicia = 0
        self.__finaliza = 0

    def inicia(self):
        self.__inicia = time.time() * 1000

    def detener(self):
        self.__finaliza = time.time() * 1000

    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia

    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza