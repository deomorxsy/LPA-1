#!/usr/bin/python3

'''
Distance

Two cars (X and Y) leave in the same direction. The car X leaves with a constant speed of
 60 km/h and the car Y leaves with a constant speed of 90 km / h.

In one hour (60 minutes) the car Y can get a distance of 30 kilometers from the X car, in
 other words, it can get away one kilometer for each 2 minutes.

Read the distance (in km) and calculate how long it takes (in minutes) for the car Y to take
 this distance in relation to the other car.

Input: The input file contains 1 integer value.
Output: Print the necessary time followed by the message "minutos" that means minutes in
 Portuguese.
'''

def main():
	distance = int(input())#in km

	necessary_time = distance * 2
	#if in each 2 mins the Y car moves away 1km from the X car, and if in 60mins the Y car is 30km
	 #away from the X car (taking as reference the X car, in the 0km), then, in this case, the output
	 #will be the double of the distance.
	return print("{} minutos".format(necessary_time))

if __name__ == "__main__":
	main()