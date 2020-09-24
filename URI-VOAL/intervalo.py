#!/usr/bin/python3
for x in range(len(intervalo)): 
	for index in range(len(intervalo[x])): 
		while ((intervalo[x][index] > intervalo[x][index+1]) or
		 (intervalo[x][index] > intervalo[x][index-1]) and 
		 (intervalo[x][index] % 2 != 0)):
			somatorio += i 
			print(somatorio) 
