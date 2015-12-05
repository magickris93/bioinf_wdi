'''Moduł z funkcjami wczytującymi listy z plików'''

def parse_list(filename):
	if filename.endswith('.li1'):
		return read_li1(filename)
	elif filename.endswith('.li2'):
		return read_li2(filename)
	elif filename.endswith('.li3'):
		return read_li3(filename)
	else:
		return None

def read_li1(filename):
	with open(filename, 'r') as f:
		content = f.read()
	content = content.lstrip('[').rstrip(']')
	return map(int, content.split(', '))


def read_li2(filename):
	with open(filename, 'r') as f:
		content = f.read()
	return map(int, content.split())


def read_li3(filename):
	with open(filename, 'r') as f:
		content = f.read()
	return map(int, content.split())	


print parse_list('list.li1')
print parse_list('list.li2')
print parse_list('list.li3')