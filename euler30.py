
def main():
    tot = 0
    # calculating an upper bound is the trick ... "random" high value used here
    for n in range(2, 400000):
        s = sum([int(d) ** 5 for d in str(n)])
        if s == n:
            tot += n
            print(s)
    print(tot)

main()
