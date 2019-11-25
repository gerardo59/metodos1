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
