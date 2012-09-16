char val;
int E1 = 10;
int M1 = 12;
int E2 = 11;
int M2 = 13;
boolean direction1 = true;
void setup()
{
  Serial.begin(115200);
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
  pinMode(E1, OUTPUT);
  pinMode(E2, OUTPUT);
} 

void loop()
{
  if(direction1){
    digitalWrite(E1,HIGH);
    digitalWrite(E2,HIGH);
  }else{
    digitalWrite(E1,LOW);
    digitalWrite(E2,LOW);
  }

  direction1 = !direction1;
  digitalWrite(M1,HIGH);
  digitalWrite(M2,HIGH);
  delay(2000);
  digitalWrite(M1,LOW);
  digitalWrite(M2,LOW);
  delay(2000);

}
