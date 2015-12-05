'''Moduł z funkcjami sortującymi'''

def bubble_sort(l):
    lc = [i for i in l]
    for i in range(len(lc)):
        for j in range(len(lc)-1-i):
            if lc[j] > lc[j+1]:
                lc[j], lc[j+1] = lc[j+1], lc[j]
    return lc

def insertion_sort(l):
    lc = [i for i in l]
    for i in range(1, len(lc)):
        j = i
        while j > 0 and lc[j] < lc[j-1]:
            lc[j], lc[j-1] = lc[j-1], lc[j]
            j -= 1
    return lc


def merge(l1,l2):
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    elif l1[0] < l2[0]:
        return [l1[0]] + merge(l1[1:],l2)
    else:
        return [l2[0]] + merge(l1,l2[1:])


def merge_sort(l):
    if len(l) <= 1:
        return l
    else:
        l1 = l[:len(l)/2]
        l2 = l[len(l)/2:]
        return merge(merge_sort(l1),merge_sort(l2))