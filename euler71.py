from utils import divisors


def main():
    # rather than listing all reduced fractions, let us see if we can find a satisfactory
    # fraction between a certain a and b, n/m, with n < m <= M, and get as close as possible to b
    b = 3/7

    print(b)

    M = 1e6

    # a good starting candidate would be 428571 / 1,000,000
    # 428571 / 999,999 is in fact == 3/7, so start a little lower
    n = 428570
    m = M-1

    e = b - n/m

    while e > 0:
        m -= 1
        e = b - n / m
        print(f'3/7 - {n}/{m} = {e}')

    # this prints 3/7 - 428570/999997.0 = 1.4285757138354782e-07, which is the solution ...
    # it could be trickier for it to work for any fraction b, but a little bit of intuition worked here.


main()
