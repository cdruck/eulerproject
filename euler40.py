from numpy import prod


def main():
    # brute force
    # we need to build d until 1e6 decimals
    # d = 0. ...
    decimals = ""
    n = 0
    tot = 0
    while tot < 1e6:
        n += 1
        tot += len(str(n))
        decimals += str(n)


    indices = [10**n for n in range(0, 7)]

    ds = [int(decimals[i-1]) for i in indices]

    print(prod(ds))

main()
