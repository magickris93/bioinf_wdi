# -*- coding: utf-8 -*-
import re


__author__ = 'kris'

# Zadanie 1

# (a)

def cena(p, m):
    with open('ceny.tlinet', 'r') as f:
        for line in f:
            row = line.split()
            if row[0] == p and row[1] == m:
                return int(row[2])
    return -1


# (b)

def koszyk(k):
    d = {}
    with open('ceny.tlinet', 'r') as f:
        for line in f:
            row = line.split()
            if row[1] not in d:
                d[row[1]] = {}
            d[row[1]][row[0]] = int(row[2])

    minimum = -1
    min_miasto = ""

    for miasto in d:
        ile = 0
        for e in k:
            if e in d[miasto]:
                ile += d[miasto][e]
            else:
                ile = -1
                break
        if (ile != -1 and minimum == -1) or (ile < minimum):
            minimum = ile
            min_miasto = miasto
    return min_miasto


# Zadanie 2


def perm(plik):
    permutacja = []
    wyrazy = []
    with open(plik, 'r') as f:
        for line in f:
            row = line.split()
            permutacja.append(int(row[0])-1)
            wyrazy.append(row[1])

    aktualny = 0
    for i in range(len(permutacja)):
        print wyrazy[aktualny],
        aktualny = permutacja[aktualny]


# Zadanie 3


def suma(plik):
    first = '2012'
    second = '2013'
    suma = 0

    with open(plik, 'r') as f:
        for line in f:
            s = re.search(first, line)
            kon = re.search(second, line)
            if s != None and kon != None and kon.start() > s.end(): 
                suma += int(line[s.end():kon.start()])
    return suma
