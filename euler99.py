from math import log10

def main():
    be = [tuple(map(int, l.split(','))) for l in open('p099_base_exp.txt').read().split('\n')]

    # this is pretty obvious ... numbers are too big to be computed as such, but we can map them to a
    # monotonous function, in particular log (in any base, I picked 10), which has the property that
    # log(a**b) == b * log(a) which is much more manageable.
    # comparing the log values will give the correct line number ...

    max_n = 0
    max_log = -1e99
    for n, (b, e) in enumerate(be):
        curlog = e*log10(b)
        if max_log < curlog:
            max_n = n
            max_log = curlog

    print(max_n + 1)

main()
