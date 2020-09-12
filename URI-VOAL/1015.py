#!/usr/bin/python3

'''
Distance Between Two Points

Read the four values corresponding to the x and y axes of two points in the plane,
 p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing four
 decimal places after the comma, according to the formula:

Distance =

Input: The input file contains two lines of data. The first one contains two double
 values: x1 y1 and the second one also contains two double values with one digit after
 the decimal point: x2 y2.
Output: Calculate and print the distance value using the provided formula, with 4 digits
 after the decimal point.
'''

def main():
	#we could use two lines like this:
	'''
	x = input()
	y = input()
	'''
	#however, it would make the code longer than it is necessary. So just put the input
	# and add a .split() method 
	p1 = input().split(' ')
	p2 = input().split(' ')
	'''
	PS: you can't transform the input's type to int above yet. Because it's still a list. 
	But when you slice it, then it works. Just like below.
	'''
	x1 = float(p1[0]) #... and it don't work! Why?!
	y1 = float(p1[1])

	'''
	because the input of this exercise contains double values. Which, in python, is built-in 
	inside float. And you can't take decimals inside int(). float() is suited for it.

	"[...] Computers store numbers in a variety of different ways. Python has two main ones. 
	Integers, which store whole numbers (ℤ), and floating point numbers, which store real 
	numbers (ℝ). You need to use the right one based on what you require. [...]" -Gareth Latty

	further reading: https://stackoverflow.com/a/13861656/7681246
	'''
	x2 = float(p2[0])
	y2 = float(p2[1])

	distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
	#you can use sqrt() from python's math library, but it is built-in...

	return print("{:.4f}".format(distance))
if __name__ == '__main__':
	main()