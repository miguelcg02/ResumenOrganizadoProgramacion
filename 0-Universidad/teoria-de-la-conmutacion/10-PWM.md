# PWM

- Pulse Width modulation
- Es una señal periódica
- Su periodo siempre es constante, lo que se cambia es el tiempo de encendido de la señal cuadrada.
- Permite graduar
- Se le inyecta energia al sistema, dependiendo del tiempo.
- Duty cicle (El porcentaje que es el cambio del puslo).


```c++
long pwm;

void setup(){

}

void loop() {
  // put your main code here, to run repeatedly:
	pwm = analogRead(A2);
  pwm = map(pwm,0,1023,0,255);
	analogWrite(2,pwm);
}
```


```c++
#include <Servo.h>
Servo miServo;
#define M1 37
#define M2 36
#define M3 35
#define M4 34

void setup(){
  miServo.attach(3);
  pinMode(M1, INPUT);
  pinMode(M2, INPUT);
  pinMode(M3, INPUT);
  pinMode(M4, INPUT);
}

void loop() {
  if(digitalRead(M1)==HIGH){
  	miServo.write(45);
  }
  if(digitalRead(M2)==HIGH){
  	miServo.write(1);
  }
  if(digitalRead(M3)==HIGH){
  	miServo.write(120);
  }
  if(digitalRead(M4)==HIGH){
  	miServo.write(160);
  }
}
```