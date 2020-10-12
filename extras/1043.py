#!/usr/bin/python3
#date: 12/10/2020
#1) Read three point floating values (A, B and C)
a, b, c = [float(x) for x in input().split()]

tera = ((b - c) * -1) if (b - c) < 0 else (b - c)
terb = ((a - c) * -1) if (a - c) < 0 else (a - c)
terc = ((a - b) * -1) if (a - b) < 0 else (a - b)
'''
Se a diferença entre B e C for NEGATIVA, converte o número para POSITIVO,
#multiplicando por -1, e retorna como valor da variável.
Se a diferença entre B e C não for negativa, retorna apenas a diferença entre B e C.
'''
flag = 0
perimetro = 0.0
trapezio = 0.0
#2) verify if is possible to make a triangle with them.
if (b + c) > a and a > tera:
	flag = flag + 1
if (a + c) > b and b > terb:
	flag = flag + 1
if (a + b) > c and c > terc:
	flag = flag + 1

#print("FLAG={}".format(flag)) #DEBUGGER

#3) If it is possible, calculate the perimeter of the triangle and print the message:
#Perimetro = XX.X
if flag == 3:
	perimetro = a + b + c
	print("Perimetro = {:.1f}".format(perimetro))

#4)If it is not possible, calculate the area of the trapezium which 
#basis A and B and C as height, and print the message:
#Area = XX.X
else:
	trapezio = ((a + b) * c) / 2.0
	print("Area = {:.1f}".format(trapezio))

