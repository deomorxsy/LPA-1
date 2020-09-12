#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
Area of a Circle

The formula to calculate the area of a circumference is defined as A = π . R2.
 Considering to this problem that π = 3.14159: 
 Calculate the area using the formula given in the problem description.

Input: The input contains a value of floating point (double precision), that is the variable R.
Output: Present the message "A=" followed by the value of the variable, as in the example
 bellow, with four places after the decimal point. Use all double precision variables.
 Like all the problems, don't forget to print the end of line after the result, otherwise
 you will receive "Presentation Error".
'''

raio = float(input()) #Python has built-in double precision values INSIDE float values. 
#In C, it would be necessary to specify as "double". 

pi = 3.14159
A = pi * (raio ** 2)

print("A={:.4f}".format(A)) 
# to print a float with decimal places in python you need to specify the
# conversion field. The colon ':' starts it and following we have ".Nf"
# which specifies the number of decimal places to be shown.