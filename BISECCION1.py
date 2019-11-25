from numpy import arange
import matplotlib.pyplot as plt


ITERACION  = int(input("NUMERO DE ITERACIONES: "))
fx=raw_input("Ingresa ecuacion: ")
fx="(x**3)-(7*(x**2))+ (14*x)-6"
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
