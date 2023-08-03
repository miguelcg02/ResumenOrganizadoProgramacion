#Asinar
x = 256

#imprimir
print(x)
print("Hola mundo")
print("Wenaaas")

#asignación multiple
y = 559; y
a = 2; b = 3; c =-1

#sequencias from,to,by
seq(20,35)

#asignación con seq y uno a uno (arreglos int)
secuencia_1 = seq(122,137) 
print(secuencia_1)

secuencia_2 = 122:137
print(secuencia_2)

secuencia_3 = seq(122,137,3)
print(secuencia_3)

# Matriz

vector_1 = matrix(122:137)
print(vector_1)

# Matriz cuadrada por fila

matriz_1 = matrix(122:137,nrow = 4, ncol=4)
# o matriz_1 = matrix(122:137,4)
print(matriz_1)

# Matriz cuadrada por columna

matriz_2 = matrix(122:137,nrow = 4, ncol=4, byrow=TRUE)
print(matriz_2)

# Generar matriz z**3

z = 1:10
matriz_z = matrix(z**3)
print(matriz_z)

# Graficar puntos

plot(z, main="Grafico de Z", xlab="Indice", ylab="Z")
plot(matriz_z, type="l", main="Grafico de Z**3", xlab="Indice", ylab="Z")

# Editar un valor de la matriz

matriz_1
matriz_1[3,2] = 135
matriz_1

plot(matriz_1[,2])
