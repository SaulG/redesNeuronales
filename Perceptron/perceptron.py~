import random

class Neurona:

    def __init__(self, nEntradas, alfa):
        self.nEntradas = nEntradas
        self.alfa = alfa
        self.pesos = []
        for i in range(nEntradas):
            self.pesos.append(random.random())
        self.pesos.append(random.random()/2.0)# Umbral

    def sumador(self, entradas):
        suma = 0.0
        for i in range(self.nEntradas):
            suma += self.pesos[i]*entradas[i]
        return suma

    def funcion_no_lineal(self, entradas):
        suma = self.sumador(entradas)
        suma -= self.pesos[-1]
        if suma >= 0:
            return 1
        else:
            return 0

    def entrenar(self, entradas, esperado):
        salida = self.funcion_no_lineal(entradas)
        entradas.append(-1)
        if salida != esperado:
            for i in range(self.nEntradas):
                self.pesos[i] += self.alfa*(esperado-salida)*entradas[i]
            return (salida, (esperado-salida)**2)
        else:
            return (salida, (esperado-salida)**2)

    def synapsis(self, entradas):
        return self.funcion_no_lineal(entradas)

    def ver_estado(self):
        print "Neurona:",
        for i in self.pesos:
            print i,

def main():
    # and
    n = Neurona(3, 0.10)
    fl = open("entrenamiento.dat", "w")
    for i in range(100):
        if (i+1)%10 == 0:
            suma = 0.0
            print "Ronda:", (i+1)
            print "[Entradas]-> (Salida)"
            temp = n.entrenar([0,0,0], 0)
            suma += temp[1]
            print "[0,0,0]->", temp
            temp = n.entrenar([0,0,1], 0)
            suma += temp[1]
            print "[0,0,1]->", temp
            temp = n.entrenar([0,1,0], 0)
            suma += temp[1]
            print "[0,1,0]->", temp
            temp = n.entrenar([0,1,1], 0)
            suma += temp[1]
            print "[0,1,1]->", temp
            temp = n.entrenar([1,0,0], 0)
            suma += temp[1]
            print "[1,0,0]->", temp
            temp = n.entrenar([1,0,1], 0)
            suma += temp[1]
            print "[1,0,1]->", temp
            temp = n.entrenar([1,1,0], 0)
            suma += temp[1]
            print "[1,1,0]->", temp
            temp = n.entrenar([1,1,1], 1)
            suma += temp[1]
            print "[1,1,1]->", temp
            print "Porcentaje de error: ", float(suma)/8
            fl.write(str(i)+" "+str(float(suma)/8.0)+"\n")

        else:
            suma = 0.0
            suma += n.entrenar([0,0,0], 0)[1]
            suma += n.entrenar([0,0,1], 0)[1]
            suma += n.entrenar([0,1,0], 0)[1]
            suma += n.entrenar([0,1,1], 0)[1]
            suma += n.entrenar([1,0,0], 0)[1]
            suma += n.entrenar([1,0,1], 0)[1]
            suma += n.entrenar([1,1,0], 0)[1]
            suma += n.entrenar([1,1,1], 1)[1]
            suma /= 8.0
            fl.write(str(i)+" "+str(suma)+"\n")
    fl.close()
main()
