# -*- coding: utf-8 -*-
__author__ = 'kris'
import re


# Zadanie 1

# (a)

'''
Wewnątrz funkcji używamy globalnej zmiennej y, także jej wartość ulegnie
zmianie po działaniu funkcji f. W wyniku wywołania f(y) otrzymamy 84 (2 * y),
natomiast y = 4 * y[wyjsciowy], zatem ostatecznie wypisze się 84 168.
'''


# (b)

'''
Wewnątrz funkcji g używana jest globalna zmienna m, zatem będzie ona ulegać
zmianie. Podczas pierwszego obrotu m stanie się [2,2,3], natomiast l będzie
postaci [7,m,9], przy czym m jest płytką kopią listy. Wynikiem będzie zatem
[7,m,9] + g([7,m]).

W drugim wywołaniu funkcji g znowu pierwszy element listy m zwiększony zostanie
o jeden, przez co m <- [3,2,3]. l nie ulegnie zmianie, bo miało już na drugim
miejscu płytką kopię m. W wyniku dostaniemy [7,m] + g([7]).

g([7]) = [7]

Zatem ostatecznie otrzymamy [7,m,9] + [7,m] + [7], czyli [7,m,9,7,m,7].
Wstawiając listę m do listy wynikowej wypisze się ostatecznie:
[7, [3, 2, 3], 9, 7, [3, 2, 3], 7] [3, 2, 3]
'''

# Zadanie 2

def adresy(tekst):
    name_re = r'([A-Z][a-z]*)[-]?[ ]?([A-Z][a-z]*-)?'
    nr_re = r'([(][+]\d{2}[)]-)?(\d{3}-\d{3}-\d{3}|\d{2}-\d{3}-\d{2}-\d{2})'
    mail_re = r'([a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z0-9._]+)'

    numery = []
    maile = []

    for match in re.finditer(name_re+nr_re, tekst):
        if match.group(3) is not None:
            numery.append((match.group(1), match.group(3)+match.group(4)))
        else:
            numery.append((match.group(1), '(+48)-'+match.group(4)))

    for match in re.finditer(name_re+mail_re, tekst):
        maile.append((match.group(1), match.group(3)))

    print numery
    print maile


# Zadanie 3






