#!/bin/bash

import re
import sys

# Zadanie 1

# (a)

# python

def avg():
	with open(sys.argv[1], 'r') as f:
		data = f.readlines()
	pensje = []
	for line in data:
		row = line.split(',')
		pensje.append(int(row[3]))

	return sum(sorted(pensje)[-int(sys.argv[2]):])/int(sys.argv[2])


# bash

'''
count=0
suma=0

for i in `cut -d',' -f4 $1 | sort -rn | head -$2`
do
	suma=$(( $suma + $i ))
	count=$(( $count + 1 ))
done
echo $(( $suma / $count ))
'''

# (b)

# python

def top_k():
	data = f.readlines()
	d = {}
	for line in data:
		row = line.rstrip('\n').split(',')
		if row[5] == sys.argv[2]:
			d[int(row[3])] = row[0]+ " " +row[1]
	x = sorted(d.keys())
	x.reverse()
	return d[x[int(sys.argv[3])-1]]

# bash

# echo `sort -t',' -k +4rn $1 | head -$2 | tail -1 | awk -F "," '{print $1 " " $2}'`


# (c)

# python
def zawod_staz():
	with open(sys.argv[1], 'r') as f:
		data = f.readlines()
		for line in data:
			row = line.rstrip('\n').split(',')
			if row[5] == sys.argv[2] and row[2] == sys.argv[3]:
				print row[0] + " " + row[1] + " " + str(int(row[3])*int(row[4]))


#bash

# zakladam, ze nie ma wojewodztw o takich samych nazwach jak zawody
# grep $2 $1 | grep $3 | awk -F "," '{print $1 " " $2 " " $4*$5}'

# Zadanie 2

# (a)

'''
import re
regexp = r'<.*?>'
html = '<egzamin>2015</egzamin>'
html += '<pktocena>SUM<60 => 2 </pktocena>'
print re.findall(regexp, html)
'''

# na ekran wypisze sie [<egzamin>, </egzamin>, <pktocena>, <60 =>, </pktocena>] poniewaz szukane wyrazenie regularne
# pasuje do kazdego napisu zamknietego w nawiasach <>.

# (b)

'''
echo 'plik:a.txt' > a.txt
cat a.txt | sed 's/plik/tresc/g' >> a.txt
cat a.txt | echo 'To byla tresc a.txt'
'''

# rzeczywiscie do pliku a.txt zostanie dopisana linia tresc:a.txt, natomiast nie generuje ono zadnego napisu, zatem jedyne
# co bedzie wypisane to napis 'To byla tresc a.txt'

# (c)

'''
echo 'linia 1' > a.txt
echo 'linia 2' >> a.txt
echo 'linia 3' > a.txt
echo 'linia 4' >> a.txt
cat a.txt | cut -d ' ' -f2 | sort -r
'''

# polecenie > nadpisuje stary plik, natomiast >> dopisuje na jego koniec. Zatem po pierwszych 4. poleceniach plik a
# ma postac:
# linia 3
# linia 4
# nastepnie bierzemy tylko druga kolumne z tego pliku i sortujemy ja w kolejnosci odwrotnej niz zwykla, czyli malejacej
# czyli w efekcie otrzymamy na ekranie
# 4
# 3

