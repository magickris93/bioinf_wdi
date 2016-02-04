#!/usr/bin/python

# Rozwiazania zadan z egzaminu 2012

# Zadanie 1
import re
import sys

with open(sys.argv[1], 'r') as f:
    data = f.read()

sum = 0
regexp = r'(\d+)' + sys.argv[2] + r'\b'
for line in data.split('\n'):
    for num in re.finditer(regexp, line):
        sum += int(num.group(1))
print sum

# Zadanie 2
# sort -t\: -k +4n pracownicy | tail -n +5 | head -n +1 | awk -F ":" '{print $1 " " $2}'
# sort -t\: -k +4n pracownicy <= rozdziel kolumny na podstawie znaku ":", posortuj numerycznie po 4 kolumnie
# tail -n +5 <= wypisz jedynie linie poczawszy od 5-tej
# head -n +1 <= wypisz tylko pierwsza linie
# awk -F ":" '{print $1 " " $2}' <= Podziel linie wzgledem znaku ":" i wypisz pierwsza kolumne, spacje i druga kolumne


# Zadanie 3
# a)'a a bc' | sed 's/\([a-z]\+\) \1 \([a-z]\+\)/\2 \1/'
# bc a

# ???

# b) echo out1 || echo out2
# out1

# || oznacza alternatywe. Poniewaz warunki wyliczane sa leniwie (nie sa wyliczane nastepne wartosciowania 
# zdan logicznych, gdy wartosc calego zdania jest juz znana) i echo out1 konczy dzialanie z kodem bledu 0 (brak bledu), 
# to nastepny fragment alternatywy juz sie nie wykona, dlatego tez na ekranie ujrzymy tylko out1

# c) echo out >> test
# <nic>

# Na ekran nie wypisze sie nic, bo echo out >> test oznacza po prostu dopisanie do pliku test napisu out.
# W przypadku gdy plik nie istnieje, to plik ten zostanie utworzony.


# Zadanie 4

def alter_sum(l):
	res = []
	for i in range(max(l)+1):
		res.append(0)
	for i in range(len(l)):
		if i % 2 == 0:
			res[l[i]] += 1
		else:
			res[l[i]] -= 1
	print res

# Zadanie 5

def fruits(kraj, plik):
	kraje = {} # kraj : lista klimatow
	owoce = {} # klimat : lista owocow
	with open(plik, 'r') as f:
		# kraj klimat owoc
		data = f.readlines()
	for row in data:
		line = row.split()
		if line[0] not in kraje:
			kraje[line[0]] = [line[1]]
		else:
			kraje[line[0]].append(line[1])

		if line[1] not in owoce:
			owoce[line[1]] = [line[2]]
		else:
			owoce[line[1]].append(line[2])
	res = []
	if kraj in kraje:
		for klimat in kraje[kraj]:
			res.extend(owoce[klimat])
	return res

# Zadanie 6

def flatten(l):
	if type(l) == int:
		return [l]
	else:
		res = []
		for x in l:
			res += elements(x)
		return res