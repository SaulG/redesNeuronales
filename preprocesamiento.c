const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)
int aux = 0;
int sum = 0;
int salida = 0;

void setup() {
  Serial.begin(9600); 
}

void loop() {
  aux+=1
    sensorValue = analogRead(analogInPin);            
  // map it to the range of the analog out:
  outputValue = map(sensorValue, 0, 1023, 0, 255);  
  // change the analog out value:
  analogWrite(analogOutPin, outputValue);           
  Serial.print("sensor = " ); 
  sum+=sensorValue;  
  Serial.print(sensorValue);      
  Serial.print("\t output = ");      
  Serial.println(outputValue);   
  if(aux == 50){
    salida = sum / 50;
    salida = ( ( 2 * ( salida / 500) ) -1);
    Serial.println(salida);
    salida = 0;
    aux = 0;
  }

}
