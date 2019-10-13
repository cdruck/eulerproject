import numpy as np
from utils import divisors

def gcd(nums, res=[], sort=True):
    while len(nums) > 0:
        if len(nums) == 0:
            return np.prod(res)
        # remove the ones
        nums = [n for n in nums if n > 1]
        if sort:
            nums = sorted(nums)

        print(f"{nums} -- {res}")

        cand = nums.pop(0)
        divs = divisors(cand)
        for d in divs:
            nums = [int(round(n/d, 0))  if n%d == 0 else n for n in nums]
            res.append(d)
            gcd(nums, res, False)

        return np.prod(res)


def main():
    l = list(range(1, 20))
    print(gcd(l))

main()
