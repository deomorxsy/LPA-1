#!/usr/bin/python3

'''
Sum of Consecutive Odd Numbers II

Read an integer N that is the number of test cases. Each test case is a line containing two integer numbers X and Y. Print the sum of all odd values between them, not including X and Y.
Input

The first line of input is an integer N that is the number of test cases that follow. Each test case is a line containing two integer X and Y.
Output

Print the sum of all odd numbers between X and Y.
'''

teste = input();
accumulator = '';
index_finder = 0;

comeco = 0; #N
fim = 0; #Y

for i in range(len(teste) - 1):
	#if teste[i] == ' ':
		#print("Espaço está em {}".format(i))
	while (teste[i] == ' '):
		index_finder = i;
		break;
	#range(len(teste)) vai retornar 5. Porém o index em strings e listas começa em 0. Por isso o -1.
	#Deixar sem o -1 retorna out of range.
	#O for loop escaneará todos os indexes até encontrar a condição prevista no while loop.
	#Uma vez atendida, a condição fará com que index_finder, que antes era 0 (int), receba como atribuição i,
	#que é o valor do index.
	#O break encerra ambos os loops.

comeco = int(teste[0:index_finder])
fim = int(teste[index_finder+1:])
print("accumulator={}".format(accumulator))
print("index_finder = {}".format(index_finder))
