#!/usr/bin/python3
#INCOMPLETO

menor = a if a < b and b < c else (b if b < c else c)
maior = a if a > b and b > c else (b if b > c else c)

print(menor)
print(a if a != maior and a != menor else (b if b != maior and b))