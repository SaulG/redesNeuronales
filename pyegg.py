import serial,time,csv

ser = serial.Serial('/dev/tty.usbmodemfa131',9600)
while(True): 
 for row in csv.reader(iter(ser.readline, None)):
     #print row[5],row[3]
     print row
     
