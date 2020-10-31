#!/usr/bin/python3
#date: 31/10/2020

an_array = []
par = []
impar = []

for i in range(15):
	an_array = an_array + [int(input())]

for i in range(15):
	if an_array[i] % 2 == 0:
		par = par + [an_array[i]]
		if (len(par)) == 5:
			for index in range(len(par)):
				print("par[{}] = {}".format(index, par[index]))
			par = []
	if an_array[i] % 2 == 1:
		impar = impar + [an_array[i]]
		if (len(impar) == 5):
			for index in range(len(impar)):
				print("impar[{}] = {}".format(index, impar[index]))
			impar = []

	'''
	if an_array[i] % 2 == 1 and i == 5:
		impar = impar + [an_array[i]]
		if (len(impar) < 5):
			print(impar)
	'''

for i in range(len(impar)):
	print("impar[{}] = {}".format(i, impar[i]))

for i in range(len(par)):
	print("par[{}] = {}".format(i, par[i]))

