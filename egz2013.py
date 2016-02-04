#!/bin/bash

# Zadanie 1

def dobry(s):
	if len(s) % 2 == 0:
		return set(s[:len(s)/2]) == set(s[len(s)/2:])
	else:
		return set(s[:len(s)/2]) == set(s[len(s)/2+1:])

def bardzo_dobry(s):
	if len(s) <= 1:
		return True
	else:
		if len(s) % 2 == 0:
			return dobry(s) and bardzo_dobry(s[:len(s)/2]) and bardzo_dobry(s[len(s)/2:])
		else:
			return dobry(s) and bardzo_dobry(s[:len(s)/2]) and bardzo_dobry(s[len(s)/2+1:])

# Zadanie 2

# (a)
def stan(historia):
	with open(historia, 'r') as f:
		data = f.readlines()
	if data != []:
		res = []
		for i in range(len(data[0].split())):
			res.append(0)
	for line in data:
		row = line.split()
		for i in range(len(row)):
			res[i] += int(row[i])
	print res

# (b)
def czy_ok(historia):
	with open(historia, 'r') as f:
		data = f.readlines()
	if data != []:
		res = []
		for i in range(len(data[0].split())):
			res.append(0)
	for line in data:
		row = line.split()
		for i in range(len(row)):
			res[i] += int(row[i])
		for v in res:
			if v < 0:
				return False
	return True


# Zadanie 3

# (a)

# boo="abc bac cab"
# for i in 'echo $boo | sed s/[bc]a/cc/g'
# do
#	 echo "$i\n" > baz.txt
# done
# cat baz.txt | grep cc

# Jezeli wszystkie cudzyslowy maja byc tak jak w pdf to wypisze sie: echo $boo | sed s/[bc]a/cc/g\n
# ' ' nie wywoluje polecenia znajdujacego sie miedzy apostrofami(robi to ` `), a jedynie podstawia
# zmienne ($i), przy czym przy iteracji, poruszamy sie po liniach tekstu, a mamy tutaj tylko jedna linie
# dodatkowo > baz.txt nadpisuje plik baz za kazdym razem.
# gdyby chodzilo o to zeby echo $boo | sed s/[bc]a/cc/g sie wywolalo to kazdy napis ktory spelnia warunki
# wyrazenia regularnego : [bc]a zostanie zamieniony na napis cc, czyli abc -> abc, bac -> ccc, cab -> ccb
# i w pliku baz.txt bedzie tylko ccb!

# (b)

'''
a = range(10)
b = a + range(5)
c = a
a.reverse()
d = sorted(a)
print b[0], b[-1], a==c, a==d
'''

# 0 4 True False

# wszystkie kopie list sa plytkie. Dodawanie list tworzy nowa liste, czyli b jest niezalezne od zmiany a
# b = [0..9, 0..4]
# c jest plytka kopia a wiec c==a
# a.reverse() odwraca liste a tzn a[i] -> a[-i]
# d jest lista zlozona z wartosci z listy a w kolejnosci rosnacej, czyli [0..9]

