import itertools

from utils import read_n_primes


def main():
    four_digits = [str(i) for i in read_n_primes(1229) if len(str(i)) == 4]

    candidates = []
    for fd in four_digits:
        perms = set(map(lambda c: ''.join(c), itertools.permutations(fd)))
        perms = list(filter(lambda p: p in four_digits and int(p)>1000, perms))

        combos = []
        if len(perms) >= 3:
            combos = [sorted(list(map(int, l))) for l in list(itertools.combinations(list(perms), 3))]

        for combo in combos:
            if combo[1] - combo[0] == combo[2] - combo[1]:
                candidates.append(combo)


    print(candidates)
    print(list(c in map(int,four_digits) for combo in candidates for c in combo))
    print([''.join(map(str,c)) for c in candidates])

main()
