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
