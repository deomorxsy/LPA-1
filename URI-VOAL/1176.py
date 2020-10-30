#!/usr/bin/python3

num_casos = int(input())
th_element = []
listado = [0, 1]
auxiliar = listado #vai guardar o valor do índice de listado
# correspondente ao número da sequencia de fibonacci
'''
0[0], 1[1]
1[2], 2[3]
3[4], 5[5]
8[6], 13[7],
21[8], 34[9],
55[10], 89[11],
144[12]
'''

for i in range(num_casos):
	th_element = th_element + [int(input())]

#print("len(th_element)={}".format(len(th_element)))
#print("========+")
for index in range(len(th_element)): #len(th_element)-1
	for numero in th_element:
		c = listado[len(listado)-1] + listado[len(listado)-2]
		listado = listado + [c]
	#print("th_element={}".format(th_element))
	print("Fib({}) = {}".format(th_element[index],listado[th_element[index]]))
#for item in th_element:print(listado)

	