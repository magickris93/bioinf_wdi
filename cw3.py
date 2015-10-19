

def rec_rev(s):
	if len(s) == 1:
		return s
	else:
		return s[-1] + rec_rev(s[:-1])


def rec_pal(s):
	if len(s) <= 1:
		return True
	elif s[0] != s[-1]:
		return False
	else:
		return rec_pal(s[1:-1])


def rec_find(v, x):
	if len(v) == 0:
		return False
	elif len(v) == 1:
		return v[0] == x
	else:
		return rec_find(v[:(len(v)/2)], x) or rec_find(v[len(v)/2:], x)


def iter_merge(l1, l2):
	res = []
	while (len(l1) and len(l2)):
		if l1[0] > l2[0]:
			res.append(l2[0])
			l2 = l2[1:]
		else:
			res.append(l1[0])
			l1 = l1[1:]
	if len(l1) == 0:
		res.extend(l2)
	else:
		res.extend(l1)
	return res

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-2) + fib(n-1)


def rek_fib(k, n):
	s = ""
	if n == 0:
		return 0
	elif n == 1:
		for i in range(k-1):
			s += " "
		if k != 0:
			s += "+1"
		print s
		return 1
	elif n == 2:
		for i in range(k-1):
			s += " "
		if k != 0:
			s += "+1"
		print s
		return 1
	else:
		for i in range(k-1):
			s += " "
		if k != 0:
			s += "+"
		x = rek_fib(k+1, n-1) + rek_fib(k+1, n-2)
		s += str(x)
		print s
		return x
