# DECIMALES CORRECTOS - ERROR ABSOLUTO

import pandas as pd
import numpy as np
import math

print("Xi:")
Xi = float(input())                     # ingresamos límite inferior(LI)
print("Xs:")
Xs = float(input())                     # ingresamos límite superior(LS)
print("Tol:")
Tol = float(input())                    # ingresamos tolerancia (decimales correctos)
print("Niter:")
Niter = float(input())                  # ingresamos número máximo de iteraciones
print("Function:")
Fun = input()                           # ingresamos la función a evaluar

LI=[]                                   # listado de LI
Fi=[]                                   # listado de fi
LS=[]                                   # listado de Ls
Fs=[]                                   # listado de fs
M=[]                                    # listado de Xm
fm=[]                                   # listado de los fm
E=[]                                    # listado de errores
x=Xi                                    
fi=eval(Fun)                            # Evaluamos el f del LI
x=Xs
fs=eval(Fun)                            # Evaluamos el f del LS

if fi==0:                               # Verificamos si LI es raiz
  s=Xi
  E=0                                     #No tendría error(cambie de lista a num)
  print(Xi, "es raiz de f(x)")
elif fs==0:                             # Verificamos si Ls es raiz
  s=Xs
  E=0                                     #No tendría error(cambie de lista a num)
  print(Xs, "es raiz de f(x)")
elif fs*fi<0:                           # Verificamos que podamos asegurar al menos una raiz en el intervalo
  c=0                                   # Iniciamos el contador
  p=(fs-fi)/(Xs-Xi)                     # Hallamos la pendiente de la recta
  Xm=(p*Xi-fi)/p                        # Encontramos el Xmedio
  x=Xm                 
  fe=eval(Fun)                          # Evaluamos el f de Xm
  LI.append(Xi)                         # Agregamos el valor actual de Xi
  Fi.append(fi)                         # Agregamos el valor de la funcion actual Xi
  LS.append(Xs)                         # Agregamos el valor actual de Xs
  Fs.append(fs)                         # Agregamos el valor de la funcion actual Xs
  M.append(Xm)                          # Agregamos el valor actual de Xm
  fm.append(fe)                         # Agregamos el valor de la funcion actual Xm
  E.append(100)                         # Agregamos el primer error como 100
  while E[c]>Tol and fe!=0 and c<Niter: # mientras no lleguemos a la tolerancia o a 0 ni sobrepasemos las iteraciones
                                        # verificamos qué intervalo sigue cumpliendo
    if fi*fe<0:                         # el inferior
      Xs=Xm                                # Xm se vuelve LS
      x=Xs                 
      fs=eval(Fun)                         # reevaluamos fs -> no es fe?
    else:                               # el superior
      Xi=Xm                                # Xm se vuelve LI
      x=Xi
      fi=eval(Fun)                         # reevaluamos fi -> no es fe?
    Xa=Xm                                  # Guardamos Xm como Xanterior --> posible opti [n-1]
    p=(fs-fi)/(Xs-Xi)                      # Hallamos la pendiente de la recta
    Xm=(p*Xi-fi)/p                         # Encontramos el Xmedio
    x=Xm 
    fe=eval(Fun)                           # evaluamos la f de Xm
    Error=abs(Xm-Xa)                       # revisamos el error entre la Xanterior y la nueva Xm -> cuando la diferencia entre estas sea menor o igual a la tolerancia coronamos
    LI.append(Xi)                          # Agregamos el valor actual de Xi
    Fi.append(fi)                          # Agregamos el valor de la funcion actual Xi
    LS.append(Xs)                          # Agregamos el valor actual de Xs
    Fs.append(fs)                          # Agregamos el valor de la funcion actual Xs
    M.append(Xm)                           # Agregamos el valor actual de Xm
    fm.append(fe)                          # Agregamos el valor de la funcion actual Xm
    E.append(Error)                        # guardamos el error en el listado
    c=c+1                                  # aumentamos el contador
                                           # al terminar:
  if fe==0:                                # Encontramos la raíz si fe es 0
    s=x
    print(s,"es raiz de f(x)")
  elif Error<=Tol:                          # Encontramos una aproximación si el último error calculado entre los LI y LS es menor a la tolerancia
    s=x
    print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
    Tabla=[LI,Fi,LS,Fs,M,fm,E]
    Tabla=np.transpose(Tabla)
    pd.set_option('display.float_format', lambda y: '%.8f' % y) #cambiamos el # de decimales a mostar en el dataframe
    df=pd.DataFrame(Tabla, columns=["Xi","f(Xi)","Xs","f(Xs)","Xm","f(Xm)","Error"])
    print(df) 
  else:
    #s=x
    print("Fracaso en ",Niter, " iteraciones ")
else:                                         # En caso de no poder asegurarla no ejecutamos nada
  print("El intervalo es inadecuado")