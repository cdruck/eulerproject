from itertools import permutations


def main():
    perms = permutations(range(0, 10))
    print(list(perms)[999999])

main()
