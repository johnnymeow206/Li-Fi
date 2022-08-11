#define CLOCK_PIN 2
#define DATA_PIN 3

short clockDelayMS = 10;
String data = "What's up doc?";

void setup()
{
  Serial.begin(9600);
  
  pinMode(CLOCK_PIN, OUTPUT);
  pinMode(DATA_PIN, OUTPUT);
}

void loop()
{
  for(int charPos = 0; charPos < data.length(); charPos++)
  {
    char charAtPos = data.charAt(charPos);
  
    for(int bitPos = 7; bitPos >= 0; bitPos--)
    {
      bool bitValue = bitRead(charAtPos, bitPos);
      Serial.print(bitValue);

      digitalWrite(DATA_PIN, bitValue);
      delay(10);
      
      digitalWrite(CLOCK_PIN, HIGH);
      
      delay(clockDelayMS);

      digitalWrite(CLOCK_PIN, LOW);

      delay(clockDelayMS);
    }

    Serial.println("");
 }
}
