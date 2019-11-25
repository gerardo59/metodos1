# -*- coding: utf-8 -*-
import os
import random

print "HOLA BIEN VENIDO A LA RECOPILACION DE PYTHON"

def matriz():

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


def matriz1():
	print "multiplicacion de matrices con python 2 parcial"

	fila1=int(raw_input("por favor introduce el numero de filas que debera tene la matriz uno}:"))
	#digite numero de filas de la matriz1:

	columna1=int(raw_input("por favor introduce el numero de columnas que debera tene la matriz uno}:"))
	#digite el numero de columnas de la matriz1

	columna2=int(raw_input("por favor introduce el numero de columnas que debera tene la matriz dos}:"))
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
		   a[i][j]=int(input("digite sus valores (%d,%d): " % (i,j)))

	for i in range(fila1):
	    print(a[i])

	print "ahora introduciremos valores de la matriz b o segunda matriz"

	#digite valores de la matriz b

	for i in range(columna1):
	    for j in range(columna2):
	           b[i][j]=int(input("digite sus valores (%d,%d): " % (i,j)))

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


	    R=[]
	    for j in range(columna2):
	      R.append(C[i][j])
	    print(R)

def biseccion():
	print "bien venido al programa de graficacion"

	from numpy import arange
	import matplotlib.pyplot as plt

	fx="(x**3)-(7*(x**2))+(14*x)-6"
	rango=arange(0.5,1,0.001)
	valores=[]

	for x in rango:
	    y = eval(fx)
	    valores.append(y)

	plt.plot(rango,valores)
	plt.grid(axis='both')
	plt.show()

def BISECCION():
	from numpy import arange
	import matplotlib.pyplot as plt


	ITERACION  = int(input("NUMERO DE ITERACIONES: "))
	fx=raw_input("Ingresa ecuacion: ")
	#fx="(x**3)-(7*(x**2))+ (14*x)-6"
	INTERVALO_A = -1.0
	INTERVALO_B = 1.0
	fm = 0.0

	while 1:
	 x= INTERVALO_A
	 fa = eval(fx)
	 x = INTERVALO_B
	 fb = eval(fx)
	 if (fa < 0 and fb >0)or(fa>0 and fb<0):

	     break
	 else:
	     INTERVALO_A -= 1
	     INTERVALO_B += 1

	INTERVALOINICIAL_A = INTERVALO_A
	INTERVALOINICIAL_B = INTERVALO_B

	print("el intervalo A es:  ",INTERVALO_A)
	print("el intervalo B es:  ",INTERVALO_B)
	raw_input()

	for i in range(0,ITERACION):
	 x = INTERVALO_A
	 fa = eval(fx)

	 x = INTERVALO_B
	 fb = eval(fx)

	 m = (INTERVALO_A +  INTERVALO_B ) /2.0
	 fm = eval(fx)
	 print("iteracion %s: " % (i+1))
	 print("a  " , INTERVALO_A)
	 print("fa  ",fa)
	 print("b  ",INTERVALO_B)
	 print("fb  ",fb)
	 print("m  ", m)
	 print("fm  ",fm)






	 if  fm < 0.0:
	   if fa > 0.0:
	         INTERVALO_B = m
	   else:
	     INTERVALO_A = m
	 else:
	   if fa < 0 :
	    INTERVALO_B = m
	   else:
	    INTERVALO_A = m
 





	rango = arange(INTERVALOINICIAL_A,INTERVALOINICIAL_B,0.0001)
	valores = []

	for x in rango:
	    y = eval(fx)
	    valores.append(y)

	plt.plot(rango,valores)
	plt.grid(axis='both')
	plt.show()

def aprox():
	from numpy import arange
	import matplotlib.pyplot as plt
	import math

	#fx="(((5*x)**2)-(math.e**x))"

	INTERVALO_A = float(raw_input("Ingresa el intervalo A: "))
	INTERVALO_B = float(raw_input("Ingresa el intervalo B: "))
	TOLERANCIA= float(raw_input("ingresa la tolerancia"))
	fx=raw_input("Ingresa ecuacion: ")
	rango = arange (INTERVALO_A,INTERVALO_B)


	valores = []

	INTERVALOINICIAL_A = INTERVALO_A
	INTERVALOINICIAL_B = INTERVALO_B
	x0= (INTERVALO_A + INTERVALO_B )/ 2.0

	print("el intervalo a es: ",INTERVALO_A)
	print("el intervalo b es: ",INTERVALO_B)
	print("X0 ES :",x0)
	raw_input()

	error = TOLERANCIA+1 
	x= x0
	i = 1


	while error > TOLERANCIA:
	     gx=eval(fx)
   
	     error = abs(gx-x)
	     x=gx
	     print("************LA ITERACION %s************: " % (i))
	     print("EL RESULTADO ES:",x)
	     print("EL ERROR ES :",error)
	     i=i+1



	rango = arange(-10, 10,TOLERANCIA)
	valores = []

	for x in rango:
	    y = eval(fx)
	    valores.append(y)

	plt.plot(rango,valores)
	plt.grid(axis='both')
	plt.show()

def menu():
	os.system("clear")
	print ("Selecciona una opción")
	print ("\t1 -BISECCION primera opción")
	print ("\t2 -biseccion segunda opción")
	print ("\t3 -matriz tercera opción")
	print ("\t4 -matriz1 cuarta opción")
        print ("\t5 -APROX quinta opción")
	print ("\t6 - salir")

while True:
	menu()

	opcionMenu = (int(raw_input("inserta un numero valor >> ")))

       	if opcionMenu == 1:
		print ("")
		raw_input("Has pulsado la opción 1...\npulsa una tecla para continuar")
		BISECCION()
        if opcionMenu == 2:
		print ("")
		raw_input("Has pulsado la opción 2...\npulsa una tecla para continuar")
		biseccion()
	if opcionMenu == 3:
		print ("")
		raw_input("Has pulsado la opción 3...\npulsa una tecla para continuar")
		matriz()
	if opcionMenu == 4:
                print ("")
                raw_input("Has pulsado la opción 3...\npulsa una tecla para continuar")
		matriz1()
	if opcionMenu == 5:
                print ("")
                raw_input("Has pulsado la opción 3...\npulsa una tecla para continuar")
		aprox()

	if opcionMenu == 6:
		break
	



