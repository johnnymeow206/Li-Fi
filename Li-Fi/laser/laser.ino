void setup() 
{                
 pinMode(13, OUTPUT);  //  定義13腳為數位輸出介面

}
void loop() {
  digitalWrite(13, HIGH);   // 打開雷射頭
  delay(1000);              // 延时一秒
  digitalWrite(13, LOW);    // 關閉雷射頭
  delay(1000);              // 延时一秒
}
