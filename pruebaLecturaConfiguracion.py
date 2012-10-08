def main():
    datos = open("configuration.dat","r")
    datos = datos.readlines()
    lista = list()
    for d in datos:
        lista.append(d.strip())
    dim = 0
    neurona = 0
    dt = list()
    aux = 0
    for i in lista:
        print "Linea ", aux," ",i
        if i == 0:
            break
        
    for e in range(len(lista)):
        if e == (len(lista) - 1):
            break
        print "Dimension",lista[e]," Neuronas ", lista[e + 1]
main()
