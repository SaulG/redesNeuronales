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
        aux = 0
        for item in entrada:
            if( ( vectorDePesos[aux] * item ) == 1 ):
                productoNeurona[aux] = 1
            else:
                productoNeurona[aux] = 0
            aux + = 1
        if umbral < sum(productoNeurona):
            print "Producto de neurona"
            print productoNeurona
            print "Sumatoria de la lista de producto"
            print sum(productoNeurona)
            return True
        else:
            return False

def main():
    neurona = redNeuronal(argv[1], float(argv[2]))
    print neurona.EvaluacionDeEntradas

    
main()
