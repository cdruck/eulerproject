from utils import generate_n_primes

MORE_PRIMES = 50000

def main():
    prime_file = open("primes", 'r')
    primes = prime_file.read().split("\n")
    existing = len(primes)
    primes = generate_n_primes(existing + MORE_PRIMES, reversed=False)

    prime_file = open("primes", 'a+')
    prime_file.write("\n")
    prime_file.write("\n".join(map(str, primes[existing:])))
    print(len(primes))
    print(primes[-10:])

main()