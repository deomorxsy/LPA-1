#!/usr/bin/python3
'''
#date: 12/09/2020

Average 2

Read three values (variables A, B and C), which are the three student's grades. Then, calculate
 the average, considering that grade A has weight 2, grade B has weight 3 and the grade C has
 weight 5. Consider that each grade can go from 0 to 10.0, always with one decimal place.

Input: The input file contains 3 values of floating points with one digit after the decimal point.
Output: Print the message "MEDIA"(average in Portuguese) and the student's average according 
 to the following example, with a blank space before and after the equal signal.
'''

A = float(input())
B = float(input())
C = float(input())

PesoA = 2
PesoB = 3
PesoC = 5

denominador = PesoA + PesoB + PesoC

MEDIA = ((A * PesoA)+(B * PesoB)+(C * PesoC)) / denominador

print("MEDIA = {:.1f}".format(MEDIA))