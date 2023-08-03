import pandas as pd
import numpy as np
import math

print("X0:")
X0 = float(input())
print("Tol:")
Tol = float(input())
print("Niter:")
Niter = float(input())
print("Function:")
Fun = input()
print("derivate Function df:")
df = input()

fn=[]
xn=[]
E=[]
N=[]
x=X0
f=eval(Fun)
derivada=eval(df)
c=0
Error=100               
fn.append(f)
xn.append(x)
E.append(Error)
N.append(c)
while Error>Tol and f!=0 and derivada!=0  and c<Niter:
  x=x-f/derivada
  derivada=eval(df)
  f=eval(Fun)
  fn.append(f)
  xn.append(x)
  c=c+1
  Error=abs(xn[c]-xn[c-1])
  N.append(c)
  E.append(Error)
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