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
     fx=gx
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
