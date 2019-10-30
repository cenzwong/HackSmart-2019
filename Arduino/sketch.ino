#include <Servo.h>

Servo myservo;  
int pos = 0;    
void setup() {
  myservo.attach(9);  
Serial.begin(9600);
}

void loop() {
 if(Serial.availble()){
switch()case{
case '1':
myservo.write(0);
break;
case '2':
myservo.write(180);
break;
case '23':
myservo.write(180);
break
}
}
}