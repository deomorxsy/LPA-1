#!/usr/bin/python3

coluna1 = '0' #I
coluna2 = '123'

accumulator = 0
index = 0
somador = 0.2
somador_col2 = somador


while (index <= 2):
	print("I={} J={}".format(coluna1, coluna2[index]))
	index += 1

index = 0
while (index <= 2):
	print("I={:.1f} J={:.1f}".format(float(coluna1) + somador_col2, (float(coluna2[index]) + somador_col2)))
	index += 1

while (accumulator < 3):
	somador_col2 += 0.2
	index = 0
	while (index <= 2):
		print("I={:.1f} J={:.1f}".format(float(coluna1) + somador_col2, (float(coluna2[index]) + somador_col2)))
		index += 1
	accumulator+=1


somador_col2 += 0.2
accumulator+=1

index = 0
while (index <= 2):
	print("I={} J={}".format( int(float(coluna1) + somador_col2), int((float(coluna2[index]) + somador_col2)) ))
	index += 1


accumulator=0

while (accumulator <= 3): 
	somador_col2 += 0.2
	index = 0
	while (index <= 2):
		print("I={:.1f} J={:.1f}".format( float(coluna1) + somador_col2, (float(coluna2[index]) + somador_col2)))
		index += 1
	accumulator+=1

somador_col2 += 0.2
accumulator+=1

index = 0
while (index <= 2):
	print("I={} J={}".format( int(float(coluna1) + somador_col2), int((float(coluna2[index]) + somador_col2)) ))
	index += 1
