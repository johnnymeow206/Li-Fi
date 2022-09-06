//please check with video if theres any change. 
//If any, follow the code from video.

#define SOLARPIN D22
#define THRESHOLD 0

int ambientReading = 0;
long delay_time = 10; // for delay
long delay_times= 1000; //for delayMicroseconds


void setup() {
  //DDRA &= B00000001;
  pinMode(SOLARPIN, INPUT);
  Serial.begin(115200);  
}

void loop() {

  int reading = digitalRead(SOLARPIN);

  String receive = "" ;
  String old_receive = "" ;

  //Listening for the start bit
  if(reading == true)  {
      if (digitalRead(SOLARPIN) == true) {
        
        Serial.print('1');
      }
      else {
        Serial.print('0');
      }

      delay(delay_time);
      
      
            }

  
}