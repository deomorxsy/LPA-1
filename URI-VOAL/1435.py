#!/usr/bin/python3
#date:11/11/2020

order = 1

while order != 0:
	cansado = 1
	order = int(input())
	matrix = []

	for i in range(order):
		matrix = matrix + [[1]*order]

	while True:
		for i in range(cansado,len(matrix)-cansado):
			for item in range(cansado,len(matrix[i])-cansado):
				matrix[i][item] = cansado+1
		if cansado == (len(matrix)//2)+1 or cansado == (len(matrix)//2):
			break
		cansado += 1

	for i in range(len(matrix)):
		print(end="  ")
		for j in range(len(matrix[i])):
			if j < order-1:#j > 0 and:
				#if len(str(matrix[i][j])) == 1:
					#print(matrix[i][j], end="   ")
				if len(str((matrix[i][j+1]))) == 2:
					print(matrix[i][j], end="  ")
				#if len(str(matrix[i][j])) == 2 or len(str(matrix[i][j])) == 3:
					#print(matrix[i][j], end="")
				else:
					print(matrix[i][j], end="   ")
			elif j == order-1:
				print(matrix[i][j])
			#if i == len(matrix)-1 and j == len(matrix)-1:
				#print()
			
	if order != 0:
		print()

	if order == 0:
		#print()
		break

