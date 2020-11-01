#!/usr/bin/python3
#date: 01/11/2020

matrix = []
row = int(input())

sum_avg = input()
somatorio = 0
media = 0

#cria uma matriz, um modelo multidimensional de array
for i in range(12):
	matrix = matrix + [[0]*12]

#DEBUGGER: printa como era a lista antes e seu comprimento
'''print("matrix length={}".format(len(matrix)))
for i in matrix:
	print(i)
'''
#adiciona as entradas a cada indice de indice
for item in range(len(matrix)):
	for index in range(len(matrix)):
		matrix[item][index] = float(input())

#DEBUGGER: printa como fica a lista depois e seu comprimento
'''
print("matrix length={}".format(len(matrix)))
for i in matrix:
	print(i)
'''
#sum_avg diz se é soma ou média.
#range 12 pois todo item dentro de matriz tem 12 itens.
#somatorio receberá a soma dos itens.
#row delimita o escopo do caso, i está iterando
#sobre cada item dentro dessa coluna.

for i in range(12):
	somatorio = somatorio + matrix[row][i]
#print(somatorio)

if sum_avg == 'S':	
	print("{:.1f}".format(somatorio))

if sum_avg == 'M':
	media = somatorio/len(matrix[row])
	print("{:.1f}".format(media))

print("matrix length={}".format(len(matrix)))
for i in matrix:
	print(i)
