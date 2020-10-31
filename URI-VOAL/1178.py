#!/usr/bin/python3
#date: 30/10/2020

array = [float(input())]
y = array[0]

for i in range(99):
	array = array + [y / 2.0]
	y = y / 2.0

for i in range(len(array)):
	print("N[{}] = {:.4f}".format(i, array[i]))