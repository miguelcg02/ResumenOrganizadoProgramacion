# Etapas

1. Problema
2. Modelo
3. formulación matematica
4. Solución 

En solución se basa este curso, hay tres formas de resolver:
- Analitica, Ej resolver por algebra
- Numerica
- Grafica

# Metodos numéricos

Formas de las cuales se pueden solucionar problemas.

# Fuentes de error

- Metodo empleado.
- Datos.
- Maquina usada.

# Error absoluto E

```
E = X - X"
```

E, es la diferencia que existe entre el valor verdadero y el valor aproximada
X, Valor verdadero
X", Medida aproximada

X" < X, se subaproxima
X" > X, se sobreaproxima

La x normalmente es desconocida, pero X" y E suelen conocerse.

El error abosoluto establece un intervalo que acota el valor de x: x e [x-E, X"+E]


Ejemplo: Calcule el error absoluto de aproximar pi con 3 cifras decimales.

```
X = pi
X" = 3,142

E = |x-x"|
E = |pi-3,142|
E = 0,000407
E = 0.41 * 10^-3
```

# Error relativo

p = E/X
p" = E/X"

Ejmplo: calcular p" para la medida de altura en H = 1,70m +- 1cm

```
p" = 0,01/1,70
p" = 0,00588
p" = 0,588%
```

# Tarea

Calcular los errores relativos siguientes:

a) Aproximar 1/3 con 5 cifras
b) Aproximar euler con 6 cifras

# notacion numerica

La de toda la vida, con su respectiva base

# Notación de punto flotante

El primer decimal (osea desps de la coma) no puede ser 0 y debe esta escrito de la forma

+- 0.d1d2d3...dk * 10^+-n

Ej: 0.1111*2^-1
Ej malo: 0.0124*10

# Redondeo

* Por corte o defecto

Se mocha de ahí pa arriba

Ej: corte a 3 cifras
```
1,43543
1,435
```

* Rondeo por exceso

Se tira para arriba siempre

Ej: exceso a 3 cifras de base binaria
```
1,011
1,110
```

* Redondeo simetrico basado en la estadistica

si dx < 5: pa abajo
si dx >= 5 pa arriba

Ej: simetrico 3 cifras
```
1,6666
1,667
```

* Redondeo simetrico basado en la distancia

Es igual que el estadistico, pero
si dk+1 = 5
- si dk+2 = impar dk = dk+1
- si dk+2 = par dk = dk
