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
