int valor;
float voltaje= 0.0;
float temp= 0.0;

void setup() {
  Serial.begin(9600);

}

void loop() {
  valor=analogRead(0);
  delay(200);
  Serial.println("------------------------------------");
  Serial.print("Conversor a/d: ");
  Serial.println(valor);
  voltaje= (valor*5.0)/1023;
  Serial.print("equivale a: ");
  Serial.println(voltaje);
  temp= (voltaje)/0.01;
  Serial.print("equivale a: ");
  Serial.println(temp);
}
