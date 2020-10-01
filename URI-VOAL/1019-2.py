#!/usr/bin/python3

duration = int(input())
accumulator = duration

lista = []
for i in range(1):
	#when number of hours is different than the number itself and 0:
	if duration % 3600 != duration or duration // 3600 == 0:
		lista.append(duration // 3600)
		accumulator = duration % 3600
		#print("PRIMEIRO IF")
		#break
	#when mins are different than the number itself
	if accumulator // 60 != accumulator:
		lista.append(accumulator // 60)
		lista.append(accumulator % 60)
		#print("SEGUNDO IF")
		#break

[print(lista[i], end=':') if lista[i] != lista[len(lista)-1] else print(lista[i]) for i in range(len(lista))]

#print(lista)#[0], lista[1], lista[2], sep=':')
