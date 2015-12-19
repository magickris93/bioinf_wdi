# -*- coding: utf-8 -*-
import re


__author__ = 'kris'


# Zadanie 1


def is_loop2(filename):
	moves = {}
	with open(filename, 'r') as f:
		for line in f:
			row = map(int, line.split())
			first = (row[0], row[1])
			second = (row[2], row[3])
			if first not in moves:
				moves[first] = [second]
			else:
				moves[first].append(second)

	for move in moves:
		for m in moves[move]:
			if move in moves[m]:
				return True
	return False


# Zadanie 2

# (a)

'''
Słownik d wewnątrz funkcji add nie jest związany niczym ze słownikiem d istniejącym
na zewnątrz funkcji, zatem to wywołanie funkcji da wynik 15 (6 + 9), a d nie ulegnie
żadnej zmianie tj. pozostanie d = {'a' : 3}.
'''

# (b)

'''
Tym razem słownik d będzie ulegał zmianie, gdyż poprzedzono go wewnątrz funkcji słowem
kluczowym global. Podczas pierwszego wywołania dodajemy nowy klucz - 'la' i jego wartością
staje się płytka kopia wartości spod klucza 'li'. Następnie modyfikujemy listę spod la poprzez
dodanie do jej zerowego elementu 1. Ponieważ jest to płytka kopia to zmiana nastąpi również w drugiej
liście przez co wynikiem pierwszego wywołania jest : d = {'la' : [2,2,3], 'li' : [2,2,3]}.

Drugie wywołanie wygląda podobnie. Pod wartosc w kluczu 'li' wstawiamy listę li, więc nic sie nie zmienia.
Następnie dodajemy do jej drugiego elementu 2. Co zmienia nam listę na [2, 4, 3]. Pamiętając, że pod 'la'
jest kopia listy 'li', ostatecznie otrzymujemy : d = {'la' : [2,4,3], 'li' : [2,4,3]}.
'''

# (c)

'''
Ponieważ listy są obiektami mutowalnymi, to ulegają zmianie poprzez działanie na nich funkcjami.
Niemniej listy lu nie zmieniamy w żaden sposób ponieważ wewnątrz funkcji liextend używamy głębokiej kopii,
(używamy li[:-1], czyli kopii bez ostatniego elementu). W przeciwieństwie do poprzednich przykładów jest to
zupełnie odrębna lista, czyli w efekcie wypisze się napis [1, 2, 3, -3, -2, -1, -3, -2, -3] [-3, -2, -1].
'''

# Zadanie 3

# Prawdopodobnie da się to zrobić mądrzej XD

def sekwencje(plik):
	reg = r'[A]{5,}[GCT]|[T]{5,}[GCA]|[G]{5,}[ATC]|[C]{5,}[ATG]'
	with open(plik, 'r') as f:
		for line in f:
			matches = re.findall(reg, line)
			for i in range(len(matches)):
				for k in range(i+1, len(matches)):
					if (matches[k][0] == 'T' and matches[i][0] == 'A') \
					or (matches[k][0] == 'A' and matches[i][0] == 'T') \
					or (matches[k][0] == 'G' and matches[i][0] == 'C') \
					or (matches[k][0] == 'C' and matches[i][0] == 'G'):
						if len(matches[k]) > len(matches[i])*2-2:
							print line, #na koncu linii jest zbedny \n
							break

