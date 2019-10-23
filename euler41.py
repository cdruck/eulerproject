from itertools import permutations

from utils import read_n_primes


def main():
    primes = list(read_n_primes(1000000))

    pands = []

    # let's approach this the other way
    for ndigits in [4, 7]:  # pandigitals with other number of digits would be divisible by 3
        digits = [str(d) for d in range(1, ndigits+1)]
        perms = [int(''.join(p)) for p in permutations(digits)]
        pands.extend([p for p in perms if p in primes])

    print(pands)
    print(max(pands))

main()
