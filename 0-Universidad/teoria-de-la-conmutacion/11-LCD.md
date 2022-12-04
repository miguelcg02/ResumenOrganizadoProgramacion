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
LiquidCrystal lcd(RS, E, D4, D5, D6, D7);

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

  
  lcd.clear();
  lcd.setCursor(3,0); //Ubica el cursor en la columna 3 de la fila 0
  lcd.print(pot1); //Muestra el mensaje “UNIVERSIDAD"
  lcd.setCursor(3, 1); //Ubica el cursor en la fila 1 de la columna 1
  lcd.print(pot2); //Muestra el mensaje " EAFIT-MEDELLIN "
  delay(50);
}
```