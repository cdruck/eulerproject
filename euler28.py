"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

73                      81
   43 44 45 46 47 48 49 50
   42 21 22 23 24 25 26
   41 20  7  8  9 10 27
   40 19  6  1  2 11 28
   39 18  5  4  3 12 29
   38 17 16 15 14 13 30
   37 36 35 34 33 32 31
65                      57
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

def main():
    # the 5x5 "spiral" has a "radius" of 2 starting with its center "1"
    # let's analyze the diagonal numbers
    # we note that the upright diagonal is formed of the squares 1, (1+2)**2, (1+2*2)**2 ... and
    # layer 0: 1
    # layer 1: 3 + 5 + 7 + 9 = 24 = 4*9 - 3*4*1
    # layer 2: 13 + 17 + 21 + 25 = 76 = 4*25 - 3*4*2
    # layer 3: 31 + 37 + 43 + 49 = 160 = 4*49 - 3*4*3
    # layer 4: 57 + 65 + 73 + 81 = 276 = 4*81 - 3*4*4

    print([1]+[4*((2*n+1)**2 - 3*n) for n in range(1, 501)])
    res = sum([1]+[4*((2*n+1)**2 - 3*n) for n in range(1, 501)])

    print(res)

    pass

main()
