#!/usr/bin/python3
#date: 12/09/2020
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
	#Nex = 140153

	horas = duration // 3600 #38
	minutos = (duration % 3600) // 60 #(140153 % 3600) // 60 | 3353 // 60 = 55
	segundos = (duration % 3600) % 60 #(140153 % 3600) % 60  | 3353 % 60 = 53


	return print("{}:{}:{}".format(horas, minutos, segundos))

if __name__ == "__main__":
	main()