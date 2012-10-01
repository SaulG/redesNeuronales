from numpy import array
from sys import argv
import random

ACTIVACION = 1.0
DESACTIVACION = -1.0

class Neurona:
    def __init__(self, dim):
        #Vector de pesos de la neurona
        self.w = self.pesos(dim)
    #Calcula el producto de vector de entrada por vector de pesos
    #nos da una activacion o desactivacion
    def calcula(self, entrada):
        global ACTIVACION, DESACTIVACION
        self.x = entrada
        self.a = sum(self.x * self.w)
        if self.a >= 0.0:
            self.y = ACTIVACION
        else:
            self.y = DESACTIVACION        
        return self.y

    #Genera de manera al azar un vector de pesos dado el tamanio
    # del vector de entrada
    def pesos(self, w):
        global ACTIVACION, DESACTIVACION
        lista = list()
        for i in range(w + 1):
            lista.append(random.uniform(DESACTIVACION, ACTIVACION))
        lista = array(lista)
        print lista
        return lista

#Genera dummies que son nuestro vector de entrada a la neurona
# de una n dimension dada de manera uniformemente
#aleatoria dentro del rando de activacion y desactivacion

def genera(dimension):
    global ACTIVACION, DESACTIVACION
    lista = list()
    for i in range(dimension):
        lista.append(random.uniform(DESACTIVACION, ACTIVACION))
    lista.append(-1.0)
    x = array(lista)
    return x

#Se le da a la neurona una n dimension para que genere
# su vector de pesos, para luego se generen una cierta cantidad
# de vectores que la neurona va ir clasificando
def main():
    dim = int(argv[1])
    neurona = Neurona(dim)
    for i in range(2000):
        neurona.calcula(genera(dim))
        print '%s %d' % (' '.join([str(elemento) for elemento in neurona.x[:-1]]), neurona.y) 

main()
