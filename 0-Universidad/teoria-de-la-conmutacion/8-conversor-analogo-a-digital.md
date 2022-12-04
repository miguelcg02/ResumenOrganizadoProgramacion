# Registro

Por la resolución va entre 0 y 1023, usando 10 bits

Formulita

Xv = (5.0v*Yadc)/1023

# Calibrar

Referencias:

Default: La referencia por defecto analódico de 5 voltios
Interior: Da un valor máximo de 1,1 voltios o 2,56voltios. Hay que tener cuidado de que no se pase. Se activa con INTERNAL1V1 
Externa: Define valores diferentes, el que uno quiera, dado por un elemento externo.

# Ejemplo 1 Mostrar en el LCD el valor numerico correspondiente a la señal análoga que entra por A0

```c++
int valor;
int lectura_ADC = 0;
float voltaje = 0.0;

void setup(){
    Serial.begin(9600);
}

void loop(){
    lectura_ADC = analogRead(0);
    voltaje = (5.0*lectura_ADC)/1023;
    temperatura = voltaje/0.01;
    delay(200);
    Serial.print("Conversor A/D: ");
    Serial.println(lectura_ADC); 
    Serial.print("Voltaje ");
    Serial.println(voltaje); 
    Serial.print("Temperatura ");
    Serial.println(temperatura); 
}
```