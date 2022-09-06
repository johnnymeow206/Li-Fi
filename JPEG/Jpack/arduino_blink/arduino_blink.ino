const int led=13;
int value=0;

void setup() 
   { 
      Serial.begin(115200); 
      pinMode(led, OUTPUT);
      digitalWrite (led, LOW);
      Serial.println("Connection established...");
   }
 
void loop() 
   {
     while (Serial.available())
        {
           value = Serial.read();
        }
     
     if (value == '1')
        digitalWrite (led, HIGH);
     else{
        digitalWrite (led, LOW);
     }
      delay(5);
   }
