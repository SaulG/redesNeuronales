import serial,time,csv #serial el modulo que instalamos                                                                                                  
egg = serial.Serial('/dev/tty.usbmodem12341',9600)
ser = serial.Serial('/dev/tty.RN42-45E5-SPP', 115200)#Primero se dice el puerto y luego en      que baud sera oido                                       

while(True):
 for row in csv.reader(iter(egg.readline, None)):
     try:
        value = int(row[1])
     except:
        value = 0                                                                                                                                      
        
     print "Concentracion "+str(value)
    
     if(value > 80):
         ser.write('1')
         ser.write('3')
     if (value > 40 and value < 80):
         ser.write('1')
         ser.write('2')
     elif (value < 40):
         ser.write('0')
         ser.write('3')
         

