#!/usr/bin/python3

matriz = [
	[11, 12, 13, 14, 15],
	[21, 22, 23, 24, 25],
	[31, 32, 33, 34, 35],
	[41, 42, 43, 44, 45],
	[51, 52, 53, 54, 55],
]

def printar_matriz(mat):
	for linha in range(len(mat)):
		for coluna in range(len(mat[linha])):
			print(mat[linha][coluna], end="")
			if coluna + 1 < len(mat[linha]):

printar_matriz(matriz)