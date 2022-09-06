//please check with video if theres any change. 
//If any, follow the code from video.

#define SOLARPIN 13
#define THRESHOLD 0

int ambientReading = 0;
int CDSVal = 0;
long delay_time = 3;
long delay_times= 1000;


void setup() {
  DDRA &= B00000001;
  pinMode(SOLARPIN, INPUT);
  Serial.begin(115200);  
  //CDSVal = analogRead(SOLARPIN);
  //Serial.println(CDSVal);  
}

void loop() {

  int reading = digitalRead(SOLARPIN);

  int bits[8];

  //Listening for the start bit
  if(reading > THRESHOLD)  {
    for (int i =0; i<8 ; i++) {
      if (PINA & B00000001) {
        bits[i] = 1 ;
      }
      else {
        bits[i] = 0;
      }
      //delay(delay_time);
      delayMicroseconds(delay_times);
      
    }

    int m = 0;
    for (int j = 1; j <8; j++) {
      if (bits[j] ==1) {
        m = m + (1<<(7-j));
      }
    }
  
    char n=m;
    Serial.println(n);
    //Serial.println(m);
  
  }
} 
