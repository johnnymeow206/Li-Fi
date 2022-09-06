int sensorPin = 22;
int value;
unsigned long time;
long delay_time=30;

void setup()
{
  pinMode(sensorPin, INPUT);
  //DDRA &= B00000001;  //This is safer as it sets ONLY pins A0(D22) as INPUT
  Serial.begin(115200);
  
}

void loop()
{
  //delayMicroseconds(100);
  //time = millis();
  value = digitalRead(sensorPin);
  
  //value = ;
  //Serial.println(time);
  
  delayMicroseconds(delay_time);
  Serial.println(value);
}
