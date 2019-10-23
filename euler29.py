

def main():
    aa = range(2, 101)
    bb = range(2, 101)

    powers = set()

    for a in aa:
        for b in bb:
            powers.add(a**b)
            powers.add(b**a)

    print(len(powers))

main()
