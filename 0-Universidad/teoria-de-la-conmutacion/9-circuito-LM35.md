# LM35

Sensor de temperatura. Sensa entre -55°C y 150°C y genera 10mV cada grado centigrado


# Mostrar código 

```c++
int cont;
int valor;
float voltaje= 0.0;
int temp=0;
int i;
int j;

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

    valor=analogRead(0);
    delay(200);
    voltaje= (valor*5.0)/1023;
    temp= (voltaje)/0.01;
    i= temp/10; //Decimas
    j= int(temp)%10; //unidades

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
```