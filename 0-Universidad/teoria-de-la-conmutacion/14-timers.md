# Timer

maximo = periodo(pre-escala)*(1/frecuencia)*(2^17)

tiempoDeConteo = (pre-escala)*(1/frecuencia)

Siempre que se va a trabajar con timers se debe agregar la librería de
este que ya viene con todos los parámetros definidos ahorrando
tiempo al programar ya que evita el proceso de estar haciendo los
cálculos manualmente con esta librería, lo único que hay que hacer es
definirle el tiempo de trabajo con el que se desea trabajar el timer
este tiempo se le debe dar en microsegundos (uS) y habilitar la
interrupción.

1. Inicializar el tiempo del Timer1. El tiempo esta en microsegundos.
    Timer1.initialize(1000000);

2. Habilitar la interrupción por timer1, e indicar que función se debe ejecutar cuando se genere la interrupción.
    Timer1.attachInterrupt(reloj);
    
3. Deshabilitar la interrupción por timer1, cuando no se requiera.
    Timer1.detachInterrupt();