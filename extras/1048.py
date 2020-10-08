#!/usr/bin/python3

salary = float(input())
reajuste = 0
if salary >= 0 and salary <= 400.00:
	reajuste = (salary * 0.15)
	#print(reajuste + salary)
	
	print("Novo salario: {:.2f}".format((reajuste + salary),))
	print("Reajuste ganho: {:.2f}".format(reajuste))
	print("Em percentual: 15 %")
	
elif salary >= 400.01 and salary <= 800.00:
	reajuste = (salary * 0.12)
	#print(reajuste + salary)
	
	print("Novo salario: {:.2f}".format((reajuste + salary),))
	print("Reajuste ganho: {:.2f}".format(reajuste))
	print("Em percentual: 12 %")
	
elif salary >= 800.01 and salary <= 1200.00:
	reajuste = (salary * 0.10)
	#print(reajuste + salary)
	
	print("Novo salario: {:.2f}".format((reajuste + salary),))
	print("Reajuste ganho: {:.2f}".format(reajuste))
	print("Em percentual: 10 %")
	
elif salary >= 1200.01 and salary <= 2000.00:
	reajuste = (salary * 0.07)
	#print(reajuste + salary)
	
	print("Novo salario: {:.2f}".format((reajuste + salary),))
	print("Reajuste ganho: {:.2f}".format(reajuste))
	print("Em percentual: 7 %")
	
elif salary >= 2000.01:
	reajuste = (salary * 0.04)
	#print(salary * 0.04)
	
	print("Novo salario: {:.2f}".format((reajuste + salary),))
	print("Reajuste ganho: {:.2f}".format(reajuste))
	print("Em percentual: 4 %")
	