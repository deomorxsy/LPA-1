#!/usr/bin/python3

filo = input()
classe = input()
dieta = input()

if filo == "vertebrado":
	if classe == "ave":
		if dieta == "carnivoro":
			print("aguia")
		elif dieta =="onivoro":
			print("pomba")
	elif classe == "mamifero":
		if dieta == "onivoro":
			print("homem")
		elif dieta == "herbivoro":
			print("vaca")

elif filo == "invertebrado":
	if classe == "inseto":
		if dieta == "hematofago":
			print("pulga")
		if dieta == "herbivoro":
			print("lagarta")
	if classe == "anelideo":
		if dieta == "hematofago":
			print("sanguessuga")
		if dieta == "onivoro":
			print("minhoca")