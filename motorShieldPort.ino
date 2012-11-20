// Se usa para almacenar el valor tomado en el puerto serial
char val;
//Puerto analogico que obtendra la posicion del potenciometro
int potPin = 1;
//SALIDAS para motores DC E1,E2, M1 y M2
int E1 = 10;
int M1 = 12;
int E2 = 11;
int M2 = 13;
//Se almacena el valor del potenciometro
int potLectura = 0;

void setup()
{
    //Se configuran como salidas los puertos que dan corriente a los motores DC
    pinMode(M1, OUTPUT);
    pinMode(M2, OUTPUT);
    pinMode(E1, OUTPUT);
    pinMode(E2, OUTPUT);
    // Comenzar comunicacion serial en 115200bps
    Serial.begin(115200);
 
}
 
void loop() {
    //Almacena el valor del potenciometro del puerto A1
    potLectura = analogRead(potPin);
    //Imprime en el puerto serial el valor del potenciometro
    Serial.println(potLectura);
    //Almacena el valor que recibe en el puerto serial
    val = Serial.read();         
    //Imprime el valor que recibe en el puerto serial
    Serial.println(val);

    // Si se recibe 1 hara un giro a la derecha 
    if(val == '1'){               
        //bandera que sirve para identificar 
        Serial.println("entre der");
        //Se coloca un umbral para no mover el brazo mas de lo debido para no lastimarlo
        if(potLectura >= 600){
            //Motores van de 0 a 180 grados
            digitalWrite(M1,HIGH);
            digitalWrite(M2,HIGH); 
            digitalWrite(E1, HIGH);
            digitalWrite(E2, HIGH);
            //Bandera para saber que entro
            Serial.println("Derecha");
            //Una espera de 2 segundos
            delay(2000);
            //Detiene motores
            digitalWrite(M1,LOW); 
            digitalWrite(M2,LOW); 
            digitalWrite(E1, LOW);
            digitalWrite(E2, LOW);
            //Bandera para saber que esta apagado
            Serial.println("Apagado");
        }
    }
  // Si se recibe 0 hara un giro a la izquierda
  if(val == '0'){ 
      //Bandera que sirve para identificar
      Serial.println("entre izq");
      //Se coloca un umbral para no mover el brazo mas de lo debido para no lastimarlo
      if(potLectura <= 1000){
          //Motores van de 180 a 0 grados
          digitalWrite(M1,LOW);
          digitalWrite(M2,LOW);
          digitalWrite(E1, HIGH);
          digitalWrite(E2, HIGH);
          //Imprime bandera
          Serial.println("Izquierda");
          //Una espera de 2 segundos
          delay(2000);
          //Detiene motores
          digitalWrite(M1,LOW);
          digitalWrite(M2,LOW);
          digitalWrite(E1, LOW);
          digitalWrite(E2, LOW);
          //Bandera para saber que esta apagado
          Serial.println("Apagado");
      }
  }  
  //Espera medio segundo
  delay(500);
}
