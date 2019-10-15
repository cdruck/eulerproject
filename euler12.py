from utils import divisors


def main():
    def next_triangle_number(triangle, last_n):
        return triangle + last_n + 1, last_n + 1

    n = 1
    triangle = 1
    divs = []
    while len(divs) < 499:
        triangle, n = next_triangle_number(triangle, n)
        divs = divisors(triangle)
        print(f'{triangle}: {len(divs)}')

main()
