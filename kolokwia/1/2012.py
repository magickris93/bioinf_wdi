# -*- coding: utf-8 -*-

__author__ = 'kris'

# link do pdf z zadaniami
# http://regulomics.mimuw.edu.pl/wp/wp-content/uploads/2015/10/kolokwium1_2012.pdf

# Zadanie 1

# (a)
def sumy(l):
    """
    Funkcja zwracająca listę sum poszczególnych segmentów listy, to jest
    fragmentów oddzielonych końcami listy, bądź zerami.
    :param l: lista liczb
    :return: lista sum segementów listy
    """
    wynik = []
    suma = 0
    ile = 0
    for x in l:
        if x != 0:
            suma += x
            ile += 1
        else:
            if ile > 0:
                wynik.append(suma)
                suma = 0
                ile = 0
    return wynik


# (b)
def suma_sum(l):
    """
    Funkcja rekurencyjna licząca sumę elementów listy
    :param l: lista liczb
    :return: suma liczb z listy
    """
    if len(l) == 0:
        return 0
    else:
        return l[0] + suma_sum(l[1:])


# Zadanie 2

def a_i(n):
    """
    Funkcja iteracyjna obliczająca wartość a_r(n).
    :param n: indeks funkcji
    :return: wynik funkcji rekurencyjnej
    """
    a = []
    b = []
    for i in range(n):
        a.append(0)
        b.append(0)

    a[n-1] = 1
    i = n-1
    wynik = 0
    while i > 0:
        a[i-1] += a[i]
        b[i] += a[i]
        wynik += a[i]

        a[i-1] += b[i]
        b[i-1] += b[i]
        wynik += b[i]*2

        i -= 1

    wynik += a[0] + b[0]
    return wynik


# Zadanie 3

def dekoduj(l):
    """
    Funkcja odszyfrowywujaca zadaną permutację.
    :param l: Lista indeksów permutacji
    :return: Permutacja określona przez parametr funkcji
    """
    wynik = []
    temp = range(len(l))
    for x in l:
        wynik.append(temp[x])
        del temp[x]
    return wynik