# -*- coding: utf-8 -*-
import re


__author__ = 'kris'

# Zadanie 1

def fly(plik_A, plik_B):
    A = {}
    B = {}
    res = None
    with open(plik_A, 'r') as f:
        for line in f:
            row = line.split()
            A[row[0]] = int(row[1])
    with open(plik_B, 'r') as f:
        for line in f:
            row = line.split()
            B[row[0]] = int(row[1])
    for start in A:
        if start in B:
            if res == None or A[start]+B[start] < min:
                res = (start, A[start]+B[start])
                min = A[start]+B[start]
    return res


# Zadanie 2

# (a)

def de_rep(s):
    res = re.sub(r'\?+', '?', s)
    res = re.sub(r'\!+', '!', res)
    return res


# (b)

def price(s):
    if len(s):
        return len(re.findall(r'(\!|\.|\?)\s[A-Z0-9]', s)) + 1
    return 0


# Zadanie 3

# (a)
'''
W pierwszej linii wypisze się [[0,1], [0,1]], co jest raczej oczywiste.
W drugiej linii natomiast wypisze się [2,1], [[2,1], [2,1]], ponieważ
lista b składa się z dwóch płytkich kopii tablicy a, zatem edytując
b[0][0] zmieniamy jednocześnie listę a.
'''

# (b)
'''
Przy wywoływaniu f(f(t,b),5) najpierw obliczane jest f(t,b).
Ponieważ t jest lista, to zmiana jej w czasie działania funkcji, zmieni
też jej globalną wartość. Zatem po wywołaniu f(t,b) mamy:
t <- [2,1]
b <- 2 || b nie ulega zmianie bo jest liczba
f(t,b) <- [4, [2,1]]

Teraz obliczamy f(f(t,b), 5). Teraz pierwszym argumentem nie jest juz lista t,
zatem podczas działania tej funkcji nie zmienimy globalnej listy t! Zatem przebieg
funkcji wygląda następująco:
zmieniamy listę [4, [2,1]] na [5, [2,1]] i jako wynik funkcji zwracamy [4, t], czyli
[4, [5, [2,1]]] {to t jest inne niz to globalne !!!}

Ostatecznie otrzymany komunikat to [4, [5, [2,1]]] [2, 1] 2
'''
