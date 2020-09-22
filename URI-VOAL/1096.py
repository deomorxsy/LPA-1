#!/usr/bin/python3
#date: 17/09/2020
'''
Sequence IJ 2

Make a program that prints the sequence like the following exemple.

Input: This problem doesn't have input.
Output: Print the sequence like the example below.
'''

'''
def contador(coluna1, coluna2, accumulator, index):
	while (accumulator > -1):
		print("I={} J={}".format(coluna1[index], coluna2[accumulator]))
		accumulator -= 1

def main():
	I="1, 3, 5, 7, 9" #coluna1
	J=[5,6,7] #coluna2
	acc = 2 #accumulator
	
	#for i in range(len(I))
	return contador(I, J, acc, 0), contador(I, J, acc, 1), contador(I, J, acc, 2), contador(I, J, acc, 3), contador(I, J, acc, 4)

if __name__ == '__main__':
	main()

'''

coluna1 = '13579' #I
coluna2 = '765' #J
index = 0

while ( index < 3):
	print("I={} J={}".format(int(coluna1[0]), int(coluna2[index])))
	index += 1

index = 0

while ( index < 3):
	print("I={} J={}".format(int(coluna1[1]), int(coluna2[index])))
	index += 1

index = 0

while ( index < 3):
	print("I={} J={}".format(int(coluna1[2]), int(coluna2[index])))
	index += 1

index = 0

while ( index < 3):
	print("I={} J={}".format(int(coluna1[3]), int(coluna2[index])))
	index += 1

index = 0	

while ( index < 3):
	print("I={} J={}".format(int(coluna1[4]), int(coluna2[index])))
	index += 1

'''
	print("I=%d J=%d", int(13579/1000),int(765/100))# dúvida: se não converter, o python faz conversão implícita?
	denominador += '0'
	accumulator += 1
	'''