import re

fx ='(x**3)+2*(3*x)+2'
t = fx.split("+")

d1 = r'^\([0-9]+\)' 		#k
d2 = r'^\(([0-9]+)\*(x)\)' 	#kx
d3 = r'^\((x)\*\*([0-9]+)\)' #x*n
d4 = r'^\(([0-9]+)\)\((x)\*\*([0-9]+)\)' #kx*n

df = ""

for termino in t:
	r = re.search(d1,termino)
	if r:
		pass

	r = re.search(d2,termino)
	if r:
		df += r.group(1)
	r = re.search(d3,termino)
	if r:
		n = int(r.group(2))
		df += "%sx**%s + "%(n,n-1)
	r =  re.search(d4,termino)
	if r:
		k = int(r.group(3))
		n = int(r.group(4))
		df += '%sx**%s + '%(n-1,k)
print df
