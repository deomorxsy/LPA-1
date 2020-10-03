#!/usr/bin/python3
#date: 03/10/2020

#coordenadas (x,y)
coord = [float(x) for x in input().split()]

if coord[0] > 0 and coord[1] > 0: #ambos positivos
	print("Q1")
elif coord[0] < 0 and coord[1] > 0: #x negativo, y positivo
	print("Q2")
elif coord[0] < 0 and coord[1] < 0: #ambos negativos
	print("Q3")
elif coord[0] > 0 and coord[1] < 0: #x positivo, y negativo
	print("Q4")
elif coord[0] == 0 and coord[1] == 0: #ambos 0; Origem
	print("Origem")
elif (coord[0] > 0 or coord[0] < 0) and coord[1] == 0:
	print("Eixo X")
elif coord[0] == 0 and (coord[1] > 0 or coord[1] < 0):
	print("Eixo Y")
