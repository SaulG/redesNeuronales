from sys import argv

def preprocesamiento(archivo):
    file = open(archivo,'r')
    datos = list()
    a = list()
    fileLines = file.readlines()
    file.close()
    for i in fileLines:
        i = i.strip()
        a = i.split(',')
        datos.append(a)
    #print datos
    newFile = open('%s.prc' % archivo ,'w')
    bandera = True
    goodData = list()
    for d in datos:
     for n in xrange(len(datos[0])):
         #print d[n]
         if int(d[0]) >= 100:
            # print "Mori"
             bandera = False
             break
         bandera = True
     if bandera:
         goodData.append(d)
    data = ''
    listaDatos = list()
    for l in goodData:
        lista = list()
        for n in xrange(len(datos[0])):
            if n == 0:
                continue
            data+= '%s ' %l[n]
            lista.append(float(l[n]))
        listaDatos.append(lista)
        print >>newFile, data
        data = ''
    newFile.close()
    return
   # for l in listaDatos:
        #print neuronal(l)         
    
    
def generatesEntries(archivo):
    file = open(archivo,'r')
    lista = list()
    fileLines = file.readlines()
    file.close()
    for i in fileLines:
        i = i.strip()
        lista = i
        print lista

def main():
    archivo = argv[1]
    print "Preprocesando ..."
    preprocesamiento(archivo)
    print "Preprocesamiento listo ..."
    print "Generando entradas"
    generatesEntries('%s.prc'%archivo)
    print "Entradas generadas..."
main()
