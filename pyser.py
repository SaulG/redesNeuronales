import serial
ser = serial.Serial('/dev/tty.usbmodemfd121',115200)
while(True):
    valor = raw_input("> ")
    ser.write(valor)
         

