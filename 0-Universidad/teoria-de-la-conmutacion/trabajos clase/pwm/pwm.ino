long pwm;

void setup(){

}

void loop() {
  // put your main code here, to run repeatedly:
  pwm = analogRead(A2);
  pwm = map(pwm,0,1023,0,255);
  analogWrite(2,pwm);
}
