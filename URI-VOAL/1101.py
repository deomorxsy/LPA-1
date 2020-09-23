#!/usr/bin/python3
#date: 22/09/2020

pares = [] #input().split(' ')
somatorio = 0

#for i in range(len(pares)):
#	pares[i] = int(pares[i])

while (pares[0] > pares[1] and (pares[0] != 0 and pares[1] != 0)):
	
	#Passo 1: pega o input, transforma tudo em int.
	pares.append(input().split(' '))

	#for i in range(len(pares[])):
	#	pares[i][i] = int(pares[i])
		
		#[pares[i] = int(pares[i]) for i in input.split(' ')]

	#PAsso 2
	for i in range(pares[1],pares[0]+1):
		somatorio += i

	for i in range(pares[1],pares[0]+1):
		print(i, end=" ")

	print("Sum={}".format(somatorio))
	break

somatorio=0
while (pares[1] > pares[0] and (pares[0] != 0 and pares[1] != 0)):
	for i in range(pares[0],pares[1]+1):
		somatorio += i
	for i in range(pares[0],pares[1]+1):
		print(i, end=" ")

	print("Sum={}".format(somatorio))
	break

'''
Sequence of Numbers and Sum

Read an undetermined number of pairs values M and N (stop when any of these values is less or equal
to zero). For each pair, print the sequence from the smallest to the biggest (including both) and
the sum of consecutive integers between them (including both).

Input: The input file contains pairs of integer values M and N. The last line of the file contains
a number zero or negative, or both.
Output: For each pair of numbers, print the sequence from the smallest to the biggest and the sum
of these values, as shown below.

'''