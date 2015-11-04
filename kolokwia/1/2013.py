# -*- coding: utf-8 -*-

__author__ = 'kris'
# link do pdf z zadaniami
# http://regulomics.mimuw.edu.pl/wp/wp-content/uploads/2015/10/kolokwium1_2013.pdf

# Zadanie 1


def wydaj(numer, stan, przegrodki):
    """
    Funkcja zmieniająca stan automatu z produktami. Jeżeli zadanego
    produktu nie ma w automacie wypisywany jest stosowny komunikat.
    W przeciwnym przypadku aktualizowany jest stan urządzenia.
    :param numer: numer produktu
    :param stan: aktualny stan automatu
    :param przegrodki: przegrodki, w których znajdują się poszczególne
    produkty
    :return:
    """
    i = 0
    if numer >= len(przegrodki):
        print 'nie ma'
    else:
        while i < len(przegrodki[numer]) \
                and stan[przegrodki[numer][i]] == 0:
            i += 1
        if i == len(przegrodki[numer]):
            print 'nie ma'
        else:
            stan[przegrodki[numer][i]] -= 1


# Zadanie 2

def zima(l):
    """
    Funkcja zwracająca długość najdłuższego segmentu tablicy, którego
    wszystkie wartości są mniejsze od 0.
    :param l: lista liczb rzeczywistych
    :return: długość najdłuższego segmentu o elementach ujemnych
    """
    max_dl = 0
    ile = 0
    for temp in l:
        if temp < 0:
            ile += 1
        else:
            if ile > max_dl:
                max_dl = ile
            ile = 0
    if ile > max_dl:
        return ile
    else:
        return max_dl


# Zadanie 3
# (a)
def zbalansowany(l):
    """
    Sprawdza czy zadana lista jest zbalansowana.
    :param l: lista do sprawdzenia
    :return: czy lista jest zbalansowana
    """
    x = len(l)/3

    if sum(l[:x]) != sum(l[2*x:]):
        return False

    ile_zer = 0
    ile_jed = 0
    # W zadaniu wydaje mi się że jest literówka dotycząca poniższego
    # zakresu. Z takim jak jest w zadaniu otrzymujemy indeks,
    # który jest poza tablicą (dla k = 1 dostajemy indeks 3)
    for i in range(x, 2*x):
        if l[i] == 1:
            ile_jed += 1
        else:
            ile_zer += 1

    return ile_jed > ile_zer


# (b)
def dobrze_zbalansowany(l):
    """
    Funkcja sprawdzająca czy zadana lista jest dobrze zbalansowana.
    :param l: lista do sprawdzenia
    :return: czy lista jest dobrze zbalansowana
    """
    if len(l) <= 1:
        return True
    else:
        x = len(l)/3
        return zbalansowany(l) and dobrze_zbalansowany(l[:x]) \
               and dobrze_zbalansowany(l[x:2*x]) \
               and dobrze_zbalansowany(l[2*x:])
