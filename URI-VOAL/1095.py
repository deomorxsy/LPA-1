#!/usr/bin/python3

'''
Sequence IJ 1

Make a program that prints the sequence like the following example.
Input: This problem doesn't have input.
Output: Print the sequence like the example below.
'''

def main():
	J=60
	I=1

	while (J > -1):
		print("I={} J={}".format(I,J))
		I += 3
		J -= 5

if __name__ == '__main__':
	main()