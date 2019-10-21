from math import factorial

def main():
    f = factorial(100)
    s = sum([int(c) for c in str(f)])
    print(s)

main()
