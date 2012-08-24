from sys import argv
import numpy
import random

class redNeuronal:
    def __init__(self, datos):
        self.valoresDeEntrada = self.stringToVector(datos)
        self.vectorDePesos = self.generador(len(self.valoresDeEntrada))
        self.validacionNeurona = self.EvaluacionDeEntradas(self.valoresDeEntrada, self.vectorDePesos)

    def stringToVector(string):
        vector = list(string.split(' '))
        return vector

    def generador(self, tamanioDeVector):
        vect = list()
        for v in tamanioDeVector:
            vect.append(random.uniform(-1,1))
        vect.append(random.uniform)
        return vect

    def EvaluacionDeEntradas(self, entrada, vectorDePesos):
        umbral = vectorDePesos[-1]
        vectorDePesos = vectorDePesos[:-2]
        productoNeurona = list()
        acumulado = 0
        for item in entrada:
            acumulado += vectorDePesos[aux] * item
        if umbral < acumulado:
            return True
        else:
            return False    
def main():
    
    neurona = redNeuronal(argv[1])
    print neurona.EvaluacionDeEntradas

    
main()
