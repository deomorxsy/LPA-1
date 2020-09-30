#!/usr/bin/python3
#date: 30/09/2020
banknotes = [100, 50, 20, 10, 5, 2, 1] 

value = int(input())
accumulator = value#accumulator inverso

notas = []
for i in range(len(banknotes)):
	while accumulator // banknotes[i] != 0:
		notas.append(accumulator // banknotes[i])
		#accumulator = accumulator % banknotes[i]
		#print("Quando a divisão NÃO É ZERO", notas, "accumulator= ", accumulator)
		break
	while accumulator // banknotes[i] == 0:
		notas.append(accumulator // banknotes[i])
		#accumulator = accumulator % banknotes[i]
		#print("Quando a divisão é ZERO", notas, "accumulator= ", accumulator)
		break
	accumulator = accumulator % banknotes[i]

print(value)
for i in range(7):
	print("{} nota(s) de R$ {},00".format(notas[i], banknotes[i]))
