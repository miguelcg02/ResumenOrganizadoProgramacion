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
