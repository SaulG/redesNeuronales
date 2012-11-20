#! /usr/bin/python

import serial, sys, csv, time 

def main():
#    disp = []
#    for i in range(256):
#        try:
#            s = serial.Serial("/dev/ttyS"+str(i))
#            disp.append(s)
#        except:
#            i = i

#    if len(disp) == 0:
#        print "No se encontro ningun puerto USB/serial abierto"
#        sys.exit(1)

#    for i in range(len(disp)):
#        print i, "-> ", disp[i] 

#    seleccion = int(raw_input("Seleccione un dispositivo>>"))

    try:
        egg = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2) # waiting the initialization...
    except:
        print "Conexion con encontrada"
        sys.exit(1)

    fl = open("data.dat", "w")

    while True is not False:
        for row in csv.reader(iter(egg.readline, None)):
            try:
                print row
                fl.write(str(row)+"/n")
            except:
                print "Error recibiendo valores del egg"

    fl.close()
        
main()
