from sys import argv
import numpy
import random

class redNeuronal:
    def __init__(self, datos, enfriamiento):
        self.valoresDeEntrada = self.stringToVector(datos)
        self.vectorDePesos = self.generador(len(self.valoresDeEntrada))
        self.umbral = self.vectorDePesos[-1]
        self.validacionNeurona = self.EvaluacionDeEntradas(self.valoresDeEntrada, self.vectorDePesos, self.umbral, enfriamiento)

    def stringToVector(string):
        vector = list(string.split(' '))
        print "VECTOR: "+vector
        return vector

    def generador(self, tamanioDeVector):
        vect = list()
        for v in tamanioDeVector:
            vect.append(random.uniform(-1,1))
        vect.append(random.uniform)
        return vect

    def EvaluacionDeEntradas(self, entrada, vectorDePesos, umbral, enfriamiento):
        vectorDePesos = vectorDePesos[]
        productoNeurona = list()
        for item in entrada:
            acumulado += vectorDePesos[aux] * item
        if umbral < acumulado:
            print acumulado
            return True
        else:
            #realizar de forma recursiva evaluacion de entradas dando un enfriamiento por cada iteracion
            return EvaluacionDeEntradas()

def main():
    neurona = redNeuronal(argv[1], float(argv[2]))
    print neurona.EvaluacionDeEntradas

    
main()
