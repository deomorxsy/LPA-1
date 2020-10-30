#!/usr/bin/python3
#date: 29/10/2020


lista_dobro = [int(input())]

for i in range(10):
	lista_dobro = lista_dobro + [lista_dobro[i]*2]

#print(lista_dobro)

for i in range(10):
	print("N[{}] = {}".format(i, lista_dobro[i]))


