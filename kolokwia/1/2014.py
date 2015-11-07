# -*- coding: utf-8 -*-

__author__ = 'kris'
# link do pdf z zadaniami
# http://regulomics.mimuw.edu.pl/wp/wp-content/uploads/2015/10/kolokwium1_2014.pdf

# Zadanie 1


def wyniki_kraju(lista, numer):
    miejsca = []
    for protokol in lista:
        i = 0
        znal = False
        while i < len(protokol) and not znal:
            if protokol[i] != numer:
                i += 1
            else:
                miejsca.append(i)
                znal = True
        if i == len(protokol):
            miejsca.append(-1)
    return miejsca


def tabela_medalowa(lista, m):
    ile = 0
    for e in lista:
        if max(e) > ile:
            ile = max(e)

    l = []
    miejsca = []

    for i in range(m+1):
        l.append(0)

    for i in range(ile):
        miejsca.append(l[:])

    for i in range(len(lista)):
        for j in range(min(len(lista[i]), m)):
            miejsca[j][lista[i][j]] += 1
    return miejsca


def gory_i_doliny(l):
    gid = []
    if len(l) > 0:
        s = l[0]
        for i in range(1, len(l)-1):
            if (l[i] > 0) and (l[i+1] < 0) and (s + l[i] > 0):
                gid.append(i)
            elif (l[i] < 0) and (l[i+1] > 0) and (s + l[i] < 0):
                gid.append(i)
            s += l[i]
    return gid


def kolor(r, i, j):
    if r == 1:
        return 'czarny'
    elif r == 2:
        if i == 1 and j == 1:
            return 'bialy'
        return 'czarny'
    else:
        x = 3 ** (r - 2)
        if (i >= x) and (i < 2 * x) and (j >= x) and (j < 2 * x):
            return 'bialy'
        else:
            return kolor(r - 1, i % x, j % x)
