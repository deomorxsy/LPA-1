#!/usr/bin/python3

'''
URI Online Judge | 1099
Sum of Consecutive Odd Numbers II

Read an integer N that is the number of test cases. Each test case is a line containing two
integer numbers X and Y. Print the sum of all odd values between them, not including X and Y.

Input: The first line of input is an integer N that is the number of test cases that follow.
Each test case is a line containing two integer X and Y.
Output: Print the sum of all odd numbers between X and Y.

'''

num_casos = int(input())
switch = 1 #Iterator: 1=True. 0 for False.
intervalo = []

accumulator = [] 
#IMUTÁVEL. guarda os itens atuais de intervalo e reseta na próxima iteração
somatorio = 0 #variável somatório
#IMUTÁVEL. recebe os ímpares


guardador = []

for i in range(num_casos):
	accumulator = [] #IMUTÁVEL
	somatorio = 0 #IMUTÁVEL

	while switch == 1:
		intervalo.append([int(x) for x in input().split(' ')])
		#print(intervalo)
		break

	for i in intervalo[len(intervalo)-1]: #retorna o ultimo index da lista e percorre a sublista:
		accumulator.append(i)

	while (accumulator[0] > accumulator[1]):
		for i in range(accumulator[1]+1,accumulator[0]): 
		#o -1 no accumulador[0] torna ESSA SITUAÇÃO DE START, maiorque STOP, excludente.
		#o -1 no STEP faz com que a lista seja percorrida ao contrário, daí ela executa
			while i % 2 != 0: #faz com que apenas numeros impares sejam retornados
				somatorio += i
				#guardador.append(somatorio)
				#print("[0]>[1]".format(i))
				break
		guardador.append(somatorio)
		break


	#somatorio=0
	
	while accumulator[0] < accumulator[1]:
		for i in range(accumulator[0]+1, accumulator[1]):
			while i % 2 != 0:
				somatorio += i
				#guardador.append(somatorio)
				#print("[1]>[0]".format(i))
				break
		guardador.append(somatorio)
		break
	

	while (accumulator[0] == accumulator[1]):# or (accumulator[0] < accumulator[1]):
		guardador.append(0)
		break
		#for i in range(accumulator[1],accumulator[0]): 
		#o -1 no accumulador[0] torna ESSA SITUAÇÃO DE START, maiorque STOP, excludente.
		#o -1 no STEP faz com que a lista seja percorrida ao contrário, daí ela executa
		'''
			while i % 2 == 0: #faz com que apenas numeros impares sejam retornados
			#somatorio += i
			#guardador.append(somatorio)
			#print("[0]>[1]".format(i))
			break
		'''
	#print("Somatorio={}".format(somatorio), end=' ')

	#print("{}".format(guardador))

for i in guardador:
	print(i)

'''
for i in range(num_casos):
	for x in range(len(accumulator)):
		for index in range(len(accumulator[x])):
			print(accumulator[x][index])

'''