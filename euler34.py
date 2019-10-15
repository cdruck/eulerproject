import numpy as np

from math import factorial

def main():
    fact_digits = [factorial(x) for x in range(0, 10)]
    print(fact_digits)

    candidates = []
    for cand in range(3, 2000000):
        if sum([fact_digits[int(i)] for i in str(cand)]) == cand:
            candidates.append(cand)
            print(cand)

    print(candidates)
    print(sum(candidates))

main()
