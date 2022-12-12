from random import randrange
from hashlib import sha1
from prime_number import PrimeNumber

class DSA():

    def __init__(self, p=None, q=None ,g=None, y=None, x=None, num=1000) -> None:
        self.p = p
        self.q = q
        self.g = g
        self.x = x
        self.y = y
        self.test = PrimeNumber(num)

    def __generate_p_q(self, L = 1024, N = 160):
        g = N
        n = (L - 1) // g
        b = (L - 1) % g
        while True:
            # generate q
            while True:
                s = randrange(1, 2**g)
                a = sha1(s.to_bytes(len(bin(s)[2:])//8 + 1, byteorder='big')).hexdigest()
                zz = (s+1)%(2**g)
                z = sha1(zz.to_bytes(len(bin(zz)[2:])//8 + 1, byteorder='big')).hexdigest()
                U = int(a, 16) ^ int(z, 16)
                mask = 2**(N-1)+1
                q = U | mask
                if self.test.is_prime(q):
                    break
            # generate p
            i = 0
            j = 2
            while i < L*4:
                V = []
                for k in range(n + 1):
                    arg = (s + j + k) % (2 ** g)
                    zzv = sha1(arg.to_bytes(len(bin(arg)[2:])//8 + 1, byteorder='big')).hexdigest()
                    V.append(int(zzv, 16))
                W = 0
                for qq in range(0, n):
                     W += V[qq] * 2 ** (g * qq)
                W += (V[n] % 2 ** b) * 2 ** (g * n)
                X = W + 2 ** (L - 1)
                c = X % (2 * q)
                p = X - c + 1  # p = X - (c - 1)
                if p >= 2 ** (L - 1):
                    if self.test.is_prime(p):
                        self.p = p
                        self.q = q
                        return p, q
                i += 1
                j += n + 1
        #while True:
        #    q = randint(2**(N-1), 2**N-1)
        #    if not self.test.is_prime(q):
        #        continue
        #    for p in range(2**(L-1), 2**L-1, 2):
        #        if (p-1)%q == 0 and self.test.is_prime(p):
        #            self.p = p
        #            self.q = q
        #            return p, q

    def __generate_g(self):
        while True:
            h = randrange(2, self.p - 1)
            exp = (self.p-1) // self.q
            g = pow(h, exp, self.p)
            if g > 1:
                self.g = g
                return 
    
    def __validate_params(self):
        if self.test.is_prime(self.p) and self.test.is_prime(self.q):
            return True 
        if pow(self.g, self.q, self.p) == 1 and self.g > 1 and (self.p - 1) % self.q:
            return True
        return False

    def __validate_sign(self, r, s):
        if r < 0 and r > self.q:
            return False
        if s < 0 and s > self.q:
            return False
        return True

    def generate_params(self, L = 128, N = 20):
        self.__generate_p_q(L, N)
        self.__generate_g()
        return self.p, self.q, self.g

    def generate_keys(self):
        self.x = randrange(2, self.q)
        self.y = pow(self.g, self.x, self.p)
        return self.x, self.y

    def sign(self, M):
        if not self.__validate_params():
            return None
        while True:
            k = randrange(2, self.q)
            r = pow(self.g, k, self.p) % self.q
            m = int(sha1(M).hexdigest(), 16)
            try:
                s = (self.test.modinv(k, self.q) * (m + self.x * r)) % self.q
                return r, s
            except ZeroDivisionError:
                pass
    
    def verify(self, M, r, s):
        if not self.__validate_params():
            return 'Invalid'
        if not self.__validate_sign(r, s):
            return False
        try:
            w = self.test.modinv(s, self.q)
        except ZeroDivisionError:
            return False
        m = int(sha1(M).hexdigest(), 16)
        u1 = (m * w) % self.q
        u2 = (r * w) % self.q
        v = (pow(self.g, u1, self.p) * pow(self.y, u2, self.p)) % self.p % self.q
        if v == r:
            return True
        return False
    
if __name__ == '__main__':
    N = 160
    L = 1024
    dsa = DSA()
    #print(dsa.generate_params(1024, 160))
    p, q, g = dsa.generate_params(L, N)
    x, y = dsa.generate_keys()
    
    text = "ASCII"
    M = str.encode(text, "ascii")
    r, s = dsa.sign(M)
    if dsa.verify(M, r, s):
        print('All ok')
    print(M, r, s, p, q, g, y, x, sep='\n')
