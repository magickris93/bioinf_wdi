# -*- coding: utf-8 -*-

__author__ = 'kris'
# link do pdf z zadaniami
# http://regulomics.mimuw.edu.pl/wp/wp-content/uploads/2015/10/kolokwium1popr_2012.pdf

# Zadanie 1


def cena(lista, kody, cennik):
    """
    Funkcja obliczająca sumę należną za zakupione towary na podstawie
    listy kodów i odpowiedającym im cenom.
    :param lista: lista towarów
    :param kody: lista kodów towarów
    :param cennik: lista cen poszczególnych towarów
    :return: należność za towary
    """
    suma = 0
    for towar in lista:
        i = 0
        while (i < len(kody)) and (kody[i][0] != towar):
            i += 1
        if i < len(kody):
            suma += cennik[kody[i][1]]
    return suma


# Zadanie 2

def is_quasindrom(l):
    """
    Funkcja sprawdzająca czy zadana liczba jest quasindromem, to znaczy
    liczby reprezentowane przez cyfry równo oddalone od obu końców
    liczby określonej przez listę będącą parametrem różnią się o co
    najwyżej jeden.
    :param l: liczba jako lista cyfr
    :return: czy liczba jest quasindromem
    """
    if len(l) <= 1:
        return True
    elif abs(l[0] - l[-1]) > 1:
        return False
    else:
        return is_quasindrom(l[1:-1])


# Zadanie 3

def is_hyperquasindrom(l):
    """
    Funkcja sprawdzająca czy zadana liczba jest hiperquasindromem.
    :param l: liczba jako lista cyfr
    :return: czy liczba jest hiperquasindromem
    """
    if len(l) <= 1:
        return True
    else:
        return is_quasindrom(l) and is_hyperquasindrom(l[:len(l)/2]) \
               and is_hyperquasindrom(l[len(l)/2:])
