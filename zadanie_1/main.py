def read_reads(plik):
    with open(plik, 'r') as f:
        lines = [line.rstrip('\n').split() for line in f]
    return lines

def compute_coverage(odczyty):
    c = {}
    for row in odczyty:
        ci = int(row[0])
        if ci not in c:
            c[ci] = []
        begin = int(row[1])
        length = int(row[2])
        for i in range(begin+length-len(c[ci])):
            c[ci].append(0)
        for i in range(begin, begin+length):
            c[ci][i] += 1
    return c

def write_coverage(pokrycie, plik_wyjsciowy):
    with open(plik_wyjsciowy, 'w') as f:
        for c in pokrycie:
            i = 1
            begin = 0
            length = 0
            while i < len(pokrycie[c]):
                if pokrycie[c][i-1] == pokrycie[c][i]:
                    length += 1
                else:
                    if pokrycie[c][i-1] != 0:
                        f.write("{0}\t{1}\t{2}\t{3}\n".format(pokrycie[c][i-1],
                                                    c, begin, length+begin+1))
                    begin = i
                    length = 0
                i += 1
            f.write("{0}\t{1}\t{2}\t{3}\n".format(pokrycie[c][i-1],
                                        c, begin, length+begin+1))

def multiply_coverage(plikA, plikB, plik_wyjsciowy):
    c1 = compute_coverage(read_reads(plikA))
    c2 = compute_coverage(read_reads(plikB))
    c_res = {}
    for key in sorted(c1.keys()):
        res = []
        for i in range(min(len(c1[key]), len(c2[key]))):
            res.append(c1[key][i] * c2[key][i])
        c_res[key] = res[:]
    write_coverage(c_res, plik_wyjsciowy)