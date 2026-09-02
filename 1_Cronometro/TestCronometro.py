from Cronometro import Cronometro

def ordenacion_seleccion(lista):
    for i in range(len(lista)):
        minimo = i

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]


numeros = list(range(1000, 0, -1))

cronometro = Cronometro()

cronometro.inicia()

ordenacion_seleccion(numeros)

cronometro.detener()

print("Tiempo de ejecución:", cronometro.lapsoDeTiempo(), "milisegundos")