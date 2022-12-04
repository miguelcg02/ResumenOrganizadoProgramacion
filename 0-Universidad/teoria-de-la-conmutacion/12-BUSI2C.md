# BUS I2C

El bus I²C, un estándar que facilita la comunicación entre microcontroladores, memorias y otros dispositivos con cierto nivel de “inteligencia”, sólo requiere de dos líneas de señal y un común o masa.

Fue diseñado por Philips y permite el intercambio de información entre muchos dispositivos a una velocidad aceptable, de unos 100 Kbits por segundo.

La metodología de comunicación de datos del bus I²C es en serie y sincrónica Requiere 2 cables: uno para la señal de reloj (CLK) y el otro para el envío de información (SDA).

• SCL (serial clock line) es la línea de pulsos de reloj que sincronizan el
sistema.
• SDA (serial data line) es la línea por la que se mueven los datos entre los
dispositivos.
• GND (tierra) común de la interconexión entre los dispositivos conectados al bus

Tiene una arquitectura tipo maestro-esclavo. El dispositivo maestro inicia la comunicación con los esclavos, y puede enviar y recibir datos de los esclavos Los esclavos NO pueden iniciar la comunicación, ni hablar entre si directamente.

# Codigo ejercicio 1

```c++
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 20, 4); //0x27 es la dirección del display lcd, el 16 es el numero de columnas y 2 es el número de filas

void setup()
{
	// initialize the LCD
	lcd.begin();

	// Turn on the blacklight and print a message.
	lcd.backlight();
	lcd.print("Hello, world!");
}

void loop()
{
	// Do nothing here...
}
```

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