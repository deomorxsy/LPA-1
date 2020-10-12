#!/usr/bin/python3
#date: 08/10/2020
#Fuel Spent, 1017

spent_time = int(input())#hours
avg_speed = int(input()) #average speed km/h

km_liter = 12 #km/l

print("{:.3f}".format((avg_speed / km_liter) * spent_time))
