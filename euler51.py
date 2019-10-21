from utils import read_primes
from itertools import combinations
import re


def family(pat, primes_str):
    return list(re.findall(r'\b{}\b'.format(pat), primes_str))


def families(ndigits, primes):
    free_pat = ['\d'] * ndigits
    ndigit_primes = family(''.join(free_pat), primes)
    ndigit_primes_str = ' '.join(ndigit_primes)

    fams = dict()

    # what are the possible family patterns?
    pats = []
    for nd in range(ndigits):
        pats = list(combinations(range(ndigits), nd))

    for prime in ndigit_primes:
        for pat in pats:
            pattern = list(prime)
            for p in pat:
                pattern[p] = '\d'
            pattern = ''.join(pattern)
            if pattern not in fams:
                fams[pattern] = family(pattern, ndigit_primes_str)

    return fams


def main():
    f = open('primes')

    primes_str = " ". join(f.read().split("\n"))
    f = families(3, primes_str)

    print(f)

main()
