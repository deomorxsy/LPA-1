#!/usr/bin/python3
'''
Sequence IJ 3

Make a program that prints the sequence like the following exemple.
Input: This problem doesn't have input.
Output: Print the sequence like the example below.
'''

coluna2_J1 = '567'
coluna2_J2 = '789'
coluna2_J3 = '91011'#9 com 1 casa decimal
coluna2_J4 = '111213'
coluna2_J5 = '131415'

coluna1 = '13579'
index = 2

#Coluna I e Coluna J1
while (index >= 0):
	print("I={} J={}".format(coluna1[0], coluna2_J1[index]))
	index -= 1

#Coluna I e Coluna J2
index = 2
while (index >= 0):
	print("I={} J={}".format(coluna1[1], coluna2_J2[index]))
	index -= 1

#Coluna I e Coluna J3(9). Coluna J3(10 e 11) dentro do while.

index=4

while (index > 0):
	print("I={} J={}".format(coluna1[2], (coluna2_J3[index-1] + coluna2_J3[index]) ))
	index -= 2
print("I={} J={}".format(coluna1[2], coluna2_J3[0]))

#Coluna I e Coluna J4(11, 12 E 13)
index=5

while (index > 0):
	print("I={} J={}".format(coluna1[3], (coluna2_J4[index-1] + coluna2_J4[index]) ))
	index -= 2 #O que acontece quando coloco 1?

#Coluna I e Coluna J5(15, 14 e 13)
index = 5
while (index > 0): 
	print("I={} J={}".format(coluna1[4], (coluna2_J5[index-1] + coluna2_J5[index]) ))
	index -= 2

'''

index = 4

while (index >= 1): #coluna2_J3 = '91011'#9 com 1 casa decimal
	#A cada iteração, index pula dois números à frente. index nesse ponto é 1.
	#SE coluna2_J3[1] = 1 E coluna2_J3[2] = 0, Então coluna2_J3[1] + coluna2_J3[2] = 10.
	print("I={} J={}".format(coluna1[2], (coluna2_J3[index-1] + coluna2_J3[index + 1]) ))
	index -= 2 #Aqui, 2 + index é atribuído ao index. Isso dá 3. O loop continua e dessa vez:
	#SE coluna2_J3[3] = 1 E coluna2_J3[4] = 1, então coluna2_J3[3] + coluna2_J3[4] = 11.



'''
