#!/usr/bin/python3

coluna1 = '0' #I
coluna2 = '123'

accumulator = 0
index = 0
somador = 0.2
somador_col2 = somador
#while (accumulator <= 11):

while (index <= 2):
	print("I={} J={}".format(coluna1, coluna2[index]))
	index += 1

index = 0
while (index <= 2):
	print("I={:.1f} J={:.1f}".format( float(coluna1) + somador, (float(coluna2[index]) + somador)))
	index += 1

while (accumulator < 3):
	somador += 0.2
	index = 0
	while (index <= 2):
		print("I={:.1f} J={:.1f}".format( float(coluna1) + somador, (float(coluna2[index]) + somador)))
		index += 1
	accumulator+=1
	print("\nsomador={}\naccumulator={}\n===========\n".format(somador, accumulator)) 



'''
0
somador
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
'''
