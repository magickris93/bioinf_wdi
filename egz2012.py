#!/usr/bin/python

#rozwiazania zadan z egzaminu 2012

#Zadanie 1
import re
import sys

with open(sys.argv[1], 'r') as f:
    data = f.read()

sum = 0
regexp = r'(\d+)' + sys.argv[2] + r'\b'
for line in data.split('\n'):
    print line
    for num in re.finditer(regexp, line):
        sum += int(num.group(1))
print sum


#Zadanie 2
# sort -t\: -k +4n pracownicy | tail -n +5 | head -n +1 | awk -F ":" '{print $1 " " $2}'
# sort -t\: -k +4n pracownicy <= rozdziel kolumny na podstawie znaku ":", posortuj numerycznie po 4 kolumnie
# tail -n +5 <= wypisz jedynie linie poczawszy od 5-tej
# head -n +1 <= wypisz tylko pierwsza linie
# awk -F ":" '{print $1 " " $2}' <= Podziel linie wzgledem znaku ":" i wypisz pierwsza kolumne, spacje i druga kolumne
