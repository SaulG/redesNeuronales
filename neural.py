from numpy import array
from sys import argv
import random

ACTIVACION = 1.0
DESACTIVACION = -1.0

class Neurona:
    def __init__(self, dim):
        self.w = self.pesos(dim)

    def calcula(self, entrada):
        global ACTIVACION, DESACTIVACION
        self.x = entrada
        self.a = sum(self.x * self.w)
        if self.a >= 0.0:
            self.y = ACTIVACION
        else:
            self.y = DESACTIVACION        
        return self.y

    def pesos(self, w):
        global ACTIVACION, DESACTIVACION
        lista = list()
        for i in range(w + 1):
            lista.append(random.uniform(DESACTIVACION, ACTIVACION))
        lista = array(lista)
        print lista
        return lista

def genera(dimension):
    global ACTIVACION, DESACTIVACION
    lista = list()
    for i in range(dimension):
        lista.append(random.uniform(DESACTIVACION, ACTIVACION))
    lista.append(-1.0)
    x = array(lista)
    return x

def main():
    dim = int(argv[1])
    neurona = Neurona(dim)
    for i in range(2000):
        neurona.calcula(genera(dim))
        print '%s %d' % (' '.join([str(elemento) for elemento in neurona.x[:-1]]), neurona.y) 

main()
