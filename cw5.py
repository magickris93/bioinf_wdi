def find_seq(seq, filename):
	with open (filename, "r") as myfile:
		data = myfile.read().replace('\n', '')

	count = 0
	for i in range (len(data)):
		if data[i:len(seq)+i] == seq:
			count += 1	
	return count
	
print find_seq('ACGT', 'DNA.txt')
