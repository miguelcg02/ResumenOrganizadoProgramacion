import pandas as pd
import numpy as np
import math

x = np.pi/4                                                 #Definimos el valor que usaremos de entrada

Tol = 0.5E-14                                               #Definimos la tolerancia por decimales correctos

n=0                                                         #n de la sumatoria
fm=[]                                                       #listado de las aproximaciones de la función
fx=((-1)**n)*(x**(2*n))/np.math.factorial(2*n)              #funcion del coseno
Error=[]                                                    #Listado de errores
Error.append(abs(fx-np.cos(x)))                             #Hallamos el primer error
fm.append(fx)                                               #la primera función de la serie 
while Error[n]>Tol:                                         #mientras que el error actual sea mayor a la tolerancia dispuesta...
     n+=1                                                   #subimos la n que vamos a trabajar
     fx+=((-1)**n)*(x**(2*n))/np.math.factorial(2*n)        #actualizamos la funcion
     fm.append(fx)                                          #añadimos la nueva aproximación
     error=abs(fm[n]-np.cos(x))                             #hallamos el error
     Error.append(error)                                    #añadimos el nuevo error
                                                            #salimos cuando el error actual sea menor o igual a la tolerancia 
Tabla=[Error,fm]
Tabla=np.transpose(Tabla)
pd.set_option('display.float_format', lambda x: '%.8f' % x) #cambiamos el # de decimales a mostar en el dataframe
df=pd.DataFrame(Tabla, columns=["Error", "cosx"])
print(df) 