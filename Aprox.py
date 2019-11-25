from numpy import arange
import matplotlib.pyplot as plt

fx=raw_input("ingrese la ecuacion :} $") 
print fx

tol=raw_input("digite la tolerancia $$")
print tol

inter1=raw_input("intervalo a....?")
print inter1

inter2=raw_input("intervalo b....?")
print inter2

plt.plot(fx)
plt.grid(axis='both')
plt.show()






