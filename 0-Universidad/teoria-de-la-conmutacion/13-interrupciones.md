# Interrupción de botonoes / KBI'2

- Key board interrupt

* Se pueden leer varios estados de interrupción:

- Low (Cuando se encuentra en 0)
- Change (No importa si fue rising o falling)
- Rising (Por ej en un flanco de subida, cuando sube)
- Falling (Por ej en un flanco de bajada, cuando baja)

* Las interrupciones tienen un pin asociado

# Sintaxis

* Prender la interrupción

attachInterrupt(pinInterrupción,laFuncion,ElModo)

- pinInterrupción: el numero de la interrupción (int)
- función: pos la función que va a interrumpir
- El modo: si va a ser low,change,rising, falling

* Apaagar la interrupción

dettachInterrupt(pinInterrumpido)