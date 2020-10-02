#!/usr/bin/python3
#date: 02/10/2020

entrada = float(input())

intervalos_str = ["[0,25]", "(25,50]", "(50,75]", "(75,100]"]
intervalos = [[0,25], [25,50], [50,75], [75,100]]

if entrada >= 0 and entrada <= 25:
	print("Intervalo {}".format(intervalos_str[0]))

elif entrada > 25 and entrada <= 50:
	print("Intervalo {}".format(intervalos_str[1]))

elif entrada > 50 and entrada <= 75:
	print("Intervalo {}".format(intervalos_str[2]))

elif entrada > 75 and entrada <= 100:
	print("Intervalo {}".format(intervalos_str[3]))

elif entrada < 0 or entrada > 100:
	print("Fora de intervalo")