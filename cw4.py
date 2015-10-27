# -*- coding: utf-8 -*-
import string

__author__ = 'kris'


def check_sort(v):
    """
    Rekurencyjna funkcja sprawdzająca czy lista jest posortowana rosnąco
    :param v: lista do sprawdzenia
    :return: bool
    """
    if len(v) <= 1:
        return True
    elif v[0] > v[1]:
        return False
    else:
        return check_sort(v[2:])


def rev_number(n):
    """
    Rekurencyjna funkcja odwracająca liczbę - jej wynikiem jest liczba
    o odwrotnym ustawieniu cyfr.
    :param n: liczba do odwrócenia
    :return: odwrócona liczba
    """
    if n <= 9:
        return n
    else:
        base = 1
        while (n / (base * 10)) > 0:
            base *= 10

        x = (n % 10) * base
        return rev_number(n / 10) + x


def collatz(n):
    """
    Funkcja obliczajaca wartosc funkcji Collatza dla zadanego argumentu
    :param n: argument funkcji
    :return: wynik funkcji dla argumentu
    """
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1


def collatz_steps(n):
    """
    Funkcja rekurencyjna obliczająca potrzebną liczbę kroków dla liczby
    n do otrzymania 1 w wyniku rekurencyjnych wywołań funkcji Collatza
    :param n: argument początkowy
    :return: liczba kroków do otrzymania 1
    """
    if n == 1:
        return 0
    else:
        return 1 + collatz_steps(collatz(n))


def iter_inc_segment(v):
    """
    Wersja iteracyjna funkcji zwracającej najdłuższy spójny rosnący
    segment listy
    :param v: lista elementów
    :return: najdłuższy rosnący segment
    """
    pocz = 0
    iter = 0
    maxp = 0
    maxk = 0
    while iter < len(v) - 1:
        if v[iter] > v[iter+1]:
            if (iter - pocz) > (maxk - maxp):
                maxp = pocz
                maxk = iter
            pocz = iter + 1
        iter += 1
    if ((iter - pocz) > (maxk - maxp)) and (v[-1] >= v[-2]):
        maxp = pocz
        maxk = iter
    return v[maxp:maxk+1]


def rek_inc_segment(v):
    """
    Wersja rekurencyjna funkcji zwracającej najdłuższy spójny rosnący
    segment listy
    :param v: lista elementów
    :return: najdłuższy rosnący segment
    """
    #TODO napisac tę funkcję xD



#Zadanie 5

s1 = "abcccbca" # -> "ccc"
s1 = s1.strip('a')
s1 = s1.rstrip('c')
s1 = s1.strip('b')
#print "s1 = " + s1

s2 = "bababa"
s2 = s2.lstrip('b')
s2 = s2.strip('a')
s2 = s2.lstrip('b')
#print "s2 = " + s2

#Zadanie 6

txt = "lorem ipsum dolor sit amet, consectetur Adipiscing elit . nunc sit amet ligula in nisi varius mattis nec a urna . phasellus tristique vehicula elit id imperdiet. lorem ipsum dolor sit amet , consectetur adipiscing Elit. Nunc orci libero, accumsan quis Cursus vel , pretium nec dui. Nunc lobortis mollis felis, at malesuada velit volutpat Id. Pellentesque Quis iaculis massa . vestibulum Commodo Egestas fringilla . proin quis justo nunc. Nam sed ultricies orci. curabitur adipiscing , Dolor vel rhoncus Accumsan , sapien tellus volutpat eros , At luctus mi augue sit Amet turpis . Aliquam sagittis, lacus id commodo volutpat , erat Justo auctor massa, in faucibus quam lectus et libero. curabitur laoreet Risus in urna aliquet Vel fringilla felis volutpat. morbi Suscipit purus Velit ."

print txt.replace(" ", "-") + "\n\n"

print "-".join(txt.split(" "))

#Zadanie 7

def fix_text(txt):
    """
    Funkcja poprawiająca zadany tekst, tak aby nie zawierał zbytecznych
    spacji, zdania zaczynały się wielką literą, a pozostałe słowa
    składały się wyłącznie z małych liter
    :param txt: tekst do poprawienia
    :return: poprawnie sformatowany tekst
    """
    words = txt.split()
    #Scalamy znaki przestankowe ze słowami
    for i in range(1, len(words)):
        if words[i] in string.punctuation:
            words[i-1] += words[i]
            words[i] = ""
    #Usuwamy puste słowa z listy
    for word in words:
        if word == "":
            words.remove(word)
    #Zamieniamy wszystko na małe litery
    for i in range(0, len(words)):
        if not words[i].islower():
            words[i] = words[i].lower()
    #Każde zdanie ma rozpoczynać się wielką literą
    if len(words) > 0:
        words[0] = words[0].capitalize()
    for i in range(1, len(words) - 1):
        if words[i].endswith("."):
            words[i+1] = words[i+1].capitalize()
    #Tekst ma się kończyć kropką
    if not words[-1].endswith("."):
        words[-1].append(".")

    return" ".join(words)
