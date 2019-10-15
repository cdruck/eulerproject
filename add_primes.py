from utils import generate_n_primes, generate_primes_up_to

MORE_PRIMES = 10000

def main():
    batch = 20
    more_primes = MORE_PRIMES
    prime_file = open("primes", 'r')
    primes = list(map(int, prime_file.read().split("\n")))

    while more_primes >= 0:
        existing = len(primes)

        primes = generate_n_primes(existing + batch, primes=primes, reversed=False)

        prime_file = open("primes", 'a+')
        prime_file.write("\n")
        prime_file.write("\n".join(map(str, primes[existing:])))
        print(list(primes[-batch:]))
        more_primes -= batch


main()



