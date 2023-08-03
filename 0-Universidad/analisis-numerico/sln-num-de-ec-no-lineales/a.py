xn = -1.85718386
xnm1= -1.85718389
xnm2= -1.85748754

a = abs(xn-xnm1)
b = abs((xnm1-xnm2)**1.62)

k = (a/b)
print(k)