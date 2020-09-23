#!/usr/bin/python3

'''
 URI Online Judge | 1114
Fixed Password

Write a program that keep reading a password until it is valid. For each wrong password
read, write the message "Senha inválida". When the password is typed correctly print the
message "Acesso Permitido" and finished the program. The correct password is the number
2002.

Input: The input file contains several tests cases. Each test case contains only an integer
number.
Output: For each number read print a message corresponding to the description of the problem.

"Senha Invalida"
"Acesso Permitido"
'''
switch = 1 # switch is True
password = 0

fixed_password = 2002

while switch == 1:
	
	password = int(input())

	while password != fixed_password:
		print("Senha Invalida")
		break

	while password == fixed_password:
		print("Acesso Permitido")
		switch = 0
		break