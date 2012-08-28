from sys import argv
import numpy
import random

class redNeuronal:
    def __init__(self, datos, enfriamiento):
        self.valoresDeEntrada = datos
        self.vectorDePesos = self.generador(len(self.valoresDeEntrada))
        self.umbral = self.vectorDePesos[-1]
        self.validacionNeurona = self.EvaluacionDeEntradas(self.valoresDeEntrada, self.vectorDePesos, self.umbral, enfriamiento)
    
    def setVectorDePesos(self, vectorDePesos):
        self.vectorDePesos = vectorDePesos
    
    def getVectorDePesos(self):
        return self.vectorDePesos

    def generador(self, tamanioDeVector):
        vect = list()
        for v in range(tamanioDeVector):
            vect.append(random.uniform(-1,1))
        vect.append(-1.0)
        print vect
        return vect

    def EvaluacionDeEntradas(self, entrada, vectorDePesos, umbral, enfriamiento):
        productoNeurona = list()
        aux = 0
        print umbral
        for item in entrada:
            print aux, item
            if( ( vectorDePesos[aux] * float(item) ) == 1 ):
                productoNeurona.append(1)
            else:
                productoNeurona.append(0)
            aux+=1
        if  0.0 < sum(productoNeurona):
            print 
            print "Producto de neurona"
            print productoNeurona
            print "Sumatoria de la lista de producto"
            print sum(productoNeurona)
            return True
        else:
            return False

def main():
    opcion = ''
    datos = ''
    enfriamiento = ''
    try:
        neurona = redNeuronal(argv[1], float(argv[2]))
        print "Validacion: ", neurona.validacionNeurona
    except: 
        datos = argv[1] 
        Input = open(datos,'r')
        vector = Input.readline()
        vector = vector.strip()
        vector = list(vector.split(' '))
        print vector
        enfriamiento = raw_input('Enfriamiento: ')
        neurona = redNeuronal(vector, float(enfriamiento))
        print "Validacion: ", neurona.validacionNeurona
        validacion = neurona.validacionNeurona
        while validacion != True:
            valorEsperado = list()
            for i in neurona.vectorDePesos:
                print 'Valor resultante: ',i
                valor = raw_input('Valor esperado del valor: ')
                valorEsperado.append(int(valor))
            neurona.setVectorDePesos(ajusteNeurona(valorEsperado,neurona.getVectorDePesos()))    
            print neurona.vectorDePesos
            validacion = neurona.validacionNeurona

def ajusteNeurona(t, entrada):
    ajuste = list()
    aux = 0 
    y = list()
    for e in t:
        if t == 0:
            y.append(1)
        else:
            y.append(-1)
    for item in entrada:
        ajuste.append( item * ( t[aux] - y[aux] ) )
        aux+=1
    print ajuste
    return ajuste

main()
