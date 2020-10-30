#!/usr/bin/python3

numbers = [] #lista de entrada
srebmun = [] #lista auxiliar

#
for i in range(20):
	numbers = numbers + [int(input())]

''' 
Desafio1: reproduzir o código abaixo
sem o uso de funções embutidas.

Desafio2: mudar a lista de entrada sem utilizar 
lista auxiliar.

for i in numbers[::-1]:
	print(i)
'''


for item in range(len(numbers)):
	srebmun = srebmun + [numbers[(len(numbers)-1) - item]]

for index in range(len(srebmun)):
	print('N[{}] = {}'.format(index, srebmun[index]))

