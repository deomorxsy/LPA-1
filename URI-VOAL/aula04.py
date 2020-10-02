#!/usr/bin/python3
#date: 01/10/2020
#INCOMPLETO 
#modelo torre de hanói
y = 5
x = 3
#maior = 0

if y > x:
	#maior = y #5
	#y = x #3
	#x = maior #5
	x = x + y #8
	y = x - y #3
	x = x - y #5