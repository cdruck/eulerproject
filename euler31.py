"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

def ways_to_pay(n, vals):
    valid_vals = [v for v in vals if v <= n]

    if n == 0:
        return [dict()]
    if len(valid_vals) == 0 or n < min(valid_vals):
        return []

    #print(f'ways_to_pay({n}, {valid_vals})')

    sols = []
    # either you take one unit of the top valued currencies, or you don't
    # take ...
    v = valid_vals[0]
    remainder = n - v
    cur_sols = ways_to_pay(remainder, vals)
    for sol in cur_sols:
        if v in sol:
            sol[v] += 1
        else:
            sol[v] = 1
    sols = sols + cur_sols

    # leave ... meaning you're not allowed to pick that currency anymore
    sols = sols + ways_to_pay(n, valid_vals[1:])

    return sols




def main():
    vals = [n*100 for n in [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]]  # force integers to avoid precision issues

    res = ways_to_pay(200, vals)

    print(res)
    print(len(res))


main()
