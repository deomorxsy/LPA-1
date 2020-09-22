#!/usr/bin/python3
#date: 22/09/2020
'''
for c in range(0,10+1):
	while c < 10+1 and c % 3 != 0:
		print(c, sep=' ', end='\n')
		break
	while c % 3 == 0:
		print(c, sep=' ', end=' ')
		break
	#print("")
'''

entrada = input().split(' ')

for i in range(len(entrada)):
	entrada[i] = int(entrada[i])

colunas = entrada[0]
iterator = entrada[1]

for c in range(1,iterator+1):
    while c % colunas != 0:
        print(c, end=' ')
        break
    while c % colunas == 0:
        print(c, sep=' ')
        break

