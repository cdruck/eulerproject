import numpy as np

def main():
    for a in range(1, 1000):
        for b in range(a, 1000-a):
            c = np.sqrt(a**2 + b**2)
            if a + b + c == 1000:
                print(np.prod([a, b, c]))

main()
