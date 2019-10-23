from utils import read_n_primes

def is_circular_prime(n, primes):
    rotations = []
    s = str(n)
    if len(s) > 1:
        for delta in range(1, len(s)):
            s2 = s[delta:] + s[0:delta]
            rotations.append(int(s2))

    return all((r in primes for r in rotations))

def main():
    primes = list(read_n_primes(78498))

    circular_primes = [p for p in primes if is_circular_prime(p, primes)]
    print(circular_primes)
    print(len(circular_primes))

main()
