import pandas as pd
import numpy as np
import math

print("X0:")
X0 = -3                           # ingresamos la condición inicial
print("Tol:")
Tol = 5e-5                        # ingresamos la tolerancia en cifras significativas
print("Niter:")
Niter = 100                          # ingresamos el máximo de iteraciones
print("Function:")
Fun = "((3/2)*x*math.log(x+100))+((x**2)*math.log(x+100))+((9/16)*math.log(x+100))"                                 # ingresamos la función a encontrar su solución f(x)=0
print("Function g:")                
g = "(((x**2)*math.log(x+100))+((9/16)*math.log(x+100)))/((-3/2)*math.log(x+100))"                                     # ingresamos la funcion g(x)=x

fn=[]                                           # arreglo de las aproximaciones hasta llegar cercano a 0
xn=[]                                           # arreglo de las aproximaciones de la solución
E=[]                                            # listado de los errores
x=X0
f=eval(Fun)
c=0
Error=100               
fn.append(f)
xn.append(x)
E.append(Error)
while Error>=Tol and f!=0 and c<Niter:
  x=eval(g)                                     # encontramos la próxima x con la g(x)
  f=eval(Fun)                                   # vemos el nuevo acercamiento al 0
  fn.append(f)                                  # agregamos el nuevo acercamiento
  xn.append(x)                                  # agregamos la nueva x
  c=c+1                                         # aumentamos el contador
  Error=abs((xn[c]-xn[c-1])/xn[c])              # encontramos el nuevo error
  E.append(Error)	                              # agregamos el nuevo error
if f==0:
  s=x
  print(s,"es raiz de f(x)")
elif Error<Tol:
  s=x
  print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
  Tabla=[xn,fn,E]
  Tabla=np.transpose(Tabla)
  pd.set_option('display.float_format', lambda y: '%.8f' % y) #cambiamos el # de decimales a mostar en el dataframe
  df=pd.DataFrame(Tabla, columns=["xn","f(xn)","Error"])
  print(df) 
else:
  s=x
  print("Fracaso en ",Niter, " iteraciones ")