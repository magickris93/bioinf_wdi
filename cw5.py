def find_seq(seq, filename):
	with open(filename, "r") as myfile:
		data = myfile.read().replace('\n', '')

	pos = []
	for i in range (len(data)):
		if data[i:len(seq)+i] == seq:
			pos.append(i)
	print pos
	print len(pos
	
print find_seq('ACGT', 'DNA.txt')


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


	
statystyki('DNA.txt')
kmers(4, 'DNA.txt')
