#!/usr/bin/python3
#date: 23/09/2020

#1 Write the message "Novo grenal (1-sim 2-nao)" and request a response.
#2
#3
'''#4 
3 grenais
Inter:2
Gremio:1
Empates:0
'''

switch = 1 #switch is True. 0 for False.

lista_goals = [0, 0] #lista de gols

#Internacional
inter_score = 0
inter_vitorias = 0

#Gremio
gremio_score = 0
gremio_vitorias = 0

#Empate: sem ganhador
empates = 0

#Iterador
resposta = 0 # 1 ou 2. 1=sim; 2=nao
grenais = 0


while (switch == 1):
	lista_goals = [int(x) for x in input().split(' ')]
	#print(lista_goals)

	#1: Computando o Score ANTES da solicitação de novo Grenal
	inter_score += lista_goals[0]
	gremio_score += lista_goals[1]

	#2: Computando o número de vitórias ANTES da solicitação de novo Grenal
	while lista_goals[0] > lista_goals[1]:	
		inter_vitorias += 1
		break
	while lista_goals[1] > lista_goals[0]:	
		gremio_vitorias += 1
		break
	while lista_goals[0] == lista_goals[1]:	
		empates += 1
		break

	#3: Novo grenal?
	while resposta != 2: # só cobre 1 e 2 INTEIROS.
		print("Novo grenal (1-sim 2-nao)")
		resposta = int(input())
		grenais += 1	
		break
	
	#4: Número de Grenais e vitorias de cada time
	while resposta == 2: # só cobre 1 e 2 INTEIROS.
		print("{} grenais".format(grenais))
		print("Inter:{}".format(inter_vitorias))
		print("Gremio:{}".format(gremio_vitorias))
		print("Empates:{}".format(empates))
		'''#4 
		Inter:2
		Gremio:1
		Empates:0
		'''
		#4.5: Time que venceu mais ou se não houve vencedor		
		while inter_score > gremio_score:
			print("Inter venceu mais")
			break
		while gremio_score > inter_score:
			print("Gremio venceu mais")
			break
		while inter_score == gremio_score:
			print("Não houve vencedor")
			break
		switch = 0 #Breaks the loop
		break
	

''' 
URI Online Judge | 1131
Grenais

Adapted by Neilor Tonin, URI Brazil
Timelimit: 1

The Federação Gaúcha de Futebol invited you to write a program to present a statistical result
of several GRENAIS. Write a program that read the number of goals scored by Inter and the
number of goals scored by Gremio in a GRENAL. Write the message "Novo grenal (1-sim 2-nao)"
and request a response. If the answer is 1, two new numbers must be read (another input case)
asking the number of goals scored by the teams in a new departure, otherwise the program must
be finished, printing:

- How many GRENAIS were part of the statistics.
- The number of victories of Inter.
- The number of victories of Gremio.
- The number of Draws.
- A message indicating the team that won the largest number of GRENAIS (or the message:
"Não houve vencedor" if both team won the same quantity of GRENAIS).
Input: The input contains two integer values​​, corresponding to the goals scored by both teams.
Then there is an integer (1 or 2), corresponding to the repetition of the algorithm.
Output: After each reading of the goals it must be printed the message "Novo grenal (1-sim 2-nao)".
When the program is finished, the program must print the statistics as the example below.
'''
