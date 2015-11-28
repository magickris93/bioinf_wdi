def read_reads(plik):
	with open(plik, 'r') as f:
		lines = [line.rstrip('\n').split() for line in f]
	return lines


def compute_coverage(odczyty):
	return None


def write_coverage(pokrycie, plik_wyjsciowy):
	return None


def multiply_coverage(plikA, plikB, plik_wyjsciowy):
	return None

print read_reads('odczytyA.sdx')