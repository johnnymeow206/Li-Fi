// RX
#include<IRremote.h>
IRsend irsend;
int i=0,r=0;
int d=40;
char rd;
void setup()
{
  Serial.begin(9600);

} 
void loop()
{
// int m=8, value=1, sum=0;
 irsend.sendSony(1, 2);
 delay(d);
 for(i=7; i>=0 ;i--)
 {
   if(analogRead(A0)>300)
     r=1;
    else
     r=0;
  delay(35);
  bitWrite(rd,i,r);
  
 }
 
  if(rd==47)
    Serial.println("");
  else
    Serial.print(rd);
 delay(d);
}