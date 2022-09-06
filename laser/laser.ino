long delay_time=30;
void setup() 
{                
 pinMode(13, OUTPUT);  //  定義13腳為數位輸出介面
 //DDRB = DDRB | B10000000;  //This is safer as it sets ONLY pins B7 as OUTPUT
}
void loop() {
  digitalWrite(13, HIGH);// 打開雷射頭
  
  //PORTB |= B10000000;         //Sets only B7 to HIGH
  delayMicroseconds(delay_time);          // 延时一秒
  digitalWrite(13, LOW);    // 關閉雷射頭
  //PORTB &= B01111111;         //Sets only B7 to LOW
  delayMicroseconds(delay_time);// 延时一秒
}
