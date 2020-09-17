#!/usr/bin/python3

'''
Sequence IJ 2

Make a program that prints the sequence like the following exemple.

Input: This problem doesn't have input.
Output: Print the sequence like the example below.
'''


def contador(coluna1, coluna2, accumulator, index):
	while (accumulator > -1):
		print("I={} J={}".format(coluna1[index], coluna2[accumulator]))
		accumulator -= 1

def main():
	I=[1, 3, 5, 7, 9] #coluna1
	J=[5,6,7] #coluna2
	acc = 2 #accumulator
	
	#for i in range(len(I))
	return contador(I, J, acc, 0), contador(I, J, acc, 1), contador(I, J, acc, 2), contador(I, J, acc, 3), contador(I, J, acc, 4)

if __name__ == '__main__':
	main()
