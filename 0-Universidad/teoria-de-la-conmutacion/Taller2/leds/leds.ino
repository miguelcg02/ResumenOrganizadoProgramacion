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
