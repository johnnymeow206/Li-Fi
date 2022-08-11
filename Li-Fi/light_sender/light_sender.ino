/*
Author : Mohamad Nur Fitri bin Abd Halim
Title : Arduino Transimitter LIFI code
*/

int incomingByte = 0; // serial data that is receive from serial monitor
const int selangmasa=1; 
const int redPin=11;
const int greenPin=9;
const int bluePin=8;

void setup() 
{
  Serial.begin(9600);
  pinMode(redPin,OUTPUT);
  pinMode(greenPin,OUTPUT);
  pinMode(bluePin,OUTPUT);
}

void loop() 
{
  if (Serial.available() > 0) 
  {
    incomingByte = Serial.read(); 
    int a[10], i ;       
    for(i=0; incomingByte>0; i++)    
    {    
      a[i]=incomingByte%2;    
      incomingByte= incomingByte/2;  
    }    
  
    for(i=i-1 ;i>=0 ;i--)
    {   
      digitalWrite(redPin,HIGH);
   		delay(selangmasa);
   		digitalWrite(redPin,a[i]);
    	delay(2*selangmasa); 
    	digitalWrite(redPin,LOW);
   		delay(2*selangmasa);
    }    
  }  
}
