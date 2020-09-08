#!usr/bin/env python3
# 08/09/2020 SET

'''
3. Modifique o exercício anterior para que um nome de 
animal seja lido e escrito no local adequado.
'''

substantivo = input("Digite um substantivo: ") #Sem quebra de linha pra ficar mais legível na execução
adjetivo = input("Digite um adjetivo:")
verbo = input("Digite um verbo: ")
animal = input("Digite um animal: ")

#Abaixo o espaço após o "O" e antes de "sobre" não são necessários, 
#visto que é automaticamente adicionado pela vírgula de delimitação.
print("O",substantivo, adjetivo, verbo, "sobre o", animal, "marrom preguiçoso")