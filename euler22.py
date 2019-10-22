

def score(name):
    return sum([ord(c)-ord('A')+1 for c in name])

def main():
    names = open('P022_names.txt').read().replace('"','').split(',')
    names = sorted(names)

    total = 0
    for n, name in enumerate(names):
        total += (n+1) * score(name)

    print(total)

main()
