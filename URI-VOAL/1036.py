#!usr/bin/python3

'''
? > 0 → a função do 2º grau possui duas raízes reais distintas.
? = 0 → a função do 2º grau possui apenas uma raiz real.
? < 0 → a função do 2º grau não possui nenhuma raiz real. 

"O valor de a é o único que não pode ser igual a zero. Isso porque a função deixaria de ser
 de segundo grau, ou seja, a formação de f(x) = ax² + bx + c passaria para f(x) = ax + b."
'''
a,b,c = [float(valores) for valores in input().split()]

delta = (b ** 2) - (4 * a * c)

if delta > 0 and a != 0:
	r1 = (-b + (delta ** 0.5)) / (2.0 * a)
	r2 = (-b - (delta ** 0.5)) / (2.0 * a)
	print("R1 = {:.5f}".format(r1))
	print("R2 = {:.5f}".format(r2))
else:
	print("Impossivel calcular")

