def find_seq(seq, filename):
	with open(filename, "r") as myfile:
		data = myfile.read().replace('\n', '')

	pos = []
	for i in range (len(data)):
		if data[i:len(seq)+i] == seq:
			pos.append(i)
	print pos
	print len(pos)


def statystyki(filename):
	f = open(filename, 'r')
	out_name = 'statystyka_' + filename
	out = open(out_name, 'w')
	lines = 0
	
	with open(filename, "r") as myfile:
		data = myfile.read().replace('\n', '')
	
	lines = len(data.split('\n'))
	words = len(data.split())
	exclam = data.find('!')
	
	out.write(str(lines) + '\n')
	out.write(str(words) + '\n')
	out.write(str(exclam) + '\n')
	
	f.close()
	out.close()

	
def kmers(k, filename):
	with open(filename, "r") as myfile:
		data = myfile.read().replace('\n', '')
	
	d = {}	
	
	for i in range(len(data)-k):
		if data[i:k+i] in d:
			d[data[i:k+i]] += 1
		else:
			d[data[i:k+i]] = 1
			
	max_key = ''
	max_count = 0
	for key in d:
		if d[key] > max_count:
			max_count = d[key]
			max_key = key
	print max_key


def avg_signal(filename):
	f = open(filename, 'r')
	count = 0
	s = 0.0
	for line in f:
		l = line.split()
		if len(l) == 9:
			if (int(l[3]) >= 1000000) and (int(l[4]) <= 5000000):	
				count += 1
				s += float(l[5])
	f.close()
	return s / count



find_seq('ACGT', 'DNA.txt')				
kmers(4, 'DNA.txt')
print avg_signal('HP1b.gff3')
