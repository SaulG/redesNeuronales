#! /usr/bin/python

import random
import networkx as nx
import matplotlib.pyplot as plt
import time
import sys

from backpropagation import RedNeuronal

try:  
    import cPickle as pickle  
except ImportError:  
    import pickle  

class NetHeuristic:
 
    """
    Las matrices de conexiones tendran las primeras celdas de izquierda a derecha y de arriba a abajo dedicadas a las entradas, las segundas a las salidas y todas las demas para las capas ocultas.
    """

    def __init__(self, entradas, salidas, limite, entrenamientos, alfa=0.95, momentum=0.25):
        self.entrenamientos = entrenamientos
        self.alfa = alfa
        self.momentum = momentum
        self.entradas = int(entradas)
        self.salidas = int(salidas)
        self.limite = limite

    def graficar(self, solucion, pesos):
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

    def cota_superior(self):
        return self.limite
 
    def cota_inferior(self):
        return 1

    def is_input(self, n):
        if n < self.entradas:
            return True
        else:
            return False

    def is_hidden(self, n):
        if n >= (self.entradas+self.salidas):
            return True
        else:
            return False

    def is_output(self, n):
        if not self.is_input(n) and not self.is_hidden(n):
            return True
        else:
            return False

    def verificar_factibilidad(self, solucion):
        total = self.hidden_nodos + self.entradas + self.salidas

        for i in range(self.entradas):
            comp = False
            for j in range(total):
                if solucion[i][j] is 1 and self.is_hidden(j):
                    comp = True
                    break
            if comp is False:
                return False
            # a cada entrada le toca una o mas salidas todas de la capa intermedia y cero entradas

        for i in range(self.entradas+self.salidas, total):
            comp1 = False
            comp2 = False
            for j in range(total):
                if solucion [i][j] is 1 and (self.is_hidden(j) or self.is_output(j)):
                    comp1 = True
                if solucion [j][i] is 1 and (self.is_hidden(j) or self.is_input(j)):
                    comp2 = True
            if not(comp1 is True and comp2 is True):
                return False

            # a cada nodo capa media le toca minimo entrada de otro nodo de capa media o entrada y minimo una salida de un nodo de capa media o salida

        for i in range(self.entradas, self.entradas+self.salidas):
            comp = False
            for j in range(total):
                if solucion[j][i] is 1 and self.is_hidden(j):
                    comp = True
                    break
            if comp is False:
                return False

            # a cada nodo de salida le toca minimo una entrada de una capa intermedia y cero salidas
        return True

 
    def funcion_objetivo(self, solucion, n = None, cmd = None):
        if n is None:
            n = self.entrenamientos

        red = RedNeuronal(self.entradas, self.salidas, self.alfa, self.momentum, solucion)

        error = 0.0
        for i in range(n-1):
            red.backpropagation([0.0, 0.0], [0.0])
            red.backpropagation([0.0, 1.0], [1.0])
            red.backpropagation([1.0, 0.0], [1.0])
            red.backpropagation([1.0, 1.0], [0.0])

        error += red.backpropagation([0.0, 0.0], [0.0])[0]
        error += red.backpropagation([0.0, 1.0], [1.0])[0]
        error += red.backpropagation([1.0, 0.0], [1.0])[0]
        error += red.backpropagation([1.0, 1.0], [0.0])[0]


        if cmd is not None:
            print "[0, 0]", red.backpropagation([0.0, 0.0], [0.0])
            print "[0, 1]", red.backpropagation([0.0, 1.0], [1.0])
            print "[1, 0]", red.backpropagation([1.0, 0.0], [1.0])
            print "[1, 1]", red.backpropagation([1.0, 1.0], [0.0])
            return error, red

        return error

    def modificar_solucion(self, solucion):
        inicio = self.entradas + self.salidas
        fin = len(solucion)-1
        i = random.randint(inicio, fin)
        j = random.randint(inicio, fin)

        if solucion[i][j] is 1:
            solucion[i][j] = 0
        else:
            solucion[i][j] = 1

        return solucion
 
    def instancia_inicial(self):
        self.hidden_nodos = random.randint(self.cota_inferior(), self.cota_superior())
        total = self.hidden_nodos + self.entradas + self.salidas

        config = []        
        for i in range(total):
            config.append([int()]*total)

        for i in range(self.entradas):
            cantidad = random.randint(1, self.hidden_nodos)
            candidatos = range(self.entradas+self.salidas, total)
            salidas_nodo = random.sample(candidatos, cantidad )

            for j in salidas_nodo:
                config[i][j] = 1
            # a cada entrada le toca una o mas salidas todas de la capa intermedia y cero entradas

        for i in range(self.entradas+self.salidas, total):
            candidatos = range(self.entradas) + range(self.entradas+self.salidas, total)
            entradas_nodo = random.sample( candidatos, random.randint(1, len(candidatos)) )

            for j in entradas_nodo:
                config[j][i] = 1

            candidatos = range(self.entradas, total)
            salidas_nodo = random.sample(candidatos, random.randint(1, len(candidatos)) )

            for j in salidas_nodo:
                config[i][j] = 1

            # a cada nodo capa media le toca minimo entrada de otro nodo de capa media o entrada y minimo una salida de un nodo de capa media o salida

        for i in range(self.entradas, self.entradas+self.salidas):
            candidatos = range(self.entradas+self.salidas, total)
            entradas_nodo = random.sample(candidatos, random.randint(1, len(candidatos)) )

            for j in entradas_nodo:
                config[j][i] = 1

            # a cada nodo de salida le toca minimo una entrada de una capa intermedia y cero salidas

        return config

    def copiar(self, solucion):
        nueva = []
        for i in solucion:
            nueva.append([])
            for j in i:
                nueva[len(nueva)-1].append(j)
        return nueva


    def busqueda_voraz(self, maxReinicios, maxIntentos):
        modificado = []
        actual = []

        inicio_time = time.time()

        while True:
            mejor = self.instancia_inicial()
            
            if self.verificar_factibilidad(mejor):
                break

        for reinicios in range(maxReinicios):
            print reinicios, time.gmtime(time.time() - inicio_time )[4:6]
            actual = self.instancia_inicial()
        
            paso = 0

            for intentos in range(maxIntentos):
                modificado = self.copiar(actual)

                while True:
                    modificado = self.modificar_solucion(modificado) 
                    if self.verificar_factibilidad(modificado):
                        break

                objetivo_modificado = self.funcion_objetivo(modificado)
                objetivo_actual = self.funcion_objetivo(actual)

                if objetivo_modificado <= objetivo_actual:
                    paso += 1
                    actual = self.copiar(modificado)

            if self.funcion_objetivo(actual) <= self.funcion_objetivo(mejor):
                mejor = actual

        return mejor


def imprimir_matriz(matriz):

    for i in range(len(matriz)):
        print 
        for j in range(len(matriz)):
            print matriz[j][i], 
    print 

def guardar_red(red, name_file):
    fl = file(name_file, "w")
    pickle.dump(red, fl)  
    fl.close()

def cargar_red(name_file):
    fl.open(name_file, "r")
    red = pickle.load(fl) 
    fl.close()
    return red

def main():
    n = NetHeuristic(2, 1, 10, 500, 0.95, 0.1)
  #  config = n.busqueda_voraz(10, 50)
    config = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]

    (error, red) = n.funcion_objetivo(config, 500, "Dummy")
    print "Error: ", error

    red.graficar()
    guardar_red(red, "exor.dat")

main()
