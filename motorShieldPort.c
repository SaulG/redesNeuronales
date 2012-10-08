char val;         // variable to receive data from the serial port
int ledpingreen = 13;  // LED connected to pin 2 (on-board LED)
int E1 = 10;
int M1 = 12;
int E2 = 11;
int M2 = 13;

void setup()
{
  pinMode(ledpingreen, OUTPUT);  // pin 13 (on-board LED) as OUTPUT
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
  pinMode(E1, OUTPUT);
  pinMode(E2, OUTPUT);
  Serial.begin(115200);       // Comenzar comunicacion serial en 115200bps
 
}
 
void loop() {
  val = Serial.read();         // lee y almacena en val

  if(val == 'D'){               // Si se recibe 1 entrar al if
    digitalWrite(ledpingreen, HIGH);  // Encender Ledpin
    digitalWrite(M1,HIGH);
    digitalWrite(M2,HIGH); //clockwise
    digitalWrite(E1, HIGH);
    digitalWrite(E2, HIGH);
    Serial.println("Derecha");
    delay(500);
  }
  
  if(val == 'I'){              // Si recibe 0 entrar al if
    digitalWrite(ledpingreen, HIGH);   // Apaga el ledping

    digitalWrite(M1,LOW);
    digitalWrite(M2,LOW); //clockwise
    digitalWrite(E1, HIGH);
    digitalWrite(E2, HIGH);
    Serial.println("Izquierda");
    delay(500);
  }
  
  if(val == 'N'){              // Si recibe 0 entrar al if
    digitalWrite(ledpingreen, LOW);   // Apaga el ledping
    digitalWrite(M2,LOW); //clockwise
    digitalWrite(E1, LOW);
    digitalWrite(E2, LOW);
    Serial.println("Apagado");
    delay(500);
  }
 
}
