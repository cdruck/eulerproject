
cache = dict()

def collatz(n):
    if cache.get(n) is not None:
        return cache[n]

    if n == 1:
        cache[n] = [n]
    elif n % 2 == 0:
        cache[n] = [n] + collatz(n//2)
    else:
        cache[n] = [n] + collatz(3*n+1)
    return cache[n]


def main():
    for n in range(1, 1000001):
        collatz(n)

    # use cache to recover max length
    lengths = {n: len(cache[n]) for n in cache}
    print(max(lengths, key=lengths.get))

main()
