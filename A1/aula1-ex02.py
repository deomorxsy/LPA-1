#!usr/bin/env python3
# 08/09/2020 SET

'''
2. Escreva um programa que leia um substantivo, uma
adjetivo e um verbo. Escreva as palavras lidas no seguinte
formato: “O” substantivo adjetivo verbo “sobre o cachorro
marrom preguiçoso”.
'''

substantivo = input("Digite um substantivo: ") #Sem quebra de linha pra ficar mais legível na execução
adjetivo = input("Digite um adjetivo: ")
verbo = input("Digite um verbo: ")

#Abaixo o espaço após o "O" e antes de "sobre" não são necessários, 
#visto que é automaticamente adicionado pela vírgula de delimitação.
print("O",substantivo, adjetivo, verbo, "sobre o cachorro marrom preguiçoso")