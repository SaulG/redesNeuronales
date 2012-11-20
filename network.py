#! /usr/bin/python                                                                                                                                                      
import serial, sys, csv, time
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


def guardar_red(red, name_file):
    fl = file(name_file, "w")
    pickle.dump(red, fl)
    fl.close()

def cargar_red(name_file):
    fl = file(name_file, "r")
    red = pickle.load(fl)
    fl.close()
    return red

def main():
    if len(sys.argv) > 1:
        red = cargar_red(sys.argv[2])
        
    else:
        red = cargar_red("red_brazo_.dat")
    
    print int(red.evaluar([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])[0])

    egg = serial.Serial("/dev/tty.usbmodem12341", 115200)
    time.sleep(2) # waiting the initialization...                                                    

    ser = serial.Serial('/dev/tty.usbmodemfd121', 115200) 

    while True:
        print "Aqui en iteracion"
        for row in csv.reader(iter(egg.readline, None)):
            try:
                print "dentro del for"
                if red.evaluar(row[1:])[0] == 1:
                    ser.write('1')
                else:
                    ser.write('0')
                print red.evaluar(row[1:])[0]
                ser.write(red.evaluar(row[1:])[0])
            except:
                print "Error recibiendo valores del egg"    
main()
