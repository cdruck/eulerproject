"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, 
it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, 
is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, 
determine the number of blue discs that the box would contain.
"""


"""
First a bit of analysis ... 

Any solution to this problem would be of the form of B blue balls out of M, and satisfies
(B/M) * xx(B-1)/(M-1) = 1/2, or

2 B**2 - 2B - M (M-1) = 0

solve using https://www.alpertron.com.ar/QUAD.HTM

"""


def solve_quad_polynomial(a, b, c):
    discriminant = (b**2 - 4*a*c)**0.5
    return (-b + discriminant)/(2*a), (-b - discriminant)/(2*a)


def main():
    b = 15;
    n = 21;
    target = 1000000000000;

    while n < target:
        btemp = 3 * b + 2 * n - 2;
        ntemp = 4 * b + 3 * n - 3;

        b = btemp;
        n = ntemp;

    print(b)

main()
