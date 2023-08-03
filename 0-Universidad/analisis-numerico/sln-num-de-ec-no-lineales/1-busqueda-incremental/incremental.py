import pandas as pd
import numpy as np
import math

print("X0:")
X0 = float(input())                     # ingresamos el punto de arranque
print("Delta:")
Delta = float(input())                  # ingresamos el delta
print("Niter:")
Niter = float(input())                  # ingresamos el Número max de iteraciones
print("Function:")
Fun = input()                           # metemos la función -> cadena

x=X0                                    # asignamos x como una variable -> para que la cadena lo interprete
f0=eval(Fun)                            # evaluamos la cadena

if f0==0:
  #s=x
  print(X0, "es raiz de f(x)")          # si la función es 0 de una damos la raiz
else:
  X1=X0+Delta                           # X1 será nuestro nuevo punto de arranque
  x=X1                                  # actualizamos el x para la evaluación
  c=1                                   # iniciamos el contador
  f1=eval(Fun)                          # evaluamos nuestra nueva función
  while f0*f1>0 and c<Niter:            # mientras que aseguremos que no hemos cambiado de cuadrante, melo -> ojo que se explota si la función nunca cambia de cuadrante(Niter)
    X0=X1
    f0=f1
    X1=X0+Delta
    x=X1                 
    f1=eval(Fun)                        # actualizamos los límites y evaluamos nuevamente
    c=c+1                               # aumentamos el contador
                                        # al terminar
  if f1==0:                             # Encontramos la raiz en sí
    #s=x
    print(X1,"es raiz de f(x)")
    print("Encontrado en ",c," iteraciones")
  elif f0*f1<0:                         # Encontramos un intervalo solución
    #s=x
    print("Existe una raiz de f(x) entre ",X0," y ",X1)
    print("Encontrado en ",c," iteraciones")
  else:                                 # No encontramos solución porque se acabo el Niter
    #s=x
    print("Fracaso en ",Niter, " iteraciones ") 
    