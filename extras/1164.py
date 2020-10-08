#!/usr/bin/python3

tests = int(input())
somatorio = 0
accumulator = []

numeros = []

for i in range(tests):
	number = int(input())
	numeros = numeros + [number] #APPEND

	for index in range(1,number+1):
		if number % index == 0 and index != number:
			somatorio += index
			#print(somatorio)
	accumulator = accumulator + [somatorio] #APPEND
	somatorio = 0

#for i in range(1,len(accumulator)-1,3):
#	print(accumulator[i])
#print(accumulator) #DEBUGGER
#print(numeros) #DEBUGGER

for i in range(len(accumulator)):
	if accumulator[i] == numeros[i]:
		print("{} eh perfeito".format(numeros[i]))
	else:
		print("{} nao eh perfeito".format(numeros[i]))