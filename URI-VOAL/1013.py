#!/usr/bin/python3
#date: 28/09/2020
def main():
	a, b, c = [int(i) for i in input().split(' ')]

	if a < b or a < c:
		if c > b:
			return print("{} eh o maior".format(c))
		if b > c:
			return print("{} eh o maior".format(b))
	else:
		return print("{} eh o maior".format(a))

if __name__ == '__main__':
	main()