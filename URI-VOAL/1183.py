#!/usr/bin/python3
#date: 04/11/2020

operation = input()
matriz = []
jumper = 0 #makes the diagonal
somatorio = 0
amount = 0 #amount of times somatorio was added

#1) creates all slots of the matrix
for i in range(12):
	matriz = matriz + [[0]*12]

#2) puts the float inputs inside all sublists' indexes
for i in range(12):
	for index in range(12):
		matriz[i][index] = float(input())

#print(len(matriz)) #DEBUGGER

#3) delimiting the diagonal DEBUGGER
'''
for i in range(12):
	print(matriz[i][jumper])
	jumper = jumper + 1
'''
#4) Summation of elements above diagonal.
for i in range(12):
	for index in range(12):
		if index <= jumper: 
		#if the index value is lower or equal to jumper, ignore and jump a step.
			continue 
			#jumps the step if index value is lower or equal to jumper
		somatorio = somatorio + matriz[i][index]
		amount = amount + 1
		#since we are skipping the steps that doesn't count, 
		#we can just add the values to somatorio.	

	jumper = jumper + 1
	#here, jumper is incremented. 
	#It's important to be after the second 
	#for block and in the same indentation depth.

'''DEBUGGER
for i in matriz:
	print(i)
'''

#5) using if statements to check the binary choice
if operation == 'S':
	print("{:.1f}".format(somatorio))

if operation == 'M':
	media = (somatorio/amount)
	print("{:.1f}".format(media))
