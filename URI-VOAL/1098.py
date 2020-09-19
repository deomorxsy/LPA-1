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
	print("I={:.1f} J={:.1f}".format( float(coluna1) + somador_col2, (float(coluna2[index]) + somador_col2)))
	index += 1

#AUTOMATED LOOP 1
while (accumulator < 3):
	somador_col2 += 0.2
	index = 0
	while (index <= 2):
		print("I={:.1f} J={:.1f}".format( float(coluna1) + somador_col2, (float(coluna2[index]) + somador_col2)))
		index += 1
	accumulator+=1
	#DEBUGGER: print("\nsomador_col2={}\naccumulator={}\n===========\n".format(somador_col2, accumulator)) 


somador_col2 += 0.2
accumulator+=1
# These two above are needed. If they were set to run one more loop, they would be equal to a string that represents a float.
# And we need a string that represents an INT or an INT itself. BTW, this "one more loop" is represented by the logical operator ">=" in "index >= 3";
# This, of course, represents 4 iterations, since we want our index starting at 0.

#STOP and print int coluna1 and coluna2.
index = 0
while (index <= 2):
	print("I={} J={}".format( int(float(coluna1) + somador_col2), int((float(coluna2[index]) + somador_col2)) ))
	index += 1

'''

accumulator=0

while (accumulator <= 3): 
	# at the end of the loop, (I=1.8 e J=4.8). Se a condição do while fosse "accumulator <= 4", isso
	#printaria a última linha, porém, no formato FLOAT(que na realidade é uma String que representa
	#um float), o que não seria lido pelo URI, que pede algo formatado como int (ou uma string que 
	#emule esse int).
	somador_col2 += 0.2
	index = 0
	while (index <= 2):
		print("I={:.1f} J={:.1f}".format( float(coluna1) + somador_col2, (float(coluna2[index]) + somador_col2)))
		index += 1
	accumulator+=1
	#DEBUGGER: print("\nsomador_col2={}\naccumulator={}\n===========\n".format(somador_col2, accumulator)) 


#STOP and print int coluna1 and coluna2.
index = 0
while (index <= 2):
	print("I={} J={}".format( int(float(coluna1) + somador_col2), int((float(coluna2[index]) + somador_col2)) ))
	index += 1

'''
'''
Expected output from coluna1 (I):

0
0.2
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
