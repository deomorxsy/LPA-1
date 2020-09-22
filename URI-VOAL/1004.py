#!/usr/bin/python3
# -*- coding: utf-8 -*-
#date: 13/09/2020

'''
Simple Product

Read two integer values. After this, calculate the product between them and store
 the result in a variable named PROD. Print the result like the example below.
 Do not forget to print the end of line after the result, otherwise you will receive
 “Presentation Error”.

Input: The input file contains 2 integer numbers.
Output: Print the message "PROD" and PROD according to the following example, with
 a blank space before and after the equal signal.

'''
int01 = int(input())
int02 = int(input())

PROD = int01 * int02

print("PROD = {}".format(PROD))
