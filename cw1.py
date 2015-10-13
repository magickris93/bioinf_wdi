# -*- coding: utf-8 -*-


def parsum(l):
    '''
    Funkcja licząca sumę parzystych elementów listy.
    Zakładam, że A jest listą.
    @return : suma parzystych elementów listy
    '''
    count = 0
    for element in l:
        if element % 2 == 0:
            count += element
    return count


def pierwiastki(a, b, c):
    '''
    Funkcja wypisuje na wyjście standardowe wartości pierwiastków
    trójmianu kwadratowego o współczynnikach a, b, c
    tj. trójmianu postaci ax^2 + bx + c, gdzie a,b,c są liczbami
    rzeczywistymi i a jest różne od 0.
    '''
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print "Brak pierwiastków rzeczywistych."
    elif delta == 0:
        x = -b / (2 * a)
        print "Jeden pierwiastek rzeczywisty podwójny " + str(x) + "."
    else:
        x1 = (delta ** 0.5 - b) / (2 * a)
        x2 = (-(delta ** 0.5) - b) / (2 * a)
        print "Dwa pierwiastki rzeczywiste " + str(x1) + \
              " oraz " + str(x2)


print "parsum(0-10) = " + str(parsum(range(11)))
print "parsum(0-50) = " + str(parsum(range(51)))
print "parsum(0-100) = " + str(parsum(range(101)))

pierwiastki(1, 2, 1)
pierwiastki(1, -2, 1)
pierwiastki(1, -1, -2)
pierwiastki(100, 100, 100)