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
