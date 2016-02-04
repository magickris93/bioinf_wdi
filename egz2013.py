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


# Zadanie 4

def wczytaj(plikA, plikB, plikC):
	miasto = {}
	targ = {}
	miary = {}

	with open(plikA, 'r') as f:
		data = f.readlines()
	for line in data:
		row = split.data()
		miasto[row[0]] = (row[1], int(row[2]))

	with open(plikB, 'r') as f:
		data = f.readlines()
	for line in data:
		row = split.data()
		targ[row[0]] = (row[1], int(row[2]))

	with open(plikB, 'r') as f:
		data = f.readlines()
	for line in data:
		row = split.data()
		miary[row[0]] = (row[1], int(row[2]))

	return miasto, targ, miary


def dobre_zakupy(skup, sprzedaz):
	res = []
	for k in skup:
		if k in sprzedaz:
			if (sprzedaz[0] == sprzedaz[1]) and (sprzedaz[k][1] > skup[k][1]):
				res.append(k)
	return res


def najlepszy_zakup(skup, sprzedaz, jednostki):
	best_buy = None
	best_val = 0
	for towar in skup:
		# licze cene w zlotowkach na jednostke podstawowa
		if skup[towar][0] in jednostki:
			val1 = float(skup[towar][1] / jednostki[skup[towar][0]])
		else:
			val1 = float(skup[towar][1])

		if sprzedaz[towar][0] in jednostki:
			val2 = float(sprzedaz[towar][1] / jednostki[sprzedaz[towar][0]])
		else:
			val2 = float(sprzedaz[towar][1])

		# im lepszy stosunek val1 do val2 tym wiekszy zysk
		val = val1 / val2

		if best_buy == None:
			best_buy = towar
			best_val = val
		elif val > best_val:
			best_buy = towar
			best_val = val


# Zadanie 5

# (a)
def styl(tekst):
	reg_word = r'(\b|[!?.,-])[A-Za-z]+(\b|[!?.,-])'
	words = re.findall(reg_word, tekst)
	count = {}
	res = []
	for w in words:
		if w in count:
			count[w] += 1
		else:
			count[w] = 1
	for i in range(20):
		max_v = 0
		max_k = None
		for word in sorted(count):
			if count[word] > max_v:
				max_k = word
		res.append(max_k)
		del count[max_k]
	return res


# (b)
def plagiat(tekst1, tekst2):
	styl1 = styl(tekst1)
	styl2 = styl(tekst2)
	# zbior1 & zbior2 <- przeciecie zbiorow
	return len(set(styl1)&set(tekst2))


# Zadanie 6

# (a)
# cat kierowcy | sort -k +3n | tail -5 | awk -F " " '{print $1 " " $3}'

# (b)
# cat kierowcy | sort -k +4n | head -5 | awk -F " " '{print $1 " " $3}'

# (c)
# cat kierowcy | awk -F " " '{print $3 - $2 " " $4}' | sort -k +1n -r | uniq