from numpy import array
import random

#deltaw = alfa * sum(x) * delta(t-y) + lambda * deltasum(w) - 1

class Neurona:
    
    def __init__(self, x, a, b):
        self.x = x
        self.wa = self.genera(x, a)
        self.wb = self.genera(x, b)
        self.clasificacion = self.clasificacion(self.x, self.wa)

    def genera(self, x, theta):
        tam = len(x)
        lista = list()
        for i in range(tam):
            lista.append(random.uniform(-1,1))
        lista.append(theta)
        return array(lista)

    def clasificacion(self, x, w):
        if ( ( sum( self.x * self.w ) ) <= 0 ):
            return True
        else:
            return False
       
def generaEntrada(tam, dim, a, b):
    output = open('datos.txt','w')
    for i in range(tam):
        st = ''
        for j in range(dim):
            numero = random.uniform(-1,1)
            valor = ''
            if numero < a:
                valor = '00'
            elif numero > a and numero < b:
                valor = '01'
            elif numero > b:
                valor = '11'
            st += str(numero)
            st += ' '
            st += valor
            st += ' '
        print>>output, st

def main():
    try:
        generaEntrada(int(argv[1]), int(argv[2]), -0.5, 0.5)
    except:
        generaEntrada(500, 1, -0.5, 0.5)
    x = array(x)
    neurna = Neurona(x, -.5, .5)
    print neurna.clasificacion
main()
