from math import log

class PrimeNumber():
    
    def __init__(self, num):
        self.sieve = self.sieve_eratosthenes(num)
    
    def sieve_eratosthenes(self, n): #решето Эратосфена
        D = {}
        P = []
        q = 2
        while len(P) < n:
            if q not in D:
                D[q * q] = [q]
                P.append(q)
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]

            q += 1
        return P

    def test_trial_division_prime(self, num, sieve): # тест на делимости первых N простых чисел
        for s in sieve:
            if num % s == 0 and num != s:
                return False
            elif num == s:
                return True
            if s > num:
                return True
        return True

    def test_trial_division(self, num):# тест пробных делений 
        i = 2
        while i*i <= num:
            if num % i:
                i+=1
            else:
                return False
        return True

    def test_is_prime_miller(self, num, sieve):
        if not self.test_trial_division_prime(num, sieve):
            return False
        logN = log(num)
        loglogN = log(logN)
        maxChecked = logN * loglogN / log(2)
        baseCurrent = 2
        isPrime = True

        while baseCurrent <= maxChecked:
            if not self.__is_strong_pseudo_prime(num, baseCurrent):
                isPrime = False
                break
            baseCurrent = self.__next_prime(baseCurrent)
        return isPrime

    def find_number_p(self, num):
        #mul = 2
        #while True:
        #    n = num * mul + 1
        #    if self.test_is_prime_miller(n, self.sieve) and len(bin(n)[2:]):
        #        return n
        #    mul+=1
        #for i in range(2**1023, 2**1024):
        #    if self.test_is_prime_miller(i, self.sieve) and (i-1)%num == 0:
        #        return i
        #for i in range(2**1023, 2**1024):
        #    if self.test_is_prime_miller(i, self.sieve) and pow(i, num - 1, num) == 1:
        #        return i
        pass

    def __is_strong_pseudo_prime(self, num, baseCurrent):
        exp = num - 1
        ost_1 = exp
        res = pow(baseCurrent, exp, num)
        if res != 1:
            return False
        while True:
            exp = exp // 2
            res = pow(baseCurrent, exp, num)
            if res == ost_1:
                return True
            if exp % 2:
                res = pow(baseCurrent, exp, num)
                if res == 1:
                    return True
                break
        return False
    
    def __next_prime(self, num):
        return self.sieve[self.sieve.index(num)+1]

if __name__ == '__main__':
    import random
    #print(test_trial_division(5, sieve_eratosthenes(1000)))
    tests = PrimeNumber(1000)
    n = 0
    while True:
        n = random.randint(2**159, 2**160 - 1)
        #n = random.randint(2**511, 2**1024 - 1)
        if tests.test_is_prime_miller(n, tests.sieve):#tests.test_trial_division_prime(n, tests.sieve): 
        #if is_prime_miller(n, sieve):
            print('простое', len(bin(n)[2:]))
            break
        #print(n)
    #print(prime_factor())
    p = tests.find_number_p(n)
    print('q=', n, '\np=', p)