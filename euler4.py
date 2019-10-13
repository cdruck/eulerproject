from utils import is_palindrome

def main():
    pals = []
    for a in range(100,1000):
        for b in range(100,1000):
            product = a * b
            if is_palindrome(product):
                pals.append(product)

    print(sorted(pals))

main()