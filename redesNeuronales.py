import numpy
from sys import argv
from random import random, choice

class redNeuronal:
    def __init__(self, tamanio, umbral):
        self.vector = self.generador(tamanio)
        self.validacionNeurona = self.determinarEntradas(tamanio, umbral)

    def generador(self, tamanio):
        vect = list()
        for v in tamanio:
            vect.append(random())
        return vect

    def determinarEntradas(self, tamanio, umbral):
        aux = 0
        productoNeurona = list()
        acumulado = 0
        for t in tamanio:
            acumulado += self.vector[aux] * int(t)
        if umbral > acumulado:
            return True
        else:
            return False    
def main():
    try:
        neurona = redNeuronal(argv[1], float(argv[2]))
        print neurona.validacionNeurona
    except:
        print 'No tenemos datos :( '
    
main()
