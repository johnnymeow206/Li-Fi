int redPin=13;
int greenPin=4;
int bluePin=5;

int redPin1=10;
int greenPin1=9;
int bluePin1=8;


void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(redPin,OUTPUT);
pinMode(greenPin,OUTPUT);
pinMode(bluePin,OUTPUT);
}
 
void loop() {

  // put your main code here, to run repeatedly:

//red
  analogWrite(redPin,255);
  analogWrite(greenPin,0);
  analogWrite(bluePin,0);
  delay(1000);
//green
  analogWrite(redPin,0);
  analogWrite(greenPin1,255);
  analogWrite(bluePin1,0);
  delay(1000);
//blue
/*  analogWrite(redPin,0);
  analogWrite(greenPin,0);
  analogWrite(bluePin,255);
//magenta
  analogWrite(redPin,255);
  analogWrite(greenPin,0);
  analogWrite(bluePin,255);
//yellow
  analogWrite(redPin,255);
  analogWrite(greenPin,255);
  analogWrite(bluePin,0);
//cyan
  analogWrite(redPin,0);
  analogWrite(greenPin,255);
  analogWrite(bluePin,255);
//white
  analogWrite(redPin,255);
  analogWrite(greenPin,255);
  analogWrite(bluePin,255);
*/

}
