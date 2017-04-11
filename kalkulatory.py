def get_help():
		print("to jest prosty program kalkulatora. Wprowadz dwie liczby i zatwierdz enter")


def dodawanie(a, b):
	wynik = a + b
	return wynik
get_help()
zm1 = int(input())
zm2 = int(input())
print(dodawanie(zm1, zm2))
