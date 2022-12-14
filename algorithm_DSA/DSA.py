from random import randrange
from hashlib import sha1
from algorithm_DSA.prime_number import PrimeNumber

class DSA():

    def __init__(self, p=None, q=None ,g=None, y=None, x=None, r=None, s=None, num=1000) -> None:
        self.p = p
        self.q = q
        self.g = g
        self.x = x
        self.y = y
        self.r = r
        self.s = s
        self.v = None
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

    def __validate_sign(self):
        if self.r < 0 and self.r > self.q:
            return False
        if self.s < 0 and self.s > self.q:
            return False
        return True

    def generate_params(self, L = 1024, N = 160):
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
            self.r = pow(self.g, k, self.p) % self.q
            m = int(sha1(str.encode(M, "ascii")).hexdigest(), 16)
            try:
                self.s = (self.test.modinv(k, self.q) * (m + self.x * self.r)) % self.q
                return k, m, self.r, self.s
            except ZeroDivisionError:
                pass
    
    def calculate_params(self, M):
        if not self.__validate_params():
            return 'Invalid'
        if not self.__validate_sign():
            return False
        try:
            w = self.test.modinv(self.s, self.q)
        except ZeroDivisionError:
            return False
        m = int(sha1(str.encode(M, "ascii")).hexdigest(), 16)
        u1 = (m * w) % self.q
        u2 = (self.r * w) % self.q
        self.v = (pow(self.g, u1, self.p) * pow(self.y, u2, self.p)) % self.p % self.q
        return m, w, u1, u2, self.v
    
    def verify(self):
        if self.v == self.r:
            return True
        return False
    