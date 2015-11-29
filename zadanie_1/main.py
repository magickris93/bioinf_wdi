__author__ = "Krzysztof Nagrodkiewicz"

def read_reads(in_file):
    """
    Returns list of lines from file

    Args:
        in_file (str): name of input file
    Returns:
        list of lines, each split by whitespace characters
    """
    with open(in_file, 'r') as f:
        lines = [line.rstrip('\n').split() for line in f]
    return lines


def compute_coverage(reads):
    """
    Returns coverage based on a read in format:
    no. of chromosome   coordinate  length of read

    Args:
        reads (list): list of lines representing a single read
    Returns:
        dictionary representing reads mapped on chromosomes
    """
    c = {}
    for row in reads:
        ci = int(row[0])
        if ci not in c:
            c[ci] = []
        begin = int(row[1])
        length = int(row[2])
        for i in range(begin+length-len(c[ci])):
            c[ci].append(0)     # expand list if necessary
        for i in range(begin, begin+length):
            c[ci][i] += 1
    return c


def write_coverage(coverage, out_file):
    """
    Writes coverage to a file in following format:
    no. of reads    no. of chromosome   first coordinate    second coordinate

    Args:
        coverage (dict): coverage of a chromosome
        out_file (str): name of output file
    """
    with open(out_file, 'w') as f:
        for c in sorted(coverage):  # write should be ordered by chromosomes
            i = 1
            begin = 0
            length = 0
            while i < len(coverage[c]):
                if coverage[c][i-1] == coverage[c][i]:
                    length += 1
                else:
                    if coverage[c][i-1] != 0:   # null reads should be omitted
                        f.write("{0}\t{1}\t{2}\t{3}\n".format(coverage[c][i-1],
                                                    c, begin, length+begin+1))
                    begin = i
                    length = 0
                i += 1
            if len(coverage[c]) != 0:
                f.write("{0}\t{1}\t{2}\t{3}\n".format(coverage[c][i-1],
                                            c, begin, length+begin+1))


def multiply_coverage(file_a, file_b, out_file):
    """
    Writes product of coverages to a file

    Args:
        file_a (str): file with reads of first coverage
        file_b (str): file with reads of second coverage
        out_file (str): output file for coverage product
    """
    c1 = compute_coverage(read_reads(file_a))
    c2 = compute_coverage(read_reads(file_b))
    c_res = {}
    for key in c1:
        if key in c2:
            res = []
            for i in range(min(len(c1[key]), len(c2[key]))):
                res.append(c1[key][i] * c2[key][i])
            c_res[key] = res[:]
    write_coverage(c_res, out_file)

multiply_coverage('a', 'b', 'c')