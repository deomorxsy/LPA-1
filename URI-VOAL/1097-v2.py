#!/usr/bin/python3
#date: 17/09/2020
'''
Sequence IJ 3

Make a program that prints the sequence like the following exemple.
Input: This problem doesn't have input.
Output: Print the sequence like the example below.
'''

def iterator(iterator, coluna1, coluna2):
	# iterador do index da sublista de index[0] da coluna J.
	while (iterator >= 0):
		print("I={} J={}".format(I[0], J[0][iterator]))
		iterator -= 1


def main():

	I = [1, 3, 5, 7, 9] #following the logic from the problem 1096
	J = [[5, 6, 7], [7,8,9], [9,10,11], [11,12,13], [13,14,15]]

	#repetidor = 3
	index = 2
	index2 = 2
	while (index >= 0):
		print("I={} J={}".format(I[0], J[0][index]))
		index -= 1

	while (index2 >= 0):
		print("I={} J={}".format(I[1], J[1][index2]))
		index2 -= 1


if __name__ == '__main__':
	main()