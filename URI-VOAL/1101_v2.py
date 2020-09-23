#!/usr/bin/python3

m = ""
n = ""

iterator = 1

sequencia = []
somador = []
soma_dos_numeros = []

while iterator == 1:
	m, n = [int(index) for index in input().split(" ")]
	#print(type(m), type(n))
	somatorio = 0

	while m > n and (m > 0 and n > 0): #OK
		for i in range(n,m+1):
			somatorio += i
			#print(i, end=' ')
		#print("Sum={}".format(somatorio))
		sequencia.append([i for i in range(n,m+1)])
		#print(sequencia)
		somador.append(somatorio)
		#soma_dos_numeros.append("Sum={}")#.format(somatorio))
		break #OK

	while n > m and (n > 0 and m > 0):
		for i in range(m,n+1): #PROBLEMA
			somatorio += i
			#print(i, end=' ')
		#print("Sum={}".format(somatorio))
		#sequencia.append([i, end='' for i in range(n,m+1)])
		sequencia.append([i for i in range(m,n+1)]) #PROBLEMA
		#print(sequencia)
		somador.append(somatorio)
		#soma_dos_numeros.append("Sum={}")#.format(somatorio))
		break #OK

	#print("Sum={}".format(somatorio))
	#m = 0 #DEBUGGER

	while m == 0 or n == 0 or ( n < 0 or m < 0): #OK
		iterator = 0 #OK
		break #OK


'''
for i in soma_dos_numeros:
	print("SOU EU!!" + soma_dos_numeros[0].format(somador[0]))
'''
#print("SOU EU!!" + soma_dos_numeros[0].format(somador[0]))

#for i in range(len(soma_dos_numeros)):
#	print(+ soma_dos_numeros[i].format(somador[i]))

#for i in range(len(sequencia)):
#	print(sequencia[i], end=' ')

for i in range(len(sequencia)): 
	for index in range(len(sequencia[i])): 
		print(sequencia[i][index], end=" "); 
	print("Sum={}".format(somador[i]))
