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


def glosowanie(wyniki):
    """
    Funkcja sprawdzająca czy w liście o długości N znajduje się taka,
    która występuje w niej więcej niż N/2 razy
    :param wyniki: lista liczb
    :rtype : int
    """
    if len(wyniki) == 0:
        return None
    else:
        k = wyniki[0]
        ile = 1
        for i in range(1, len(wyniki)):
            if wyniki[i] == k:
                ile += 1
            elif ile > 0:
                ile -= 1
            else:
                k = wyniki[i]
                ile = 1
        #Jeżeli na liście jest liczba występująca ponad N/2 razy
        #to jej liczba wystąpień przewyższy liczbę innych liczb.
        if ile > (len(wyniki) / 2):
            return k
        elif wyniki.count(k) > (len(wyniki) / 2):
            return k
        else:
            return None
