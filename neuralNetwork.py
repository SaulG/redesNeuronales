from numpy import array
from sys import argv
import random

ACTIVACION = 1.0
DESACTIVACION = -1.0
TASA_DE_APRENDIZAJE = 0.05

class Neurona:
    def __init__(self, dim):
        self.w = self.pesos(dim)
        self.e = 0.0
        return

    def entrena(self, entrada, respuestaDeseada):
        global TASA_DE_APRENDIZAJE
        self.calcula(entrada)
        if self.y != respuestaDeseada:
            self.cambio = TASA_DE_APRENDIZAJE * (respuestaDeseada - self.y) * entrada
            self.w += self.cambio
        return

    def pesos(self, dim):
        global ACTIVACION, DESACTIVACION
        lista = list()
        for i in range(dim):
            lista.append(random.uniform(DESACTIVACION, ACTIVACION))
        lista = array(lista)
        return lista

    def calcula(self, entrada):
        global ACTIVACION, DESACTIVACION
        self.x = entrada
        self.a = sum(self.x * self.w)
        if self.a >= 0.0:
            self.y = ACTIVACION
        else:
            self.y = DESACTIVACION
        return self.y

class Capa:
    def __init__(self, tamanio, dim):
        self.neuronas = list()
        for e in xrange(tamanio):
            self.neuronas.append(Neurona(dim + 1)) 
        return

    def calcula(self, entrada):
        self.y = list()
        entrada.append(-1.0)
        entrada = array(entrada)
        for neurona in self.neuronas:
            self.y.append(neurona.calcula(entrada))
        return self.y
    
    def entrena(self, desada, siguiente):
        global TASA_DE_APRENDIZAJE
        if deseada is not None:
            self.e = deseada - self.y
        else:
            self.e = 0.0
            for neurona in siguiente:
                self.e+= neurona.w * neurona.e
                self.w += self.e * self.x * TASA_DE_APRENDIZAJE
        return

class Red:
    def __init__(self, archivo):
        dato = open(archivo,"r")
        d = dato.readlines()
        dato.close()
        dim = int(d.pop(0))
        self.capas = list()
        while len(d) > 0:
            cantidad = int(d.pop(0))
            self.capas.append(Capa(cantidad, dim))
            dim = cantidad
        return

    def calcula(self, entrada):
        for c in self.capas:
            entrada = c.calcula(entrada)
        return entrada

    def entrena(self):
        self.capas[-1].entrena(t,None)
        n = len(self.capas) - 1
        for i in n:
            self.capas[n -i -1].entrena(None, self.capas[n -i])
        return
                                        
def genera(dimension):
    global ACTIVACION, DESACTIVACION
    lista = list()
    for i in range(dimension):
        value = random.uniform(DESACTIVACION, ACTIVACION)
        lista.append(value)
    return lista

def main():
    try:
        red = Red(argv[1])
    except:
        red = Red("configuration.dat")
    for i in xrange(20):
        entrada = genera(4)
        print entrada, red.calcula(entrada)
main()
