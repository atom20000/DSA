seed = 1103515245

class random:
    @classmethod
    def rand_number(cls) -> int:
        a = 1103515245
        c = 12345
        m = 2 ** 31
        global seed
        seed = (a * seed + c) % m
        return seed

    @classmethod
    def randrange(cls, start, stop) -> int:
        r = range(start, stop)
        return r[cls.rand_number() % len(r)]

def  pow(self, n, ex, d):
	res = 1
	n %= d
	while ex > 0:
		if ex & 1:
			res  = (res * n) % d
		ex = ex >> 1
		n = (n * n) % d
	return res
