#!/usr/bin/python3
#date: 01/10/2020
def main():
	'''
	Then if B is greater than C and D is greater than A and
	if the sum of C and D is greater than the sum of A and B
	and if C and D were positives values and if A is even, write
	the message “Valores aceitos” (Accepted values). Otherwise,
	write the message “Valores nao aceitos” (Values not accepted).
	'''
	a, b, c, d = [int(x) for x in input().split()]
	
	if ( (b > c) and (d > a) and (c + d) > (a + b)
	 and (c > -1) and (d > -1) and (a % 2 == 0) ):	
		return print("Valores aceitos")
	else:
		return print("Valores nao aceitos")
		#return print(abcd)

if __name__ == '__main__':
	main()
