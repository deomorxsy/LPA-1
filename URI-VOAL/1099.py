#!/usr/bin/python3

'''
Sum of Consecutive Odd Numbers II

Read an integer N that is the number of test cases. Each test case is a line containing two
 integer numbers X and Y. Print the sum of all odd values between them, not including X and Y.
Input: The first line of input is an integer N that is the number of test cases that follow.
 Each test case is a line containing two integer X and Y.
Output: Print the sum of all odd numbers between X and Y.
'''

numero_testes = int(input()); #para o for loop
casos = []
acumulador = []

somatorio = 0

for i in range(numero_testes):
	casos = [int(i) for i in input().split(' ')]
	somatorio=0
	
	while ((casos[0] == casos[1]) 
		or (casos[0] + 1 == casos[1]) 
		or (casos[1] + 1 == casos[0]) 
		or (casos[0] == casos[1] + 2 and (casos[1]-1) % 2 == 0) 
		or (casos[1] == casos[0] + 2 and (casos[0]-1) % 2 == 0)):

		somatorio = 0
		print("N1 Loop")
		print("somatorio={}".format(somatorio))
		print("somatorio depois da soma={}\n".format(somatorio))
		acumulador.append(somatorio)
		break
	'''
	somatorio = 0
	while (casos[0] + 1 == casos[1]) or (casos[1] + 1 == casos[0]):
		somatorio = 0
		print("N2 Loop")
		print("somatorio={}".format(somatorio))
		print("somatorio depois da soma={}\n".format(somatorio))
		acumulador.append(somatorio)
		break
	'''
	somatorio = 0
	while (casos[0] < casos[1]): 
		for i in range(casos[0],casos[1]):
			while (i % 2 != 0) and (i != casos[0]): #if
				print("N2 Loop")
				print("somatorio={}".format(somatorio))
				somatorio += i;
				print("somatorio depois da soma={}\n".format(somatorio));
				#print("{}".format(casos[i]))#DEBUGGER
				break
			acumulador.append(somatorio)
		break
	
	somatorio=0
	while (casos[0] > casos[1]): 
		for i in range(casos[0],casos[1],-1): #start,stop,step
			while (i % 2 != 0) and (i != casos[0]): #if
				print("N3 Loop")
				print("somatorio={}".format(somatorio))
				somatorio += i
				print("somatorio depois da soma={}\n".format(somatorio))
				break
			#print("{}".format(i))#DEBUGGER
			acumulador.append(somatorio)
		#print("casos[0] não é maior que caso[1].") #DEBUGGER
		break

	


print("=====================")
for i in range(len(acumulador)):
	print("{}".format(acumulador[i]))

'''
	if (casos[0] < casos[1]):
		for i in range(len(casos)):
			print("{}".format(casos[i]))
	else:
		print("casos[0] não é maior que caso[1].")

#for item in range(casos[i][0],casos[i][1],-1):
'''
'''
index=0
while (index <= numero_testes):
	casos = input().split('')
	index+=1

'''