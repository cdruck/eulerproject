import os
import itertools
import numpy as np

beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)

def is_palindrome(a: int) -> bool:
    return str(a) == str(a)[::-1]

def is_binary_palindrome(a: int) -> bool:
    s = "{0:b}".format(a)
    return s == s[::-1]

def divisors(n):
    divs = [i for i in range(2, n+1) if n % i == 0]
    return divs

def generate_n_primes(n, primes=[], reversed=True):
    if primes is None or len(primes) == 0:
        p = 2
    else:
        p = int(primes[-1])
    while len(primes) < n:
        if p == 2:
            p = 3
        else:
            p += 2
        if is_prime(p, primes):
            primes.append(p)
    if reversed is not None:
        return sorted(primes, reverse=reversed)
    else:
        return primes

def generate_primes_up_to(max_num):
    primes = []
    cands = [2] + list(range(3, max_num, 2))
    while len(cands) > 0:
        cand = cands.pop(0)
        primes.append(cand)
        cands = [c for c in cands if c % cand > 0]  # sieve
    return primes

def is_prime(n, primes=[2]):
    if not primes:
        pass
    reduced_primes = filter(lambda y: y <= np.sqrt(n)+1, primes)
    return all([n%p > 0 for p in reduced_primes])

def read_primes():
    f = open('primes')
    return (int(i) for i in f.read().split("\n"))

def read_n_primes(n):
    return itertools.islice(read_primes(), n)
