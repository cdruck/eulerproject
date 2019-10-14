from utils import is_prime, generate_n_primes


def is_concatenable_prime(a, b):
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))


def main():
    n_primes = 1000
    primes = generate_n_primes(n_primes, reversed=False)
    min_sum = 1e100
    for i, p1 in enumerate(primes):
        for p2 in primes[i+1:]:
            if p1+p2 < min_sum:
                if is_concatenable_prime(p1, p2):
                    min_sum = p1 + p2
                    print((p1, p2))

main()
