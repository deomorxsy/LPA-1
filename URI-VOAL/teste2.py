#!/usr/bin/python3


nf = int(input()) #numero de funcionario
nh = int(input()) #horas trabalhadas
vh = float(input()) #valor/hora
sl = float(nh * vh) #salario

print('NUMBER = '.format(nf))
print('SALARY = U$ {:.2f}'.format(sl))

'''
print('NUMBER = {}',nf)
print('SALARY = U$ %.2f'%sl)
'''