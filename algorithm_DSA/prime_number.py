from math import log
from random import randrange

class PrimeNumber():
    
    def __init__(self, num = 1000):
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

    def test_miller(self, num): # тест Миллера
        #if not self.test_trial_division_prime(num, sieve):
        #    return False
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

    def test_miller_rabin(self, num, iconfidence= 40):
        if  num == 2:
            return True
        if  num % 2 == 0:
            return False
        r, s = 0, num - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(iconfidence):
            a = randrange(2,  num - 1)
            x = pow(a, s, num)
            if x == 1 or x == num - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, num)
                if x == num - 1:
                    break
            else:
                return False
        return True

    def is_prime(self, num, iter = 40):# проверка числа на простоту 2 способами
        if  self.test_miller_rabin(num, iter) and self.test_miller(num):
            return True
        return False

    def test_solovay_strassen(self, num, iconfidence= 3):# тест Соловая-Штрасса 
        for i in range(iconfidence):
            a = randrange(1, num)
            if self.__gcd(a, num) > 1:
                return False
            if not self.__jacobi(a, num) % num == pow(a, (num - 1)//2,num):
                return False
        return True

    def modinv(self, a, m):
        g, x, y = self.__interactive_egcd(a,m)
        if g != 1:
            return None
        else:
            return x % m
    
    def __interactive_egcd(self, a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
            b,a, x,y, u,v = a,r, u,v, m,n
        return b, x, y

    def __jacobi(self, a, n):
        if a == 0:
            if n == 1:
                return 1
            else:
                return 0
        elif a == -1:
            if n%2 == 0:
                return 1
            else:
                return -1
        elif a == 1:
            return 1
        elif a == 2:
            if n % 8 == 1 or n % 8 == 7:
                return 1
            elif n % 8 == 3 or n % 8 == 5:
                return -1
        elif a >= n:
            return self.__jacobi(a%n, n)
        elif a%2 == 0:
            return self.__jacobi(2, n) * self.__jacobi(a//2, n)
        else:
            if a % 4 == 3 and n % 4 == 3:
                return -1 * self.__jacobi(n, a)
            else:
                return self.__jacobi(n, a)

    def __gcd(self, a, b):
        while b!=0:
            c = a % b
            a = b
            b = c
        return a

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
    #print(test_trial_division(5, sieve_eratosthenes(1000)))
    tests = PrimeNumber(1000)
    n = 0
    #while True:
        #n = randrange(2**511, 2**512)
        #n = random.randint(2**511, 2**1024 - 1)
    for n in [16850784224551826771, 14042614733540932519]:
        if tests.is_prime(n):#tests.test_trial_division_prime(n, tests.sieve): 
        #if is_prime_miller(n, sieve):
            print('простое', n)
            #break
        #print(n)
        else:
            print('составное', n)
    #print(prime_factor())
    #p = tests.find_number_p(n)
    #print('q=', n, '\np=', p)