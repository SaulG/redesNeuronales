from numpy import array
from sys import argv
import random

ACTIVACION = 1.0
DESACTIVACION = -1.0
TASA_DE_APRENDIZAJE = 0.05

class Neurona:
    def __init__(self, dim):
        self.w = self.pesos(dim)

    def entrena(self, entrada, respuestaDeseada):
        global TASA_DE_APRENDIZAJE
        self.calcula(entrada)
        self.respuesta = respuestaDeseada
        self.cambio = TASA_DE_APRENDIZAJE * (self.respuesta - self.y) * self.x
        self.w += self.cambio
        return

    def pesos(self, w):
        global ACTIVACION, DESACTIVACION
        lista = list()
        for i in range(w + 1):
            lista.append(random.uniform(DESACTIVACION, ACTIVACION))
        lista = array(lista)
        return lista

    def calcula(self, entrada):
        global ACTIVACION, DESACTIVACION
        self.x = entrada
        self.a = sum(self.x * self.w)
        if self.a >= 0.0:
            self.y = ACTIVACION
        else:
            self.y = DESACTIVACION
        return self.y

class Capa:
    def __init__(self, tamanio, dim):
        self.neuronas = self.inicializaNeurona(tamanio, dim)
        self.tamanio = tamanio
        self.dim = dim
        
    def inicializaNeurona(self, tamanio, dim):
        neuronas = list()
        for e in range(tamanio):
            neuronas.append([Neurona(dim)]) 
        return neuronas

    def calcula(self, entrada):
        self.y = list()
        for neurona in self.neuronas
            y.append(neurona.calcula(entrada)
        return array(self.y)

class Red:
    def __init__(self, archivo):
        self.capas = self.inicializaCapas(archivo)

    def inicializaCapas(self, archivo):
        datos = open(archivo,"r")
        datos = datos.readlines()
        datos.close()
        datosDeConfiguracion = list()
        for d in datos:
            datosDeConfiguracion.append(int(d.strip()))    
        capas = list()
        for e in range(len(datosDeConfiguracion)):
            if e == ( len(datosDeConfiguracion) -1):
                break
            capas.append(Capa(datosDeConfiguracion[e] , datosDeConfiguracion[e + 1]))
        return capas

    def calcula(self, entrada):
        for e in range(len(self.capas)):
            capas[e].calcula(entrada)

def genera(dimension):
    global ACTIVACION, DESACTIVACION
    lista = list()
    for i in range(dimension):
        value = random.uniform(DESACTIVACION, ACTIVACION)
        lista.append(value)
    lista.append(-1.0)
    x = array(lista)
    return x

def main():
    try:
        red = Red(argv[1])
    except:
        red = Red("configuracion.dat")
main()
