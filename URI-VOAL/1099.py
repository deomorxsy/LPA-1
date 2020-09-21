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
index = 0

acumulador = []

somatorio = 0

for i in range(numero_testes):
	casos = [int(i) for i in input().split(' ')]
	while (casos[0] < casos[1]): 
		for i in range(casos[0],casos[1]):
			while (i % 2 != 0) and (i != casos[0]): #if
				somatorio += i
				#print("{}".format(casos[i]))#DEBUGGER
				break
			acumulador.append(somatorio)
		break
	
	somatorio=0

	while (casos[0] > casos[1]): 
		for i in range(casos[0],casos[1],-1): #start,stop,step
			while (i % 2 != 0) and (i != casos[0]): #if
				somatorio += i
				#print("{}".format(i)) # debugger
				break
			acumulador.append(somatorio)
			#print("{}".format(i))#DEBUGGER
		#print("casos[0] não é maior que caso[1].") #DEBUGGER
		break

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