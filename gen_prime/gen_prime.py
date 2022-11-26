from math import log


def sieve_eratosthenes(n): #решето Эратосфена
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

def test_trial_division2(num, sieve): # тест на делимости первых N чисел
    for s in sieve:
        if num % s == 0 and num != s:
            return False
        elif num == s:
            return True
        if s > num:
            return True
    return True

def test_trial_division(num):# тест пробных делений 
    i = 2
    while i*i <= num:
        if num % i:
            i+=1
        else:
            return False
    return True


def is_prime_miller(num, sieve):
    if not test_trial_division2(num, sieve):
        return False
    logN = log(num)
    loglogN = log(logN)
    maxChecked = logN * loglogN / log(2)
    baseCurrent = 2
    isPrime = True
    
    while baseCurrent <= maxChecked:
        if not is_strong_pseudo_prime(num, baseCurrent):
            isPrime = False
            break
        baseCurrent = next_prime(baseCurrent)
    return isPrime

def is_strong_pseudo_prime(num, baseCurrent):
    exp = num - 1
    ost_1 = exp
    res = baseCurrent**exp % num
    if res != 1:
        return False
    while True:
        exp = exp / 2
        res = baseCurrent**exp % num
        if res == ost_1:
            return True
        if exp % 2:
            res = baseCurrent**exp % num
            if res == 1:
                return True
            break
    return False

sieve = sieve_eratosthenes(100)

def next_prime(num):
    return sieve[sieve.index(num)+1]
    

if __name__ == '__main__':
    import random
    #print(test_trial_division(5, sieve_eratosthenes(1000)))
    import pdb; pdb.set_trace()
    print(is_prime_miller(15, sieve)) #63053729533
    while True:
        n = random.randint(2**35, 2**36 - 1)
        if test_trial_division(n):
        #if is_prime_miller(n, sieve):
            print('простое', n)
            break
        print(n)
    #print(prime_factor())