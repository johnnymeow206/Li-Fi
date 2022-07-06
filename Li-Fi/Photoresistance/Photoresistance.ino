int CDSPin = A15; // 光敏電阻接在A0接腳
int CDSVal = 0; // 設定初始光敏電阻值為0

void setup() {
  Serial.begin(9600);
}

void loop() { 
  CDSVal = analogRead(CDSPin);
  Serial.println(CDSVal);  
  delay(500); //每2s讀取一次       
}
