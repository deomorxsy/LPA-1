#!/usr/bin/python3
#date: 12/10/2020

a, b = [int(x) for x in input().split()]

if a % b == 0 or b % a == 0:
	print("Sao Multiplos")
else:
	print("Nao sao Multiplos")