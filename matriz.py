import random


print "multiplicacion de matrices con python 2 parcial"

fila1=int(input("por favor introduce el numero de filas que debera tene la matriz uno}:"))
#digite numero de filas de la matriz1:

columna1=int(input("por favor introduce el numero de columnas que debera tene la matriz uno}:"))
#digite el numero de columnas de la matriz1

columna2=int(input("por favor introduce el numero de columnas que debera tene la matriz dos}:"))
#digite el numero de columnas que debera tener la matriz2

#primera matriz 
a=[]
for i in range(fila1):
	a.append([0]*columna1)

for i in range(fila1):
	print(a[i])

#segunda matriz
b=[]
for i in range(columna1):
        b.append([0]*columna2)

for i in range(columna1):
        print(b[i])

#introducir los valores de la matriz a
for i in range(fila1):
    for j in range(columna1):
	   a[i][j]= random.randint(0,100)

for i in range(fila1):
    print(a[i])

print "ahora introduciremos valores de la matriz b o segunda matriz"

#digite valores de la matriz b

for i in range(columna1):
    for j in range(columna2):
           b[i][j]=random.randint(0,100)

for i in range(columna1):
    print(b[i])

#insercion de los datos de la matriz a + b
C=[]
for i in range(fila1):
    C.append([0]*columna2)

for i in range(fila1):
    print(C[i])

#operacion de la matriz por multiplicacion

for i in range(fila1):
    for j in range(columna2):
        #for k in range(columna1):
		C[i][j] += a[i][j] * b[j][i]


for i in range(fila1):
    R=[]
    for j in range(columna2):
      R.append(C[i][j])
    print(R)







