#!/usr/bin/python3
'''
Time Conversion

Read an integer value, which is the duration in seconds of a certain event in a factory,
 and inform it expressed in hours:minutes:seconds.
Input: The input file contains an integer N.
Output: Print the read time in the input file (seconds) converted in hours:minutes:seconds
 like the following example.

'''

def main():
	duration = int(input()) #duration of an event in factory
	
	horas = duration // 3600 #38
	minutos = (duration % 3600) // 60
	segundos = (duration % 3600) % 60


	return print("{}:{}:{}".format(horas, minutos, segundos))

if __name__ == "__main__":
	main()