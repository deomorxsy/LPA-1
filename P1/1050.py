#!/usr/bin/python3
#date: 08/10/2020
ddd = [61, 71, 11, 21, 32, 19, 27, 31]
destination = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]

code_number = int(input())
somatorio = 0

for item in ddd:
	somatorio += 1

if code_number in ddd:
	for item in range(somatorio-1):
		if code_number	== ddd[item]:
			print(destination[item])
else:
	print("DDD nao cadastrado")