#!/usr/bin/python3
#date: 08/10/2020
testes = int(input())
entradas = ""

saidas = []

for i in range(testes):
	entradas = int(input())
	if (entradas % 2 == 0) and (entradas > 0): #par e positivo
		saidas = saidas + ["EVEN POSITIVE"]
	elif (entradas % 2 == 0) and (entradas < 0): #par e negativo
		saidas = saidas + ["EVEN NEGATIVE"]
	elif (entradas % 2 != 0) and (entradas > 0): #impar e positivo
		saidas = saidas + ["ODD POSITIVE"]
	elif (entradas % 2 != 0) and (entradas < 0): #impar e negativo
		saidas = saidas + ["ODD NEGATIVE"]
	elif (entradas == 0):
		saidas = saidas + ["NULL"]

for i in saidas:
	print(i)

