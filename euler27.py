from utils import read_n_primes


def main():
    primes = list(read_n_primes(500000))

    max_primes = 0
    max_coeff_prod = 0

    # brute force all polynomials of the form n**2 + a n + b with -1000 <= a, b <= 1000
    # polynomial in n=0 should be a (positive) prime, so we can restrict the scope of b
    for b in [p for p in primes if p <= 1000]:
        # polynomial in n=1 should be a (positive) prime, so 1 + a + b must be prime, so a must be in the
        # set of [p-1-b] where p is prime
        for a in [p-1-b for p in primes if p-1-b <= 1000]:
            n = 0
            while int(n**2 + a*n + b) in primes:
                n += 1
            n -= 1

            if n > max_primes:
                max_primes = n
                max_coeff_prod = a*b
                print (f'n**2 + {a} n + {b} produces {n} conseq primes')
                print (max_coeff_prod)

    # last print gives the answer ...

main()
