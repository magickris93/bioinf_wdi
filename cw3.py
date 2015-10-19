
def rec_rev(s):
	if len(s) == 1:
		return s
	else:
		return s[-1] + rec_rev(s[:-1])


def rec_pal(s):
	if len(s) <= 1:
		return True
	else:
		return (s[0] == s[-1]) and (rec_pal(s[1:-1]))


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
