#!/usr/bin/python3
#date: 08/10/2020
# Interval, 1037. 

entrada = float(input())
#[0,25] (25,50], (50,75], (75,100]
# [] between; ( greater than
#print("Intervalo {}")

if (entrada >= 0.00) and (entrada <= 25.00):
	print("Intervalo [0,25]")
elif (entrada > 25.00) and (entrada <= 50.00):
	print("Intervalo (25,50]")
elif (entrada > 50.00) and (entrada <= 75.00):
	print("Intervalo (50,75]")
elif (entrada > 75.00) and (entrada <= 100.00):
	print("Intervalo (75,100]")
elif (entrada < 0.00) or (entrada > 100.00):
	print("Fora de intervalo")