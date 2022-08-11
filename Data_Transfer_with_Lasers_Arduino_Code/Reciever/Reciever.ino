#define CLOCK_PIN A1
#define DATA_PIN A0

short lightThreshold = 400;
bool dataWasRead = false;

char currentChar = 0;
short currentCharPos = 7;

void setup() {
  Serial.begin(9600);
}


void loop() {
  short analogValueClock = analogRead(CLOCK_PIN);
  bool boolValueClock = analogValueClock > lightThreshold;

  short analogValueData = analogRead(DATA_PIN);
  bool boolValueData = analogValueData > lightThreshold;
  
  if (boolValueClock)
  {
    if (!dataWasRead)
    {
      dataWasRead = true;

      currentChar = currentChar | ( boolValueData << currentCharPos );
      currentCharPos--;

      if (currentCharPos == -1)
      {
        Serial.print(currentChar);
        currentChar = 0;
        currentCharPos = 7;
      }
    }
  }
  else
  {
    dataWasRead = false;
  }
}
