#!/usr/bin/python3
'''
Sphere

Make a program that calculates and shows the volume of a sphere being provided the value of
 its radius (R) . The formula to calculate the volume is: (4/3) * pi * R³. Consider (assign)
 for pi the value 3.14159.

Tip: Use (4/3.0) or (4.0/3) in your formula, because some languages (including C++) assume
 that the division's result between two integers is another integer. :)

Input: The input contains a value of floating point (double precision).
Output: The output must be a message "VOLUME" like the following example with a space
 before and after the equal signal. The value must be presented with 3 digits after
 the decimal point.

'''

def main():
	#volume of a sphere

	radius = float(input())
	pi = 3.14159

	volume = (4.0/3.0) * pi * (radius ** 3)

	return print("VOLUME = {:.3f}".format(volume))
if __name__ == '__main__':
	main()