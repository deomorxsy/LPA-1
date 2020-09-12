# -*- coding: utf-8 -*-
#!/usr/bin/python3

'''
Extremely Basic - Read 2 variables, named A and B and make the sum of these two variables,
 assigning its result to the variable X. Print X as shown below. Print endline after the
 result otherwise you will get “Presentation Error”.

Input: The input file will contain 2 integer numbers.
Output: Print the letter X (uppercase) with a blank space before and after the equal
 signal followed by the value of X, according to the following example.

Obs.: don't forget the endline after all.

'''

#A, B = input(), input()

A = int(input()) #reads any input and place it on the variable as a STRING.
B = int(input())

X = A + B 
#Trying to sum it will return error. This will only concatenate it. So, 3 + 2 will
# return 32, because A and B type is STR (string).

print("X = {}".format(int(X))) 
#if you convert it to INTEGER here, it will not work.
# Has to be directly in the variable.

