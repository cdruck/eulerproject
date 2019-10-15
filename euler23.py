from utils import divisors
import itertools


def is_abundant(n):
    return sum(divisors(n)) + 1 > n

def main():
    max_n = 28123
    abundants = [i for i in range(1, max_n) if is_abundant(i)]
    print(abundants)

    sum_of_2_abundants = {sum(n) for n in itertools.combinations(abundants, 2)}
    for n in abundants:
        sum_of_2_abundants.add(2*n)
    print(len(sum_of_2_abundants))
    sum_of_2_abundants = {n for n in sum_of_2_abundants if n < max_n}
    print(len(sum_of_2_abundants))

    candidates = list(range(1, 28123))

    ans = list(filter(lambda c: c not in sum_of_2_abundants, candidates))

    print(ans)
    print(sum(ans))


main()
