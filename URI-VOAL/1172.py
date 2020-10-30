#!/usr/bin/python3
#date: 29/10/2020

lista = []

for i in range(10):
	lista = lista + [int(input())]

for i in range(len(lista)):
	if (lista[i] == 0) or (lista[i] < 0):
		lista[i] = 1

for i in range(len(lista)):
	print("X[{}] = {}".format(i, lista[i]))