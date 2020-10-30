#!/usr/bin/python3
#date: 30/10/2020

foo = []
entrada = int(input())

while len(foo) <= 1000:
	for i in range(entrada):
		if len(foo) <= 1000:
			foo = foo + [i]

for i in range(len(foo)-1):
	print("N[{}] = {}".format(i, foo[i]))