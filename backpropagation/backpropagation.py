#! /usr/bin/python

import random
import math

class Neurona:

    def __init__(self, nEntradas, alfa, N):
        self.nEntradas = nEntradas
        self.alfa = alfa
        self.N = N
        self.cambio_anterior = 0.0
        self.pesos = []

        for i in range(nEntradas+1):
            self.pesos.append(random.random())


    def sumar(self, entradas):
        suma = 0.0
        for i in range(len(self.pesos)):
            suma += self.pesos[i]*entradas[i]
        return suma

    def funcion_no_lineal(self, entradas):
        suma = self.sumar(entradas)
#        return math.tanh(suma)
        return (1.0/(1+math.exp(-1*suma)))

    def derivada_funcion(self, y):
        return (y-y**2)
#        return (1.0-y**2)

    def entrenar(self, error):
        temp = []
        for i in range(len(self.pesos)):
            if i < len(self.pesos)-1 : 
                temp.append( self.pesos[i]*error*self.derivada_funcion(self.ultima_salida) )
            cambio = 2*self.alfa*error*self.ultimas_entradas[i]*self.derivada_funcion(self.ultima_salida) #+ self.N*self.cambio_anterior
            self.pesos[i] += cambio
            self.cambio_anterior = cambio
        return temp #regresa el error de las neuronas de la siguiente capa

    def synapsis(self, entradas):
        self.ultimas_entradas = entradas
        self.ultima_salida = self.funcion_no_lineal(entradas)
        return self.ultima_salida

    def ver_estado(self):
        print "Neurona:",
        for i in self.pesos:
            print i,
        print 

class Red_neuronal:

    def __init__(self, entradas, salidas, capas, neurona_por_capa, alfa, constante_momentum): #El numero de capas ocultas, el numero de neuronas en cada capa
        self.entradas = entradas
        self.salidas = salidas
        self.capas = capas
        self.neuronas= neurona_por_capa
        self.alfa = alfa
        self.N = constante_momentum
        self.red = []
        self.cambio_anterior = ""

        #Entrada 
        temp = []
        for j in range(neurona_por_capa):
            temp.append(Neurona(entradas, self.alfa, self.N))
        self.red.append(temp)

        for i in range(1, capas):
            temp = []
            for j in range(neurona_por_capa):
                temp.append(Neurona(neurona_por_capa, self.alfa, self.N))
            self.red.append(temp)

        temp = []
        for i in range(salidas):
            temp.append(Neurona(neurona_por_capa, self.alfa, self.N))
        self.red.append(temp)

    def backpropagation(self, entradas, deseado):
        salida = self.evaluar(entradas)

################# trabajando aqui
        next_err = []
        for j in range(len( self.red[len(self.red)-1] )):
            error = deseado[j] - salida[j]
            temp = self.red[len(self.red)-1][j].entrenar(error)

            if j <= 0:
                next_err = temp
            else:
                for i in range(len(next_err)):
                    next_err[i] += temp[i]

        error = next_err
#################

        for i in range(1, len(self.red)):

            next_err = []
            for j in range(len( self.red[(len(self.red)-1)-i] )):
                temp = self.red[((len(self.red)-1)-i)][j].entrenar(error[j])

                if j <= 0:
                    next_err = temp
                else:
                    for i in range(len(next_err)):
                        next_err[i] += temp[i]

            error = next_err

        general_error = 0.0
        for i in range(len(deseado)):
            general_error = general_error + ((float(deseado[i]-salida[i])**2)/2.0)

        return salida, general_error

    def copiar_vector(self, vector):
        temp = []
        for i in vector:
            temp.append(i)
        return temp

    def evaluar(self, entradas):
        output = []
        entradas.append(-1.0)
        for i in range(len(self.red[0])):
            output.append(self.red[0][i].synapsis(entradas))
        output.append(-1.0)

        for i in range(1, len(self.red)):
            input_ = self.copiar_vector(output)
            output = []
            for j in range(len(self.red[i])):
                output.append(self.red[i][j].synapsis(input_))
            if i < len(self.red) - 1:
                output.append(-1.0)

        return output
 
def main():
    # Entradas, salidas, capas ocultas, neurona por capa,
    n = Red_neuronal(2, 1, 1, 2, 0.95, 0.25 )

    for j in range(1):
        fl = open(("entrenamiento"+".dat"), "w")
        for i in range(2000):
            suma = 0.0
            #print "Iteracion: ", (i+1)
            #print "[0, 0]->", n.backpropagation([0, 0], [0])
            suma += n.backpropagation([0, 0], [0])[1]
            #print "[0, 1]->", n.backpropagation([0, 1], [1])
            suma += n.backpropagation([0, 1], [1])[1]
            #print "[1, 0]->", n.backpropagation([1, 0], [1])
            suma += n.backpropagation([1, 0], [1])[1]
            #print "[1, 1]->", n.backpropagation([1, 1], [0])
            suma += n.backpropagation([1, 1], [0])[1]
            fl.write(str(i)+" "+str(suma)+"\n")
            if (i+1)%200 == 0:
                print "Entrenamiento ", (i+1)
                print "[Entradas]->([Salidas], Error de la entrada)"
                print "[0, 0]->", n.backpropagation([0, 0], [0])
                print "[0, 1]->", n.backpropagation([0, 1], [1])
                print "[1, 0]->", n.backpropagation([1, 0], [1])
                print "[1, 1]->", n.backpropagation([1, 1], [0])
                print "Error total:", suma


        fl.close()
main()
