# -*- coding: utf-8 -*-


def kalkulator(d, a, b):
    """
    Funkcja dająca wynik działania określonego na podanych argumentach
    :param d: działanie do wykonania
    :param a: pierwszy argument
    :param b: drugi argument
    :rtype : double/int
    """
    return eval(str(a) + d + str(b))


def double_sum(a, b):
    """
    Funkcja obliczająca: sumę liczb w sytuacji gdy są od siebie
    różne; podwojoną sumę liczb gdy są takie same
    :param a: pierwszy składnik
    :param b: drugi składnik
    :rtype : int
    """
    if a != b:
        return a + b
    return 4 * a


def sum_div_3_or_5(n):
    """
    Funkcja obliczająca sumę liczb od 0 do n [wyłącznie], podzielnych
    przez 3 lub 5.
    :param n: końcowy zakres przedziału obliczania sumy (wyłączając n)
    :rtype : int
    """
    count = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count


def fib(n):
    """
    Funkcja obliczająca n-tą liczbę Fibonacciego metodą iteracyjną.
    :param n: numer liczby Fibonacciego
    :rtype : int
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def palindrom(s):
    """
    Funkcja sprawdzająca czy dany napis jest palindromem.
    :param s: napis
    :rtype : bool
    """
    ok = True
    for i in range(len(s) / 2):
        if s[i] != s[-i - 1]:
            ok = False
    return ok