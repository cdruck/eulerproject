euler18 = \
"""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def max_path(triangle):
    if len(triangle) == 1:
        return triangle[0][0]

    # "eliminate" the last row by maximizing the 2-layer triangles and repeat
    n_1 = len(triangle) - 2
    n = len(triangle) - 1

    for c, val in enumerate(triangle[n_1]):
        triangle[n_1][c] += max(triangle[n][c], triangle[n][c+1])

    triangle.pop()

    res = max_path(triangle)

    return res


def main():
    # euler 18
    triangle = euler18.split("\n")
    for l, line in enumerate(triangle):
        triangle[l] = [int(n) for n in line.split(" ")]

    print("Euler 18 solution: {}".format(max_path(triangle)))

    # euler 67
    triangle = open("p067_triangle.txt", 'r').read().split('\n')
    for l, line in enumerate(triangle):
        triangle[l] = [int(n) for n in line.split(" ")]

    print("Euler 67 solution: {}".format(max_path(triangle)))

main()
