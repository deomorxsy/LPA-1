#!/usr/bin/python3

ddd = [61, 71, 11, 21, 32, 19, 27, 31]
destination = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]
entrada = int(input())

for i in range(len(ddd)-1):
	if entrada == ddd[i]:
		print(destination[i])

if not(entrada in ddd):
	print("DDD nao cadastrado")