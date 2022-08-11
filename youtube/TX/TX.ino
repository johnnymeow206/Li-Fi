// TX
#include <IRremote.h>
int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
decode_results results;
int ledpin=8,i=0;
char data[]="/ABCD/";
int len=sizeof(data);
int d=10;
void setup()
{
  Serial.begin(9600);
  //Serial.println(s);
  pinMode(ledpin,OUTPUT);
  Serial.println("Enabling IRin");
  irrecv.enableIRIn();
}
void loop()
{
  delay(d);
  if (irrecv.decode(&results)) 
  {
    irrecv.resume(); 
  }
  
  if(results.value==1)
   { 
    if(len==(i+1))
       i=0;
     if(data[i]!='\0')
      {
        int ascii=data[i];// store acsii to c

        for(int j=7 ; j>=0 ;j--)
         {
          int l=bitRead(ascii,j);
          digitalWrite(ledpin,l);     
          delay(35);
         }
         i++;
        }
    }
   results.value=0;
   delay(d);

}
