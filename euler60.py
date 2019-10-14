import itertools

from utils import read_n_primes


def is_concatenable_prime(a, b, primes):
    ab = int(str(a) + str(b)) in primes
    ba = int(str(b) + str(a)) in primes
    #print(f"{a} {b} {int(str(a) + str(b))} {ab} {int(str(b) + str(a))} {ba}")

    return ab and ba

def filter_combos(combos, mprimes, bound=1e100, use_bound=True):
    print(len(combos), len(mprimes))
    valid_combos = []
    for combo in combos:
        if not use_bound or sum(combo) < bound:
            if reversed(combo) not in valid_combos:
                couples = itertools.combinations(combo, 2)
                if all((is_concatenable_prime(*couple, mprimes) for couple in couples)):
                    valid_combos.append(combo)
                    bound = min(bound, sum(combo))
                    #print(", ".join(map(str, combo)) + " --- " + str(sum(combo)))
    return valid_combos


def main():
    n_primes = 1100
    m_primes = 100000
    nprimes = list(read_n_primes(n_primes))
    mprimes = list(read_n_primes(m_primes))
    print(mprimes[-10:])

    combos = list(itertools.combinations(nprimes, 2))
    combos = [(a, b) for a, b in combos if a < b]
    valid_couples = filter_combos(combos, mprimes, use_bound=False)
    print("valid_couple length {}".format(len(valid_couples)))


    special_primes = set()
    for a, b in valid_couples:
        special_primes.add(a)
        special_primes.add(b)
    print("{} special_primes: {}".format(len(special_primes), sorted(list(special_primes))))
    triples = []
    for combo in valid_couples:
        for prime in special_primes:
            if prime not in combo:
                triples.append((*combo, prime))
    triples = [(a, b, c) for a, b, c in triples if a < b < c]

    valid_triples = filter_combos(triples, mprimes, use_bound=False)
    print(len(valid_triples))
    print(valid_triples)

    quads = []
    for combo in valid_triples:
        for prime in special_primes:
            if prime not in combo:
                quads.append((*combo, prime))
    quads = [(a, b, c, d) for a, b, c, d in quads if a < b < c < d]
    print(quads)

    valid_quads = filter_combos(quads, mprimes, use_bound=False)
    print(len(valid_quads))
    print(valid_quads)

    quints = []
    for combo in valid_quads:
        for prime in special_primes:
            if prime not in combo:
                quints.append((*combo, prime))
    quints = [(a, b, c, d, e) for a, b, c, d, e in quads if a < b < c < d < e]
    print(quints)

    valid_quints = filter_combos(quints, mprimes, use_bound=True)
    print(len(valid_quints))

main()
