def read_reads(plik):
    with open(plik, 'r') as f:
        lines = [line.rstrip('\n').split() for line in f]
    return lines


def compute_coverage(odczyty):
    c = {}
    for row in odczyty:
        ci = int(row[0])
        if int(row[0]) not in c:
            c[ci] = []
        begin = int(row[1])
        length = int(row[2])
        for i in range(length-begin+2-len(c[ci])):
            c[ci].append(0)
        for i in range(begin, length+1):
            c[ci][i] += 1
    return c


def write_coverage(pokrycie, plik_wyjsciowy):
    with open(plik_wyjsciowy, 'w') as f:
        for c in pokrycie:
            i = 1
            begin = 0
            length = 0
            while i < len(pokrycie[c]):
                if pokrycie[c][i-1] != pokrycie[c][i]:
                    if pokrycie[c][i-1] != 0:
                        f.write("{0}\t{1}\t{2}\t{3}\n".format(pokrycie[c][i-1],
                        c, begin, length+begin+1))
                    begin = i
                    length = 0
                else:
                    length += 1
                i += 1
        if pokrycie[c][i-1] != 0:
            f.write("{0}\t{1}\t{2}\t{3}\n".format(pokrycie[c][i-1],
            c, begin, length+begin+1))

def multiply_coverage(plikA, plikB, plik_wyjsciowy):
    return None

# print compute_coverage(read_reads('odczytyA.sdx'))
write_coverage(compute_coverage(read_reads('odczytyA.sdx')), 'wynikiheheh')