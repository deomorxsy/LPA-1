#!/usr/bin/python3

age = int(input())#in days

tempo = []
for i in range(1):
	tempo.append(age // 365)
	tempo.append((age % 365) // 30)
	tempo.append((age % 365) % 30)

#[print(tempo[i], end=':') if (i != len(tempo)-1) else print(tempo[i]) for i in range(len(tempo))]

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(tempo[0],tempo[1],tempo[2]))