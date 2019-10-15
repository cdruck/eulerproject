from utils import generate_n_primes, generate_primes_up_to
import itertools

MORE_PRIMES = 10000

def generate():
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

def read_utm():
    f = open('primes_utm_edu.txt', 'r')
    primes = f.read()
    primes = primes.split('\n')[2:]
    primes = [list(filter(lambda l: len(l)>0, line.split(' '))) for line in primes]
    primes = list(itertools.chain.from_iterable(primes))

    f = open('primes', 'w+')
    f.write('\n'.join(primes))

def main():
    read_utm()

main()



