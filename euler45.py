import numpy as np

def main():
    specials = []
    hexs = (i*(2*i-1) for i in range(1, 10000))

    for h in hexs:
        # is it pentagonal?
        # solution of 3*x**2-x-2h = 0 must be a positive integer
        x1 = (1 + (1 + 4*3*2*h)**0.5)/2
        x2 = (1 - (1 + 4*3*2*h)**0.5)/2
        if x1 % 1 == 0 or x2 % 1 == 0:
            print(f'{h} is pentagonal')
        else:
            continue

        # is it Triagonal?
        # solution of 0 = n**2 + n - 2h must be a positive integer
        x1 = (-1 + (1 + 4*2)**0.5)/2
        x2 = (-1 - (1 + 4*2)**0.5)/2
        if x1 % 1 == 0 or x2 % 1 == 0:
            print(f'{h} is triagonal')
        else:
            continue

        specials.append((h))
        print(specials)
        print(sum(specials))

main()
