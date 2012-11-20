#! /usr/bin/python

import random
import math
import networkx as nx
import matplotlib.pyplot as plt

class RedNeuronal:

    def __init__(self, entradas, salidas, alfa, constante_momentum, red): #El numero de capas ocultas, el numero de neuronas en cada capa
        self.entradas = entradas
        self.salidas = salidas

        self.alfa = alfa
        self.N = constante_momentum

        self.red = red
        self.total_neuronas = len(red)
        self.neuronas_escondidas = len(red) - self.entradas - self.salidas

        self.pesos = new_matrix(self.total_neuronas)
        self.last_output = [float()]*self.total_neuronas

        self.threshold_vector = []
        self.threshold_vector_anterior = [float()]*self.total_neuronas

        for i in range(self.total_neuronas):
            self.threshold_vector.append(random.random())

        self.cambio_anterior = []
        for i in range(self.total_neuronas):
            self.cambio_anterior.append([float()]*self.total_neuronas)

        for i in range(self.total_neuronas):
            for j in range(self.total_neuronas):
                if self.red[i][j] is 1:
                    self.pesos[i][j] = random.uniform(-1, 1)

    def graficar(self, solucion=None, pesos=None):
        if solucion == None:
            solucion = self.red
        if pesos == None:
            pesos = self.pesos
        G=nx.DiGraph()

        colors = list()
        labels = list()
        graph = list()
        contador = 0

        for i in range(self.entradas):
            colors.append("green")
            for j in range(len(solucion[i])):
                if solucion[i][j] is 1:
                    labels.append(str(round(pesos[i][j], 2)) )
                    G.add_edge(i, j)
                    graph.append( (i, j) )

        for i in range(self.entradas, self.entradas+self.salidas):
            colors.append("red")
            for j in range(len(solucion[i])):
                if solucion[i][j] is 1:
                    labels.append(str(round(pesos[i][j], 2)) )
                    G.add_edge(i, j)
                    graph.append( (i, j) )

        for i in range(self.entradas+self.salidas, len(solucion)):
            colors.append("blue")
            for j in range(len(solucion[i])):
                if solucion[i][j] is 1:
                    labels.append(str(round(pesos[i][j], 2)) )
                    G.add_edge(i, j)
                    graph.append( (i, j) )

        positions = nx.shell_layout(G)

        nx.draw_networkx_nodes(G, positions, node_size=100, 
                           alpha=0.3, node_color=colors)

        nx.draw_networkx_edges(G, positions, width=1,
                           alpha=0.3, edge_color="black")

        nx.draw_networkx_edge_labels(G, positions, edge_labels=dict(zip(graph, labels)), 
                                         label_pos=0.3)

        plt.show()

    def backpropagation(self, entradas, deseado):
        visitados = [int()]*self.total_neuronas
        delta = [float()]*self.total_neuronas
        pesos_anteriores = copy_matrix(self.pesos)
        
        salidas = self.evaluar(entradas)

        siguientes = list()
        contador = 0
        general_error = 0.0

        for i in range(self.entradas, self.entradas+self.salidas):
            visitados[i] = 1
            delta[i] = float(deseado[contador]-salidas[contador])*derivada_funcion(self.last_output[i] )
            general_error += float(deseado[contador]-salidas[contador])**2
            contador += 1

            for j in range(self.total_neuronas):
                if self.red[j][i] is 1:
                    cambio = self.alfa*delta[i]*self.last_output[j] + self.cambio_anterior[j][i]*self.N
                    self.cambio_anterior[j][i] = cambio
                    self.pesos[j][i] -= cambio
                    siguientes.append(j)

            cambio = self.alfa*delta[i] + self.threshold_vector_anterior[i]*self.N # Este es el valor del umbral agregado ala sumatoria de pesos*entradas
            self.threshold_vector_anterior[i] = cambio
            self.threshold_vector[i] -= cambio 
        del contador
        general_error /= 2.0

        while True:
            sig_temp = list()
            for i in siguientes:
                if visitados[i] is 1:
                    continue
                visitados[i] = 1
            
                for j in range(self.total_neuronas):
                    if self.red[i][j] is 1:
                        delta[i] += pesos_anteriores[i][j]*delta[j]
                delta[i] *= derivada_funcion(self.last_output[i] )

                for j in range(self.total_neuronas):
                    if self.red[j][i] is 1:
                        cambio = self.alfa*delta[i]*self.last_output[j] + self.cambio_anterior[j][i]*self.N
                        self.cambio_anterior[j][i] = cambio
                        self.pesos[j][i] -= cambio
                        sig_temp.append(j)

                cambio = self.alfa*delta[i] + self.threshold_vector_anterior[i]*self.N# Este es el valor del umbral agregado ala sumatoria de pesos*entradas
                self.threshold_vector_anterior[i] = cambio
                self.threshold_vector[i] -= cambio 
            
            if len(sig_temp) < 1:
                break
            siguientes = sig_temp

        return general_error, salidas

    def evaluar(self, entradas):
        visitados = [int()]*self.total_neuronas

        siguientes = list()
        for i in range(len(entradas)):
            visitados[i] = 1
            self.last_output[i] = entradas[i]

            for j in range(self.total_neuronas):
                if self.red[i][j] is 1:
                    siguientes.append(j)


        # tomar en cuenta siguiente capa
        while True:
            sig_temp = list()
            for i in siguientes:
                if visitados[i] is 1:
                    continue
                visitados[i] = 1
            
                sumatoria = 0.0
                for j in range(self.total_neuronas):
                    if self.red[j][i] is 1:
                        sumatoria += self.pesos[j][i]*self.last_output[j]
                sumatoria += self.threshold_vector[i] # Este es el valor del umbral agregado ala sumatoria de pesos*entradas

                self.last_output[i] = kernel(sumatoria)

                for j in range(self.total_neuronas):
                    if self.red[i][j] is 1:
                        sig_temp.append(j)
            
            if len(sig_temp) < 1:
                break
            siguientes = sig_temp

        output = self.last_output[self.entradas : self.entradas+self.salidas]

        return output

def kernel(value ):
    return math.tanh(value)
    #return (1.0/(1+math.exp(-1*value)))

def derivada_funcion(value ):
    #return (value-value**2)
     return 1 - value**2
    #return kernel(value)*(1 - kernel(value))
    
def copy_matrix(matrix):
    new = list()
    for i in matrix:
        temp = list()
        for j in i:
            temp.append(j)
        new.append(temp)
    return new
 

def new_matrix(n):
    n = int(n)
    matrix = list()
    for i in range(n):
        matrix.append( [int()]*n)
    return matrix
