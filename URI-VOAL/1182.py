#!/usr/bin/python3
#date:04/11/2020

coluna = int(input())
operation = input()

matriz = []
somatorio = 0
media = 0

#Cria os 144 slots para matriz (12x12)
for i in range(12):
	matriz = matriz + [[0]*12]

#print(len(matriz)) #DEBUGGER
#matriz[0][2] = 80 #DEBUGGER
#print(matriz[0]) #DEBUGGER

#Adiciona os floats da entrada em cada um
#dos slots
for i in range(12):
	for index in range(12):
		matriz[i][index] =  float(input())


#print(len(matriz)) #DEBUGGER

#DEBUGGER
#for i in range(12):
	#print(matriz[i])

#print("============") #DEBUGGER

#Faz o somatorio dos itens de cada coluna
for i in range(12):
	for index in range(12):
		if index == coluna:
			#print(matriz[i][index])
			somatorio = somatorio + matriz[i][index]

if operation == 'S':
	print("{:.1f}".format(somatorio))

if operation == 'M':
	media = (somatorio/12)
	print("{:.1f}".format(media))

