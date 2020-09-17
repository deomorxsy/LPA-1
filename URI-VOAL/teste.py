#!/usr/bin/python3
segundos=int(input())
h =segundos//3600
segundos =segundos%3600
minutos =segundos//60
segundos =segundos%60
print("%d:%d:%d", % h, minutos, segundos)
