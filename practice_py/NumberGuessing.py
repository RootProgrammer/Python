from random import *


def match(n):
	r = randint(1, 10)
	if n == r:
		print()
		print("Winner!")
	else:
		print()
		print("Loser!")


while True:
	print()
	n = int(input("Guess the number(0<n=>10): "))
	match(n)

	print()
	choice = input("Do you want to continue?(y/n): ")
	if (choice.lower()) == "y":
		continue
	else:
		break
