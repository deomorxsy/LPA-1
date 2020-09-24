#!/usr/bin/python3
# date: 23/09/2020
'''
URI Online Judge | 1143
Squared and Cubic

Write a program that reads an integer N (1 < N < 1000). This N is the number of output lines
printed by this program.

Input: The input file contains an integer N.
Output: Print the output according to the given example.

'''
linhas = int(input())

while (linhas > 1) and (linhas < 1000):
	for i in range(1,linhas+1):
		print(i, i**2, i**3)
	break

