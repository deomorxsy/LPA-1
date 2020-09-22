x = 3 #int(input())
y = 99 #int(input())

for c in range(y):
	while (c < y):
		print(c + 1, end = "")
		break
	while (not((c + 1) % x == 0)):
		print(" ", end="")
		break
	while ((c + 1) % x == 0):
		print("")
		break