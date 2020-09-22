#!/usr/bin/python3
#date: 12/09/2020
'''
Simple Calculate

In this problem, the task is to read a code of a product 1, the number of units of product 1,
 the price for one unit of product 1, the code of a product 2, the number of units of product 2
 and the price for one unit of product 2. After this, calculate and show the amount to be paid.

Input: The input file contains two lines of data. In each line there will be 3 values: two
 integers and a floating value with 2 digits after the decimal point.
Output: The output file must be a message like the following example where
 "Valor a pagar" means Value to Pay. Remember the space after ":" and after 
 "R$" symbol. The value must be presented with 2 digits after the point.

'''

def main():

	produto1 = input().split(' ')
	produto2 = input().split(' ')

	
	p1_code = int(produto1[0])
	p1_units = int(produto1[1])
	p1_price = float(produto1[2])

	p2_code = int(produto2[0])
	p2_units = int(produto2[1])
	p2_price = float(produto2[2])
	

	total = (p1_units * p1_price) + (p2_units * p2_price)

	return print("VALOR A PAGAR: R$ {:.2f}".format(total))
if __name__ == '__main__':
	main()

#print("valor p1 = {}".format(p2_units * p2_price))

'''	input1 = 12 1 5.30
	list1 = 0
	list1 = input1.split(' ') 
	list1
	['12', '1', '5.30'] '''