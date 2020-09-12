#!/usr/bin/python3

'''
Consumption

Calculate a car's average consumption being provided the total distance traveled (in Km)
 and the spent fuel total (in liters).

Input: The input file contains two values: one integer value X representing the total
 distance (in Km) and the second one is a floating point number Y  representing the
 spent fuel total, with a digit after the decimal point.

Output: Present a value that represents the average consumption of a car with 3 digits
 after the decimal point, followed by the message "km/l".
'''

def main():
	#If spent_fuel is given in km/l, then it's just divide the total distance per the spent fuel.
	t_distance = int(input())
	spent_fuel = float(input())

	average_con = t_distance/spent_fuel

	return print("{:.3f} km/l".format(average_con))
if __name__ == '__main__':
	main()