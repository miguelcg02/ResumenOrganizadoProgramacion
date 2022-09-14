# MOTORES PASO A PASO

- Los motores paso a paso son un tipo especial de motores que permiten el movimiento de su eje en ángulos muy precisos y por pasos, tanto a la izquierda como a la derecha. Aplicando a ellos una secuencia de pulsos. Cada paso tiene un ángulo muy preciso, determinado por la construcción del motor lo que permite realizar movimientos exactos. Son utilizados para generar movimientos precisos, por ejemplo en robots, en equipos con movimientos X-Y, entre otros.

* Motores Unipolares: este tipo de motor tiene dos bobinas en cada uno de los estatores y cada par de bobinas tienen un punto común, es decir, tiene 5 ó 6 terminales
* Motores Bipolares: este tipo de motor tiene dos bobinas y no poseen puntos comunes, es decir tiene cuatro terminales.
Para controlar este tipo de motor paso a paso bipolar es necesaria usar 8 transistores o circuitos integrados especiales.

# 4 estados

```c++
void setup(){
pinMode(22, OUTPUT); //define pin 22 como salida
pinMode(23, OUTPUT); //define pin 23 como salida
pinMode(24, OUTPUT); //define pin 24 como salida
pinMode(25, OUTPUT); //define pin 25 como salida
digitalWrite(22,LOW);
digitalWrite(23,LOW);
digitalWrite(24,LOW);
digitalWrite(25,LOW);

}

void loop() {
  // Primera i
  digitalWrite(22,HIGH);
  digitalWrite(23,HIGH);
  digitalWrite(24,LOW);
  digitalWrite(25,LOW);

  delay(2);
  
  digitalWrite(22,LOW);
  digitalWrite(23,HIGH);
  digitalWrite(24,HIGH);
  digitalWrite(25,LOW);

  delay(2);

  digitalWrite(22,LOW);
  digitalWrite(23,LOW);
  digitalWrite(24,HIGH);
  digitalWrite(25,HIGH);

  delay(2);

  digitalWrite(22,HIGH);
  digitalWrite(23,LOW);
  digitalWrite(24,LOW);
  digitalWrite(25,HIGH);

  delay(2);
}
```

# Ahora con hor/antihor y enmascaramiento

```c++
int cont;
const int sw = 37; //define sw para el pin 37
byte const horario[4] = {0b1100, 0b0110, 0b0011, 0b1001};
byte const antih[4] = {0b1001, 0b0011, 0b0110, 0b1100};
void setup()
{
pinMode(22, OUTPUT); //define pin 22 como salida
pinMode(23, OUTPUT); //define pin 23 como salida
pinMode(24, OUTPUT); //define pin 24 como salida
pinMode(25, OUTPUT); //define pin 25 como salida
pinMode(sw, INPUT); //define sw como entrada
}
10
Teoría de la Conmutación
11
void loop() {
if (digitalRead(sw) == HIGH) // Pregunta si SW esta encendido
{
cont = 0; // Se pone cont en cero
while (cont < 4 && digitalRead(sw) == HIGH) // Mientras que cont sea menor a 4 y sw este encendido
{
PORTA = (horario[cont]); // Envíe al PORTA la información de la tabla de horario
delay(100); // Retardo de 100 milisegundos
cont++; // Incremente la variable cont
}
}
else // de lo contrario
{
cont = 0; // la variable cont=0
while (cont < 4 && digitalRead(sw) == LOW) // Mientras que cont sea menor a 4 y sw este apagado
{
PORTA = (antih[cont]); // Envíe al PORTA la información de la tabla de antih
delay(100); // Retardo de 100 milisegundos
cont++; // Incremente la variable cont
}
}
}
```

```c++
int cont;

int pA = 29;
int pB = 28;
int pC = 27;
int pD = 26;
int pE = 25;
int pF = 24;
int pG = 23;
int eD = 30; //Izq
int eI = 31; //Derecha
long double t1,t2;

byte display[10]= {0b1111110,0b0110000,0b1101101,0b1111001,0b0110011,0b1011011,0b0011111,0b1110000,0b1111111,0b1110011};

void setup(){
  pinMode(pA, OUTPUT); //define pin 43 como salida
  pinMode(pB, OUTPUT); //define pin 44 como salida
  pinMode(pC, OUTPUT); //define pin 45 como salida
  pinMode(pD, OUTPUT); //define pin 46 como salida
  pinMode(pE, OUTPUT); //define pin 47 como salida
  pinMode(pF, OUTPUT); //define pin 48 como salida
  pinMode(pG, OUTPUT); //define pin 49 como salida
  pinMode(30, OUTPUT); //define pin 48 como salida
  pinMode(31, OUTPUT); //define pin 49 como salida
  digitalWrite(eI,HIGH);
  digitalWrite(eD,LOW);
}

void loop(){
  for(int i=0; i<10;i++){
    for(int j=0; j<10;j++){
        t1=millis();
        t2=millis();
        while(t1-t2<200){
          mostrar_numer(i);
          digitalWrite(eI,HIGH);
          digitalWrite(eD,LOW);
          delay(2);
          mostrar_numer(j);
          digitalWrite(eI,LOW);
          digitalWrite(eD,HIGH);
          delay(2);
          t1=millis();
        }
    }
  } 
}

void mostrar_numer(int digito){
  digitalWrite(pA, display[digito] & 0b1000000);
  digitalWrite(pB, display[digito] & 0b0100000);
  digitalWrite(pC, display[digito] & 0b0010000);
  digitalWrite(pD, display[digito] & 0b0001000);
  digitalWrite(pE, display[digito] & 0b0000100);
  digitalWrite(pF, display[digito] & 0b0000010);
  digitalWrite(pG, display[digito] & 0b0000001);
}
```