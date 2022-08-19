# Transistores

1. Que es?

- Son pequeños componentes electrónicos con dos funciones principales. i) Encender y apagar circuitos ii) Ser amplificadores de señal
- Numero de parte, es el numero de transistor que se utiliza para revisar la ficha técnica del fabricante.
- Se tienen tres terminales. E B C
- E: Emisor
- B: Base
- C: Colector

- Poniendo la parte plana de frente, la parte izq es el emisor, el centro la base y la de la derecha el colcetor

2. Para que se usa?

- El transistor puede servir para automatizar procesos de paso o no de correitne
- En la base se necesita aplicar al menos 0.6-0.7 voltios para que el transistor encienda.
- Se puede controlar para que se mande mayor voltaje o corriente
- Un pequeño cambio en la entrada de voltaje en la base provoca una gran carga en la salida.
- Generalmente el circuito corresppondiente a la base tiene una corriente muy pequeña, pero la corriente en el colectro es mucho más grande

Beta = corriente de colector/corriente de la base

- En el transistor NPN: La corriente se acumula en este.
- En el transistor PNP: La corriente se divide en este.

- Mirar dibujos de cada uno.
- La flecha corresponde a la dirección de la corriente

3. Cómo funciona?

- El flujo de electrone es de negativo a positivo. Pero se diseñan los circuitos usando la corriente convencional.

# Compuertas logicas


Logia positiva: 0 no se hace nada
Logica negativa: 1 que se hace algo

El numero de estados 2^(numero de entradas)

And = Multiplicación
y = AxB
=D- Es AND

Or = Aditiva
y = A + B
=})- Es Or

compuertas, circuitas combinatoria

1. BUFFER (y=A)  
2. NOT (y=-A)
3. AND (y=AxB)
4. OR (y=A+B)
5. NAND (y=-(AxB))
6. NOR (y=AoB)
7. XOR (y=-(AoB))


# Latch SR

- Puede ser consideraod como una memoria de 1 byte
- Dispositivo de almacenamiento de 1-bit
- Son similarea a los Flip-Flops

- Tienen 2 entradas: S y R
- Tienen 2 salidas: Q y -Q

- Dispositivo l+ogico biestable o múltivibrador
- Hay Latch S-R con entradas activas a nivel Bajo (Compuertas NAND)
- Y con entradas activas a nivel alto (De compuestas NOR)

- SET: Establecer salidas a Q=1
- RESET: Restablecer salidas a Q=0

# Flip-flop SR

1. Sin reloj

- El flip-flop es una bascula donde va a sensar 2 valores.
- Reset 0
- Set 1

