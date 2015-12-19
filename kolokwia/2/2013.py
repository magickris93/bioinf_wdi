# -*- coding: utf-8 -*-
import re


__author__ = 'kris'

# Zadanie 1

# (a)

def zadzwonic(f_numery, f_rozmowy):
    d = {}

    with open(f_numery, 'r') as f:
        for line in f:
            d[line.replace('\n', '')] = []
    with open(f_rozmowy, 'r') as f:
        for line in f:
            row = line.split()
            if row[1] not in d:
                d[row[1]] = []
            d[row[1]].append((row[0], row[2]))

    niedodzwonione = []
    for numer in d:
        ok = True
        for e in d[numer]:
            if e[1] != '0':
                ok = False
                break
        if ok:
            niedodzwonione.append(numer)

    return niedodzwonione


# (b)

def bledy(f_numery, f_rozmowy):
    d = {}
    baza = []

    with open(f_numery, 'r') as f:
        for line in f:
            baza.append(line.replace('\n', ''))
    with open(f_rozmowy, 'r') as f:
        for line in f:
            row = line.split()
            if row[1] not in d:
                d[row[1]] = []
            d[row[1]].append((row[0], row[2]))

    pomylki = set([])
    for numer in d:
        ok = True
        for e in d[numer]:
            if numer not in baza:
                pomylki.add(e[0])
            elif e[1] != '0':
                if ok:
                    ok = False
                else:
                    pomylki.add(e[0])

    return list(pomylki)

# Zadanie 2

# (a)

def kazde(l):
    osoby = set([])
    for lista in l:
        for element in lista:
            osoby.add(element)
    res = []
    for osoba in osoby:
        ok = True
        for lista in l:
            if osoba not in lista:
                ok = False
                break
        if ok:
            res.append(osoba)
    return res


# (b)

def najczesciej(l, u):
    osoby = set([])
    for lista in l:
        for element in lista:
            osoby.add(element)
    obecnosci = {}
    for osoba in osoby:
        obecnosci[osoba] = 0
    for lista in l:
        for osoba in lista:
            obecnosci[osoba] += 1

    max_ob = obecnosci[u[0]]
    max_os = u[0]

    for osoba in u:
        if obecnosci[osoba] > max_os:
            max_ob = obecnosci[osoba]
            max_os = osoba

    return max_os


# Zadanie 3

# (a)

'''
No tutaj po prostu trzeba przesledzic kolejne kroki i wychodzi ostatecznie [22].
'''

# (b)

'''
Poniewaz lista [2] jest jednoelementowa, to wchodzimy do else'a.
Na poczatku do l dodajemy v + l[0] czyli 2 + 2, czyli 4. l <- [2, 4]
Teraz ustawiamy v na 2 + 2, czyli 4. l[0] = v czyli l <- [4, 4] i to
jest ostateczny wynik.
'''
