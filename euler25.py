


def main():
    last_fibs = [2, 1, 1]
    digits = 1000

    while len(str(last_fibs[-1])) < digits:
        last_fibs = [last_fibs[0]+1, last_fibs[-1], sum(last_fibs[-2:])]

    print(last_fibs)



main()
