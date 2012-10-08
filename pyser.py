import serial
ser = serial.Serial('/dev/tty.usbmodem131',115200)
while(True):
    valor = raw_input("> ")
    ser.write(valor)
         

