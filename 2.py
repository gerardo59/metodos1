print "Practicas METODOS NUMERICOS \n\n" 
print "URIEL MATEO CARMONA\n\n"
print "ISC-151\n\n\n  Seleccione programa"


def matriz():
	print('Ingresa el orden de su Matriz 1')
	filas1,columnas1 = int(input()),int(input())
	print('Ingresa el orden de su Matriz 2')
	filas2,columnas2 = int(input()),int(input())

	if (columnas1==filas2):
	
		matriz1 = []
		for i in range(filas1):
			matriz1.append( [0] * columnas1 )
	
		matriz2 = []
		for i in range(filas2):
			matriz2.append( [0] * columnas2 )
	
		print 'Ingrese su Matriz 1'
		for i in range(filas1):
			for j in range(columnas1):
				matriz1[i][j] = float(raw_input('Elemento (%d,%d): ' % (i, j)))
		print 'Ingrese su Matriz 2'
		for i in range(filas2):
			for j in range(columnas2):
				matriz2[i][j] = float(raw_input('Elemento (%d,%d): ' % (i, j)))
	
		matriz3 = []
		for i in range(filas1):
			matriz3.append( [0] * columnas2 )
	
		for i in range(filas1):
			for j in range(columnas2):
				for k in range(filas2):
					matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
		print ('Su matriz resultante es')
		print matriz3
	else:
		print ('Recurda la multiplicacion entre matrices debe ser mxn * nxp')
	return 0
	
def grafica():
	from numpy import arange 
	import matplotlib.pyplot as plt 
	import math


	fx="(((5*x)**2)-(math.e**x))"
	rango = arange(-10,10)
	valores = []
	
	for x in rango:
	    y = eval(fx)
	    valores.append(y)
	    print "x = %s y = %s" %(x, y)

	plt.plot(rango,valores)
	plt.grid(axis='both')
	plt.show()
	return 0

def biseccion():
	import math
	# Funcion que evalua f(x) con el metodo de Horner
	def f(coeficientes, grado, valor):
	    resultado = coeficientes[0]
	    i = 1
	
	    while(i <= grado):
	        resultado = (resultado * valor) + coeficientes[i]
	        i += 1
	
	    return resultado
	# FUNCION QUE CALCULA Mx
	def Mx(a, b):
	    return (a + b) / 2
	
	# METODO DE BISECCION
	
	def biseccion(coeficientes, grado, iInicial, iFinal):
	    a = iInicial
	    b = iFinal
	    nIteraciones = math.ceil((math.log(b - a) - math.log(0.00001)) / math.log(2))
	
	    print "{0}\t{1}\t{2}\t{3}\t{4}".format('n', 'a', 'b', 'Mx', 'f(Mx)f(a)')
	
	    i = 1
	    while(i <= nIteraciones):
	        x = Mx(a, b)
	        Fx = f(coeficientes, grado, x)
	        Fa = f(coeficientes, grado, a)


	        condicion = Fx * Fa
	
	        print i, "\t{:.4}\t{:.4}\t{:.4}\t{:.4}".format(a, b, x, condicion)
	
	
	        if(condicion > 0):
	            a = x
	        elif(condicion < 0):
	            b = x
	        else:
	            x = x
	
	
	        i += 1
		print "\nLa raiz encontrada es: {0}\n".format(x)
	
	
	#Programa principal
	
	consulta = '1'
	while(consulta != '0'):
	
	    print "Metodo de biseccion\n"
	
	
	    grado = int(raw_input("Grado de ecuacion: "))   
	    print                                                  
	    iInicial = float(raw_input("Intervalo inicial: "))      
	    iFinal = float(raw_input("Intervalo final: "))         
	
	
	
	    coeficientes = []       
	
	
	    i = grado
	    while(i >= 0):                                              
	        cof = float(raw_input("Ingresa x^{0}: ".format(i)))     
	        coeficientes.append(cof)                                
	        i -= 1                                                   
	
	
	    biseccion(coeficientes, grado, iInicial, iFinal)
	
	
	    print
	    consulta = raw_input("Para salir presiona 0, sino otra tecla: ")			
				
				
def aproximacion():
		from numpy import arange
		import matplotlib.pyplot as plt
		import math
		
		#fx="(((5*x)**2)-(math.e**x))"
		INTERVALO_A = float(input("Ingresa el intervalo A: "))
		INTERVALO_B = float(input("Ingresa el intervalo B: "))
		TOLERANCIA= float(input("ingresa la tolerancia"))
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
		#math.sqrt(math.e**(x)/5)
		#  (x***3)-10(x)-5     -1 ,0
		#  x**3-6(x**2)+11(x)-6.1    35,36
		while error > TOLERANCIA:
		     gx = eval(fx)
		   
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
		return 0		
	
	
while True :
	opcion = int(raw_input("1) Multiplicacion de matrices \n2)Graficacion\n3)programa biseccion \n4)programa de aproximacion\n5)SALIR..."))

	if opcion == 1:
		matriz()
	if opcion == 2:
		grafica()
	if opcion == 3:
		biseccion()
	if opcion == 4:
		aproximacion()
	if opcion == 5:
		break

