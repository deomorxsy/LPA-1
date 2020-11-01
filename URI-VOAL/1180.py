#!/usr/bin/python3
#date: 31/10/2020
#1 2 3 4 -5 6 7 8 9 10

number = int(input())
holder = input().split()
vetor = []

lowest = 0
indice = 0

#certifies that the length will be equal to number
for i in range(number):
	vetor = vetor + [holder[i]]
#converts each item inside vetor to integer
for i in range(number):
	vetor[i] = int(vetor[i])

#sets a comparison parameter
lowest = vetor[0]

#if the first element already is the "lowest",
#then we just need to test the others.
#if any item is less than lowest, then 
#this number is assigned to lowest.
#and if lowest isn't bigger than any item,
#then indeed, lowest is really the lowest.
for i in range(1,len(vetor)):
	if vetor[i] < lowest:
		lowest = vetor[i]
		indice = i
		#print("ué")


#print("==========")
print("Menor valor: {}\nPosicao: {}".format(lowest, indice))


