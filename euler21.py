from utils import divisors

def main():
    amicables = set()
    for n in range(2, 10001):
        sd = sum(divisors(n)) + 1
        if sum(divisors(sd)) + 1 == n and sd < 10000 and sd != n:
            amicables.add(n)

    print([(a, sum(divisors(a)) + 1) for a in amicables])
    print(sum(amicables))



main()
