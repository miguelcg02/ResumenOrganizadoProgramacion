import pandas as pd
import numpy as np
import math

x = np.pi/6                                                 #Definimos el valor que usaremos de entrada

Tol = 5E-8                                               #Definimos la tolerancia por cifras significativas

n=0                                                         #n de la sumatoria
fm=[]                                                       #listado de las aproximaciones de la función
fx=((-1)**n)*(x**((2*n)+1))/np.math.factorial((2*n)+1)      #funcion del seno
Eps=[]                                                      #Listado de errores
Eps.append(100)                                             #el primer error es de 100
fm.append(fx)                                               #la primera función de la serie 
while Eps[n]>=Tol:                                          #mientras que el error actual sea mayor o igual a la tolerancia dispuesta...
     n+=1                                                   #subimos la n que vamos a trabajar
     fx+=((-1)**n)*(x**((2*n)+1))/np.math.factorial((2*n)+1)#actualizamos la funcion
     fm.append(fx)                                          #añadimos la nueva aproximación
     errorRel=abs((fm[n]-fm[n-1])/fm[n])                    #hallamos el error
     Eps.append(errorRel)                                   #añadimos el nuevo error
                                                            #salimos cuando el error actual sea estrictamente menor a la tolerancia 
Tabla=[Eps,fm]
Tabla=np.transpose(Tabla)
pd.set_option('display.float_format', lambda x: '%.8f' % x) #cambiamos el # de decimales a mostar en el dataframe
df=pd.DataFrame(Tabla, columns=["ErrorRel", "sinx"])
print(df)  