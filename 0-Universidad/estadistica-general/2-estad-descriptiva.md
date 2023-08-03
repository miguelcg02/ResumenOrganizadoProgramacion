# Definiciones estadistica descriptiva

- Frecuencia absoluta: de un dato es el número de veces que aparece el dato en una bdd
- Frecuencia relativa: Conciente entre la frecuencia absoluta del dato y el número total de datos. Representa la participación de cada categoria dentro del total.
- Porcentaje: Frecuencia relativa * 100
- Hay varias maneras de graficar

# Trablas de frecuencia

- Datos ordenados de menor a mayor

- Rango: Xmax - Xmin
Xmax: mayor valor observado
Xmin: Menor valor observado

- Establcer número de clases: 
1. La regla de Sturges:
l = 1 + 3.322log(n)
l = 1+ 1.443ln(n)

l: núm de clases o intervalos
n = núm de observaciones

2. Regla de la raíz
i = sqr(n)

- Establecer longitud de las clases

La amplitud de cada intervalo estar ́a dada por la diferencia entre el valor m ́aximo y el valor m ́ınimo dividido por el n ́umero de intervalos obtenido anteriormente. Se recomienda establecer una longitud igual para todos los intervalos. Tomar amplitudes que faciliten los calculos como enteros, multiplos de 0.5, etc.

a = (Xmax-Xmin)/l
a = Rango/l

a: amplitud de los intervalor
l: núm de clases o intervalos

- Establecer límites de los intervalos. Se trata de buscar el límite inferior del primer intervalo.

Comenzar el primer intervalo con Xmin

Repartir la diferencia entre el recorrido de los intervalos y el rango de los datos al principio y al final de los datos. 

Linferior = Xmin - (a * l - Rango)/2

a: amplitud tomada para los intervalos
l: núm de intervalos tomados

La marca de clase de denota como x'i y se calcula asi:

x'i = (Lii + Lsi)/2

x'i es la marca de clase
Lii: límite inferior del intervalo i
Lsi: límite superior del intervalo i

# Pasos para resolver un ejercicio

Datos:
n: 50 datos
Xmax: 513
Xmin: 11

1. Ordenar los datos.

2. Sacar el Rango

Rango = Xmax - Xmin
Rango = 513 - 11
Rango = 502

3. Sacar el núm de intervalos o clases

regla de sturges (general)

l = 1 + log2(n)
l = 1 + log2(50)
l = 6.64 
I ~ 7

4. Determinar la amplitud de los intervalos

a >= Rango/l
a >= 502/7
a >= 71.714...
a ~ 72

5. Determinar donde empezar el primer intervalo

Opcion:
a. Desde el valor min obervado Xmin = 11

Empieza desde 11 y va sumando 72

11 a 83
83 a 155
155 a 227
ETC...
443 a 515


b. Empezar con un núm anterior al min observado que sea representativo

c. Repartir la diferencia

Linf = Xmin  (a*I - Rango)/2
Linf = 11 - (72*7 - 502)/2
Linf = 11 - (504 - 502)/2
Linf = 10

Empieza desde 10 y va sumando 72

...

6. Definir marcas de clase

Punto medio de 11 a 83 -> 47
Punto medio de 83 a 155 -> 119
Punto medio de 155 a 227 -> 191
Punto medio de ETC...
Punto medio de 443 a 515 -> 479

6. Hacer la tabla
