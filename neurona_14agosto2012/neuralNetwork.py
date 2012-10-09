#! usr/bin/python

import random

class Neuron:
    
    def __init__(self, nInputs, umbral):
        self.umbral = umbral
        self.weightVector = []
        for i in range(nInputs):
            self.weightVector.append(random.random()) # Modificar

    def algo(self, inputVector):
        
        otroAlgo = 0.0
        for i in range(len(inputVector)):
            inputVector[i] *= self.weightVector[i]
            otroAlgo += inputVector[i]

        if otroAlgo <= self.umbral:
            return 0.0
        else:
            return 1.0

class neuralNet:

    def __init__(self, umbral=0.5, nNeurals=1):
        self.umbral = umbral
        self.neuralVector = [] # Modificar despues, ahora representar una capa
        for i in range(nNeurals):
            self.neuralVector.append( Neuron(5, umbral) ) # Terminar

    def start(self):
        for i in self.neuralVector:
            inputVector = []
            for j in range(5):
                inputVector.append(float(random.randint(0,1)))

def main():
    net = neuralNet (0.5)
    net.start()

main()
