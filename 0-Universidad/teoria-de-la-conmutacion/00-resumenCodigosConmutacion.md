# PRENDER Y APAGAR MOTOR CON RETARDO USANDO LA FUNCIÓN MILLIS

```c++
int motor = 22; // motor en el pin 22
int inicio = 37; // inicio en el pin 37
int detener = 36; // detener en el pin 36
unsigned int tiempoActual = 0;
unsigned int tiempoAnterior = 0;

void setup() {// configura los pines usados
    pinMode(motor, OUTPUT); // configura el motor como salida
    pinMode(inicio, INPUT); // configura el pulsador inicio como entrada
    pinMode(detener, INPUT); // configura el pulsador detener como entrada
    digitalWrite(motor, LOW); // desactiva el motor
}

void Retardo_10s() {//Función Retardo_10s (10 segundos)
    tiempoAnterior=millis();
    tiempoActual=millis();
    while(tiempoActual-tiempoAnterior<10000&&digitalRead(detener)==LOW){
        tiempoActual=millis();
    }
}

void loop(){// inicia el bucle del programa
    if(digitalRead(inicio)==HIGH){
        digitalWrite(motor, HIGH); // activa el motor
        Retardo_10s();
        digitalWrite(motor, LOW); // activa el motor
    }
}
```

# GENERACION DE NUMEROS ALEATORIOS CON RANDOM SEED

Para generar números aleatorios en el Arduino se usa la función random().

La función random(min,max), genera un numero aleatorio entre un valor min y un valor max
Parámetros:
    min - límite inferior del valor aleatorio, inclusive (opcional)
    max - límite superior del valor aleatorio, exclusive (se devuelve hasta el anterior)

Para generar el numero aleatorio se necesita una semilla o un punto de partida que debe ser
diferente cada vez que se llame la función random(), y así garantizar que el numero generado pueda
ser diferente.

Una forma de generar la semilla es llamando la función millis() cada vez que se oprime el pulsador
que genera el numero aleatorio.

```c++
int inicio = 37; //Pulsador en el pin 37
int numero;
void setup(){
    pinMode(inicio, INPUT); // configura el pulsador de inicio como entrada
    Serial.begin(9600);
}
void loop() { //Hacer por siempre
    if(digitalRead(inicio)==HIGH){
    randomSeed(millis()); // genera una semilla para aleatorio a partir de la función millis()
    numero = random(0,10); // genera número aleatorio entre 0 y 9
    Serial.println(numero);
    delay(500);
    }
}
```

# Controlar un motor paso a paso conectado a los cuatro bits menos significativos del PORTA

```c++
int cont;
const int sw = 37; //define sw para el pin 37
byte const horario[4] = {0b1100, 0b0110, 0b0011, 0b1001};
byte const antih[4] = {0b1001, 0b0011, 0b0110, 0b1100};
void setup(){
    pinMode(22, OUTPUT); //define pin 22 como salida
    pinMode(23, OUTPUT); //define pin 23 como salida
    pinMode(24, OUTPUT); //define pin 24 como salida
    pinMode(25, OUTPUT); //define pin 25 como salida
    pinMode(sw, INPUT); //define sw como entrada
}

void loop() {
    if (digitalRead(sw) == HIGH) {// Pregunta si SW esta encendido
    cont = 0; // Se pone cont en cero
    while (cont < 4 && digitalRead(sw) == HIGH) { // Mientras que cont sea menor a 4 y sw este encendido
        PORTA = (horario[cont]); // Envíe al PORTA la información de la tabla de horario
        delay(100); // Retardo de 100 milisegundos
        cont++; // Incremente la variable cont
    }
    }
    else { // de lo contrario
    cont = 0; // la variable cont=0
        while (cont < 4 && digitalRead(sw) == LOW) {// Mientras que cont sea menor a 4 y sw este apagado
        PORTA = (antih[cont]); // Envíe al PORTA la información de la tabla de antih
        delay(100); // Retardo de 100 milisegundos
        cont++; // Incremente la variable cont
        }
    }
}
```
# CONTADOR MULTIPLEXAJE 2 SEGEMENTOS (SOLUCION PROPIA) 

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

# CONTADOR MULTIPLEXAJE 2 SEGEMENTOS (SOLUCION PROFE)

```c++
int cont; // Declarar la variable cont como un entero, es decir de 8 bits
int tdec = 23; // tdec en el pin 23
int tuni = 24; // tdec en el pin 23
byte display[10]= {63,06,91,79,102,109,125,07,127,103};
int uni,dec; // Declarar las variables uni,dec como un entero, es decir de 8bits
void setup(){
    pinMode(tuni, OUTPUT); // configura el tuni como salida
    pinMode(tdec, OUTPUT); // configura el tdec como salida
    pinMode(43, OUTPUT); //define pin 43 como salida
    pinMode(44, OUTPUT); //define pin 44 como salida
    pinMode(45, OUTPUT); //define pin 45 como salida
    pinMode(46, OUTPUT); //define pin 46 como salida
    pinMode(47, OUTPUT); //define pin 47 como salida
    pinMode(48, OUTPUT); //define pin 48 como salida
    pinMode(49, OUTPUT); //define pin 49 como salida
}

void loop() { //haga por siempre
    cont = 57;
    dec = cont / 10;
    uni = cont % 10;
    digitalWrite(tdec, LOW); // apaga el display de decenas
    digitalWrite(tuni, HIGH); // enciende el display de unidades
    PORTL = (display[uni]); // Muestra lo que hay en unidades
    delay(1); //retardo de 1 milisegundo
    digitalWrite(tuni, LOW); // apaga el display de unidades
    digitalWrite(tdec, HIGH); // enciende el display de decenas
    PORTL = (display[dec]); // Muestra lo que hay en decenas
    delay(1); //retardo de 1 milisegundo
}
```

# LM35 FORMULA PARA CONVERSION ANALOGA

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

# LEER TEMPERATURA Y MOSTRARLO REPRESENTADO CON COLORES RGB

```c++
int valor;
float voltaje= 0.0;
int temp;

void setup(){
  Serial.begin(9600);
}
//20-25 -> verde
//>25 -> naranja
//>30 -> rojo
//<20 -> morado
void loop() {
  // put your main code here, to run repeatedly:
  valor=analogRead(0);
  //delay(200);
  voltaje= (valor*5.0)/1023;
  temp= (voltaje)/0.01;
  Serial.println(temp);

  if(temp<20){
    Serial.println("morado");
    analogWrite(2,255);//red
    analogWrite(3,0);//green
    analogWrite(4,255);//blue
  }
  else if(temp >= 20 && temp <= 25){
    Serial.println("verde");
    analogWrite(2,0);//red
    analogWrite(3,255);//green
    analogWrite(4,0);//blue
  }
  else if(temp > 25 && temp <= 30){
    Serial.println("naranja");
    analogWrite(2,255);//red
    analogWrite(3,128);//green
    analogWrite(4,0);//blue
  }
  else{ 
    Serial.println("rojo");
    analogWrite(2,255);//red
    analogWrite(3,0);//green
    analogWrite(4,0);//blue
  }
}
```

# PWM

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

# LEER POTENCIOMETRO

```C++
int pwmAzul = A0;
int pwmRojo = A1;
int potenciometro=0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  potenciometro=analogRead(pwmAzul);
  Serial.print("Valor Analogo");
  Serial.println(potenciometro);
  delay(200);
}
```

# SERVOMOTOR

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

# MANEJO DE LCD

#include <LiquidCrystal.h> : Esta línea permite agregar en el proyecto la librería, que facilita en control del display
de cristal liquido.
LiquidCrystal lcd(RS, E, D4, D5, D6, D7); : Definir los pines en los que se conecta los pines del display de cristal liquido.
lcd.begin(16, 2); : Definir el numero de columnas y filas del display de cristal liquido.
lcd.setCursor(0, 1); : Define la posición inicial en la que se muestra el mensaje columna, fila.
lcd.print("Cadena de caracteres"); Muestra la cadena de caracteres que se pone dentro de las comillas.
lcd.print(Variable); Imprimir el valor que contiene una variable tipo entero.
lcd.print(Variable,DEC);Imprimir el valor que contiene una variable tipo decimal.
lcd.clear(); Limpiar pantalla
lcd.write(48); Imprimir el carácter Ascii del valor en este caso imprime el 0.
lcd.noCursor(); No aparecer el cursor en pantalla.
lcd.cursor();: Aparecer cursor en pantalla.
lcd.display(); y lcd.noDisplay(); : Mostrar mensaje en la pantalla de cristal liquido y no mostrar el mensaje respectivamente.
lcd.home(); ; ir a la posición columna 0 a fila 0.
lcd.leftToRight(); : Escribir los caracteres de derecha a izquierda en la pantalla de cristal liquido.
lcd.rightToLeft(); : Escribir los caracteres de izquierda a derecha en la pantalla de cristal liquido.

* PINES PARA CONECTAR EL LCD USADOS EN LOS EJEMPLOS
/*
LCD RS al pin digital 48  Corresponde a L1
LCD Enable al pin digital 49  Corresponde a L0
LCD D4 al pin digital 45  Corresponde a L4
LCD D5 al pin digital 44  Corresponde a L5
LCD D6 al pin digital 43  Corresponde a L6
LCD D7 al pin digital 42  Corresponde a L7
LCD R/W al pin digital 47  Corresponde a L2
VDD a +5V
VSS a tierra
VEE a trimer
*/
LiquidCrystal lcd(48,49,45,44,43,42);
LiquidCrystal lcd(RS,E, D4,D5,D6,D7);

```c++
#include <LiquidCrystal.h> //Agrega la librería del LCD
LiquidCrystal lcd(48,49,45,44,43,42); //Inicializa la librería y define los pines digitales para el LCD

int pwm1 = A0;
int pwm2 = A1;
int pot1,pot2;

void setup() {
  pinMode(pwm1,INPUT);
  pinMode(pwm2,INPUT);
  Serial.begin(9600);
  pinMode(47, OUTPUT);
  digitalWrite(47, 0);
  lcd.begin(16,2);

}

void loop() {
  pot1=analogRead(pwm1);
  pot1=map(pot1,0,1023,0,100);
  pot2=analogRead(pwm2);
  pot2=map(pot2,0,1023,0,1000);
  
  Serial.print("potencia 1: ");
  Serial.println(pot1);

  Serial.print("potencia 2: ");
  Serial.println(pot2);

  delay(2000);
  
  lcd.clear();
  lcd.setCursor(3,0); //Ubica el cursor en la columna 3 de la fila 0
  lcd.print(pot1); //Muestra el mensaje “UNIVERSIDAD"
  lcd.setCursor(3, 1); //Ubica el cursor en la fila 1 de la columna 1
  lcd.print(pot2); //Muestra el mensaje " EAFIT-MEDELLIN "
  delay(2000);
}
```





# ############################################################################################################################################# #

# TALLER 2 - PUNTO Y FAMA

```c++
int numeroRandom; //El digito que genera el sistema
int intentos; // numero de intentos que el usuario desea
long double ti,tf;// definimos los tiempos que se toman con millis
int tiempo;// definimos la diferencia de tiempos
bool adivino;//variable que nos indica si adivinó o no en los intentos que desea el usuario
String generada,ingresada;//cadenas que comparamos
int pica, fama;//número de picas y de famas por cada intento

void setup(){
  Serial.begin(9600);// inicializamos monitor serial
}

void loop(){ //Hacer por siempre
  bool revisar[] = {false,false,false,false,false,false,false,false,false,false};//usamos un arreglo que verificará que los 4 números serán diferentes
  generada = "";
  randomSeed(millis()); // genera una semilla para aleatorio a partir de la función millis()
  
  while (generada.length() != 4){ //Genera el string con los 4 num diferentes
    numeroRandom = random(0,10); // genera número aleatorio entre 0 y 9
    if (revisar[numeroRandom]==false){ //Se revisa que el número no se ha usado mediante el arreglo revisar[], para que cada digito sea diferente
      revisar[numeroRandom] = true;
      generada += String(numeroRandom);// se agrega el número a la cadena generada 
    }
  }

  do{// repetimos la petición hasta ingresar correctamente un número posible de intentos
    Serial.print("Ingrese el número de intentos que desee: ");
    while(Serial.available()==0){ // Se para el serial hasta que coloque el numero de intento que desea
      
    }
    intentos=Serial.parseInt();// se ingresan los intentos que desea hacer el usuario
    Serial.println(intentos);
    Serial.readStringUntil('\n');//limpiamos el serial

    if(intentos<0){ //Se hace la restriccion de que solo reciba un numero positivo
      Serial.println("no puedes tener intentos negativos, por favor inténtalo de nuevo");
    }else{
      break;//Salimos de la petición
    }
  }while(true);
  
  ti=millis();// se comienza a tomar el tiempo

  adivino=false;//se inicializa nuestro verificador en false

  while(intentos--){//se repiten las siguientes preguntas segun el numero de intentos
    Serial.println("----");// se muestra los campos a llenar

    do{//repetimos la consideración del usuario hasta que ingrese 4 dígitos estrictamente

      while(Serial.available()==0){
    
      }
      ingresada = Serial.readStringUntil('\n');// se ingresan los numeros que el usuario cree

      if(ingresada.length()==4){
        break;
      }else{
        Serial.println("Por favor ingrese nuevamente la cadena, recuerde que deben ser 4 digitos");
      }
    }while(true);
    
    pica=0;//iniciamos picas en 0
    fama=0;//iniciamos famas en 0
    for(int i=0; i<4; i++){//revisamos dígito a dígito la cadena ingresada
      if(generada.indexOf(ingresada[i])>=0){//revisamos si el dígito actual está en la generada
        if(generada.indexOf(ingresada[i])==i){//revisamos si aparte de estar, está en la misma posición que estamos revisando
          fama++;//si cumple lo último aumenta la fama
        }else{
          pica++;// si simplemente está aumenta la pica
        }
      }//de lo contrario no aumenta ninguna variable
    }

    if(fama==4){//si hay 4 famas indicamos que adivinó el número 
      tf=millis();
      tiempo=(tf-ti)/1000;//encontramos el tiempo que transcurrió entre ti y tf y lo pasamos a segundos
      Serial.print("¡Lo has adivinado en ");
      Serial.print(tiempo);
      Serial.println(" segundos!");
      Serial.print("El número era: ");
      Serial.println(generada);

      adivino=true;//indicamos a nuestro verificador que se ha adivinado el número
      break;//dejamos de preguntar el número de intentos y salimos
    
    }else{// si no adivina el número

      Serial.println(ingresada);//mostramos el número ingresado

      if(fama==0 && pica==0){//si no hay picas ni famas, no se adivinó nada
        Serial.println("No adivinaste nada");
      }else{//de lo contrario se muestran el número correspondiente de picas y famas
        if(fama==0){
          Serial.print(pica);
          Serial.println(" Pica(s)");
        }else if(pica==0){
          Serial.print(fama);
          Serial.println(" Fama(s)");
        }else{
          Serial.print(pica);
          Serial.print(" Pica(s) y ");
          Serial.print(fama);
          Serial.println(" Fama(s)");
        }
      }
    }
  }

  if(!adivino){//si finalmente el usuario no adivino en los intentos que el establecio
    tf=millis();
    tiempo=(tf-ti)/1000;//encontramos el tiempo que transcurrió entre ti y tf y lo pasamos a segundos
    Serial.print("Se acabaron tus intentos, te tardaste: ");
    Serial.print(tiempo);
    Serial.println(" segundos");
    Serial.print("El número era: ");
    Serial.println(generada);//y mostramos cuál fue el número que no se adivinó
  }

  Serial.println("Fin del juego\n.......................................................................................");
  
}
```

# TALLER 2 - MOTOR (SUBE/BAJA) Y LEDS

```c++
int msup = 37;
int msdown = 36;
int p1 = 35;
int p2 = 34;
int p3 = 33;
int p4 = 32;

int up = 22;
int down = 23;
int l1 = 24;//subiendo
int l2 = 25;//bajando
int l3 = 26;//apagado
int l4 = 27;//pausado

unsigned long tiempoI;
unsigned long tiempoA;

void setup() {
    Serial.begin(9600);
    
    //Salidas
    pinMode(up, OUTPUT);
    pinMode(down, OUTPUT);
    pinMode(l1, OUTPUT);
    pinMode(l2, OUTPUT);
    pinMode(l3, OUTPUT);
    pinMode(l4, OUTPUT);
    
    // Entradas
    pinMode(msup, INPUT);
    pinMode(msdown, INPUT);
    pinMode(p1, INPUT);
    pinMode(p2, INPUT);
    pinMode(p3, INPUT);
    pinMode(p4, INPUT);

    digitalWrite(l1,LOW);
    digitalWrite(l2,LOW);
    digitalWrite(l3,LOW);
    digitalWrite(l4,LOW);
    digitalWrite(up,LOW);

    //Que baje el motor
    bajar();
}

void loop() {    
    // Funcionalidad 1
    if(digitalRead(p1)==HIGH){
      rutina1();
    }

    //Funcionalidad 2
    if(digitalRead(p2)==HIGH){
      rutina2();
    }

    led(l3);//encendemos led 3
    Serial.println("detenido");
}

void retardo_2s(){
  tiempoI = millis(); // Aqui se declara en 0 porque arranca, o ya cuando lleve más tiempo por el bucle
  tiempoA = millis(); // Aqui se declara en 0 porque arranca, o ya cuando lleve más tiempo por el bucle

  while((tiempoA-tiempoI)<2000){ // Que no hayan pasado los 2 segs y que el boton de detener no este presionado
    tiempoA = millis(); // Aqui lo actualizamos dependiendo de cuanto lleve corriendo
    led(l3);//encendemos led 3
    Serial.println("detenido");
  }
}

void subir(){
  led(l1);//encendemos led 1
  digitalWrite(up,HIGH);
  while(digitalRead(msup)==LOW){ // mientras sube (Funcionalidad 3)
    Serial.println("subiendo");
    if(digitalRead(p3)==HIGH){
      digitalWrite(up,LOW);
      led(l4);//encendemos led 4
      while(digitalRead(p4)==LOW){// mientras que no se despause
        Serial.println("en pausa");
      }
      led(l1);//encendemos nuevamente led 1
      digitalWrite(up,HIGH);// continua la rutina
    }
  }
  digitalWrite(up,LOW);
}

void bajar(){
  led(l2);//encendemos led 2
  digitalWrite(down,HIGH);
  while(digitalRead(msdown)==LOW){ // mientras baja (Funcionalidad 3)
    Serial.println("bajando");
    if(digitalRead(p3)==HIGH){
      led(l4);//encendemos led 4
      digitalWrite(down,LOW);
      while(digitalRead(p4)==LOW){// mientras que no se despause
        Serial.println("en pausa");
      }
      led(l2);//encendemos nuevamente led 2
      digitalWrite(down,HIGH);// continua la rutina
    }
  }
  digitalWrite(down,LOW);
}

void led(int x){
  //apagamos todos los leds
  digitalWrite(l1,LOW);
  digitalWrite(l2,LOW);
  digitalWrite(l3,LOW);
  digitalWrite(l4,LOW);
  //encendemos el led deseado
  digitalWrite(x,HIGH);
}

void rutina1(){
  subir();
  bajar();
}

void rutina2(){
  subir();
  retardo_2s();
  bajar();
  retardo_2s();
  subir();
  retardo_2s();
  bajar();
  retardo_2s();
}
```

# ############################################################################################################################################# #


# TALLER 3 - SEMAFORO

```c++
// Display 
int pA = 49;
int pB = 48;
int pC = 47;
int pD = 46;
int pE = 45;
int pF = 44;
int pG = 43;
int unidades = 30;
int decenas = 31;

byte display[10]= {0b1111110,0b0110000,0b1101101,0b1111001,0b0110011,0b1011011,0b0011111,0b1110000,0b1111111,0b1110011};

// Funcionalidad semaforo
// BC -> bombillo carro
// BP -> bombillo peatón
int on = 36;
int BCgreen = 22;
int BCyellow = 23;
int BCred = 24;
int BPgreen = 25;
int BPred = 26;
long double t1,t2;

void setup() {
  pinMode(pA, OUTPUT); 
  pinMode(pB, OUTPUT); 
  pinMode(pC, OUTPUT); 
  pinMode(pD, OUTPUT); 
  pinMode(pE, OUTPUT); 
  pinMode(pF, OUTPUT); 
  pinMode(pG, OUTPUT);
  pinMode(unidades, OUTPUT); 
  pinMode(decenas, OUTPUT);
  
  digitalWrite(unidades,LOW);
  digitalWrite(decenas,LOW);
  
  pinMode(on, INPUT);
  pinMode(BCgreen, OUTPUT);
  pinMode(BCyellow, OUTPUT);
  pinMode(BCred, OUTPUT);
  pinMode(BPgreen, OUTPUT);
  pinMode(BPred, OUTPUT);
  
  digitalWrite(BCgreen, LOW);
  digitalWrite(BCyellow, LOW);
  digitalWrite(BCred, LOW);
  digitalWrite(BPgreen, LOW);
  digitalWrite(BPred, LOW);

}

void loop() {
  
  if(digitalRead(on)==HIGH){ //Mientras esta encendido el suiche
    digitalWrite(BCred, HIGH);
    digitalWrite(BPgreen, HIGH);
    esperar(15000.0);
    
    for (int i = 0; i < 6; i++){
      digitalWrite(BPgreen, HIGH);
      esperar(500.0);
      digitalWrite(BPgreen,LOW); //Va a quedar apagado cuando salga del for
      esperar(500.0);
    }
    
    digitalWrite(BPred, HIGH);
    esperar(2000.0);
    digitalWrite(BCred, LOW);
    digitalWrite(BCgreen, HIGH);
    
    esperar(15000.0);
    
    for (int i = 0; i < 6; i++){
      digitalWrite(BCgreen, HIGH);
      esperar(500.0);
      digitalWrite(BCgreen,LOW); //Va a quedar apagado cuando salga del for
      esperar(500.0);
    }
    
    digitalWrite(BCyellow, HIGH);
    esperar(2000.0);
    digitalWrite(BCyellow, LOW);// Se apaga para que inicie el ciclo con todos apagados
    digitalWrite(BPred,LOW);// Se apaga para que inicie el ciclo con todos apagados
    digitalWrite(unidades,LOW);
    digitalWrite(decenas,LOW);
  }

}

void esperar(float tiempoEspera){
  t1=millis();
  t2=millis();
  int tiempoRestante;
  int u, d;
  while(t1-t2<tiempoEspera){
    tiempoRestante = int(tiempoEspera - (t1-t2)); // se guarda la cuenta regresiva del tiempo que queda
    tiempoRestante = tiempoRestante/1000; //se pasa a segundos
    d = tiempoRestante/10; 
    u = tiempoRestante%10;
    mostrar_numer(u);
    digitalWrite(unidades,HIGH);
    digitalWrite(decenas,LOW);
    delay(2);
    mostrar_numer(d);
    digitalWrite(unidades,LOW);
    digitalWrite(decenas,HIGH);
    delay(2);
    t1=millis();
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

# TALLER 3 - JUEGO RARO CON EL DISPLAY 7 SEGMENTOS

```C++
// Display 
int pA = 29;
int pB = 28;
int pC = 27;
int pD = 26;
int pE = 25;
int pF = 24;
int pG = 23;
int unidades = 30;
int decenas = 31;

// display[10] = E
// display[11] = j
byte display[12]= {0b1111110,0b0110000,0b1101101,0b1111001,0b0110011,0b1011011,0b0011111,0b1110000,0b1111111,0b1110011,0b1001111,0b0111000};

// Juego
// P -> pulsador
// n -> el número que se comparará para saber quién gana
int Pjug1 = 34;
int Pjug2 = 36;
int nJug1 = 0; 
int nJug2 = 0;
int numeroRandom;

long double t1,t2;

void setup() {

  Serial.begin(9600);

  pinMode(pA, OUTPUT); 
  pinMode(pB, OUTPUT); 
  pinMode(pC, OUTPUT); 
  pinMode(pD, OUTPUT); 
  pinMode(pE, OUTPUT); 
  pinMode(pF, OUTPUT); 
  pinMode(pG, OUTPUT);
  pinMode(unidades, OUTPUT); 
  pinMode(decenas, OUTPUT);
  
  digitalWrite(unidades,LOW);
  digitalWrite(decenas,LOW);
  
  pinMode(Pjug1, INPUT);
  pinMode(Pjug2, INPUT);
  
}

void loop() {

  if (digitalRead(Pjug1) == HIGH && nJug1 == 0){ //el jugador 1 pulsa para guardar su número solo 1 vez por juego
    randomSeed(millis()); //iniciamos el pseudorandomizado
    numeroRandom = random(1,10);
    nJug1 = numeroRandom;//guardamos las unidades del número
    mostrar_numer(numeroRandom);//dejamos el display mostrando solo las unidades
    digitalWrite(unidades,HIGH);
    digitalWrite(decenas,LOW);
    while(digitalRead(Pjug1) == HIGH){//en caso de palanca, sino comentar este while
      Serial.println("espera 1");
    }
    while(digitalRead(Pjug1) == LOW){//esperamos hasta que se vuelva a pulsar
      Serial.println("espera 2");
    }
    
    numeroRandom = random(1,10);
    nJug1 = nJug1 + (numeroRandom*10);//agregamos las decenas del número

    t1=millis();
    t2=millis();
    while(t1-t2<1000){//mostramos el número final por 1 segundo
      mostrar_numer(nJug1%10);
      digitalWrite(unidades,HIGH);
      digitalWrite(decenas,LOW);
      delay(2);
      mostrar_numer(nJug1/10);
      digitalWrite(unidades,LOW);
      digitalWrite(decenas,HIGH);
      delay(2);
      t1=millis();
    }    
    digitalWrite(unidades,LOW);//apagamos el display
    digitalWrite(decenas,LOW);
  }
  
if (digitalRead(Pjug2) == HIGH && nJug2 == 0){ //el jugador 1 pulsa para guardar su número solo 1 vez por juego
    randomSeed(millis());//iniciamos el pseudorandomizado
    numeroRandom = random(1,10);
    nJug2 = numeroRandom;//guardamos las unidades del número
    mostrar_numer(numeroRandom);//dejamos el display mostrando solo las unidades
    digitalWrite(unidades,HIGH);
    digitalWrite(decenas,LOW);

    while(digitalRead(Pjug2) == HIGH){//en caso de palanca, sino comentar este while
      Serial.println("espera 1");
    }
    
    while(digitalRead(Pjug2) == LOW){//esperamos hasta que se vuelva a pulsar
      Serial.println("espera 2");
    }
    
    numeroRandom = random(1,10);
    nJug2 = nJug2 + (numeroRandom*10);//agregamos las decenas del número

    t1=millis();
    t2=millis();
    while(t1-t2<1000){//mostramos el número final por 1 segundo
      mostrar_numer(nJug2%10);
      digitalWrite(unidades,HIGH);
      digitalWrite(decenas,LOW);
      delay(2);
      mostrar_numer(nJug2/10);
      digitalWrite(unidades,LOW);
      digitalWrite(decenas,HIGH);
      delay(2);
      t1=millis();
    }    
    digitalWrite(unidades,LOW);//apagamos el display
    digitalWrite(decenas,LOW);
  }
  
  if(nJug1 != 0 && nJug2 != 0){//cuando ambos jugadores ya tienen su número
    if(nJug1 > nJug2){//se revisa si gano j1
      Serial.println("gano j1");
      for(int i = 0; i < 3; i++){//titila 3 veces
        t1=millis();
        t2=millis();
        while(t1-t2<500){//se deja encendido j1 por medio segundo
          mostrar_numer(1);
          digitalWrite(unidades,HIGH);
          digitalWrite(decenas,LOW);
          delay(2);
          mostrar_numer(11);
          digitalWrite(unidades,LOW);
          digitalWrite(decenas,HIGH);
          delay(2);
          t1=millis();
        }
        digitalWrite(unidades, LOW);//apagamos el display y se espera 1 segundo
        digitalWrite(decenas, LOW);//era medio segundo pero,
        while(t1-t2<1000){//le subimos, sino no titila
          t1=millis();
        }
      }

      nJug1=0;//ya que finalizó el juego reiniciamos los valores de los jugadores
      nJug2=0;
    }
    
    else if(nJug1 < nJug2){//se revisa si gano j2
      Serial.println("gano j2");
      for(int i = 0; i < 3; i++){//titila 3 veces
        t1=millis();
        t2=millis();
        while(t1-t2<500){//se deja encendido j2 por medio segundo
          mostrar_numer(2);
          digitalWrite(unidades,HIGH);
          digitalWrite(decenas,LOW);
          delay(12);
          mostrar_numer(11);
          digitalWrite(unidades,LOW);
          digitalWrite(decenas,HIGH);
          delay(2);
          t1=millis();
        }
        digitalWrite(unidades, LOW);//apagamos el display y se espera 1 segundo
        digitalWrite(decenas, LOW);//era medio segundo pero,
        while(t1-t2<1000){//le subimos, sino no titila
          t1=millis();
        }
      }

      nJug1=0;//ya que finalizó el juego reiniciamos los valores de los jugadores
      nJug2=0;
    }
    
    else{//si no ganó nadie, quedó en empate
      Serial.println("empate");
      for(int i = 0; i < 3; i++){//titila 3 veces
        t1=millis();
        t2=millis();
        while(t1-t2<500){//se deja encendido EE por medio segundo
          mostrar_numer(10);
          digitalWrite(unidades,HIGH);
          digitalWrite(decenas,HIGH);
          delay(2);
          t1=millis();
        }
        digitalWrite(unidades, LOW);//apagamos el display y se espera 1 segundo
        digitalWrite(decenas, LOW);//era medio segundo pero,
        while(t1-t2<1000){//le subimos, sino no titila
          t1=millis();
        }
      }
      nJug1=0;//ya que finalizó el juego reiniciamos los valores de los jugadores
      nJug2=0;
    }
    
  }
}


void mostrar_numer(int digito){//enmascaramiento
  digitalWrite(pA, display[digito] & 0b1000000);
  digitalWrite(pB, display[digito] & 0b0100000);
  digitalWrite(pC, display[digito] & 0b0010000);
  digitalWrite(pD, display[digito] & 0b0001000);
  digitalWrite(pE, display[digito] & 0b0000100);
  digitalWrite(pF, display[digito] & 0b0000010);
  digitalWrite(pG, display[digito] & 0b0000001);
}
```
# #################################################################################################
# Codigo poema lcd I2C

```c++
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
// se llama 27
LiquidCrystal_I2C lcd(0x27, 20, 4);

String string[]={
"antigua quien dijo:",
"dos enormes ",
"piernas petreas, ",
"sin su tronco se ",
"yerguen en el ",
"desierto.A su lado,",
"en la arena,",
"semihundido, yace ",
"un rostro hecho ",
"pedazos, cuyo ceno",
"y mueca en la boca,",
"y desden de frio ",
"dominio,cuentan que",
"su escultor ",
"comprendio bien ",
"esas pasiones las",
"cuales aun ",
"sobreviven,grabadas",
"en estos inertes ",
"objetos, a las ",
"manos que las",
"tallaron y al ",
"corazon que las ",
"alimento. Y en el ",
"pedestal se leen ",
"estas palabras:",
"Mi nombre es ",
"Ozymandias, rey de",
"reyes: ¡Contemplad",
"mis obras, ",
"poderosos, y ",
"desesperad! Nada",
"queda a su lado. ",
"Alrededor de la ",
"decadencia de estas",
"colosales ruinas, ",
"infinitas y desnudas",
"se extienden, a lo ",
"lejos, las ",
"solitarias y llanas",
"arenas",
};

void setup()
{
  // initialize the LCD
  lcd.begin();
}

void loop()
{
  // Turn on the blacklight and print a message.
  // k es la 
  for(int i=0;i<37;i++){
    lcd.backlight();
    lcd.setCursor(0,0);
    lcd.print(string[i]); //Linea 1
    lcd.setCursor(0,1);
    lcd.print(string[i+1]); //Linea 2
    lcd.setCursor(0,2);
    lcd.print(string[i+2]); //Linea 3
    lcd.setCursor(0,3);
    lcd.print(string[i+3]); //Linea 4
    delay(3000);
    lcd.clear();
  }
}
```

# Interrupciones y timers

```c++
int cont = 0;

void setup() {
  attachInterrupt(2,reset_ISR,CHANGE);
  Serial.begin(9600);
}

void loop() {
  delay(1000);
  cont++;
  Serial.println(cont);
}

void reset_ISR(){
  delay(300);
  cont=0;
  Serial.println(cont);
}
```

