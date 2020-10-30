#!/usr/bin/python3
#date: 29/10/2020

a_array = []

for i in range(100):
	a_array = a_array + [eval(input())]

#print("=====")
for index in range(len(a_array)):
	if a_array[index] <= 10: #menor ou igual.
		print("A[%d] = %.1f" %(index, a_array[index])) #old string formatting
		#print("A[{}] = {:.1f}".format(index, a_array[index])) # new string formatting