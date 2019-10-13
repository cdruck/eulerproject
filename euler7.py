# a little brutal, but ...

def generate_n_primes(n):
    primes = [2]
    p = 2
    while len(primes) < n:
        p += 1
        if is_prime(p, primes):
            primes.append(p)
    return sorted(primes, reverse=True)

def is_prime(n, primes):
    return all([n%p > 0 for p in primes])

def main():
    print(generate_n_primes(10001))

main()
