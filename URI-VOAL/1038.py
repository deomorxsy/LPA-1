#!/usr/bin/python3
#date: 02/10/2020
'''
Cachorro Quente 4.00 
X-Salada 4.50
X-Bacon 5.00
Torrada simples 2.00
Refrigerante 1.50
'''
code, amount = [int(item) for item in input().split()]
cardapio = [4.00, 4.50, 5.00, 2.00, 1.50]

print("Total: R$ {:.2f}".format(cardapio[code-1] * amount))

