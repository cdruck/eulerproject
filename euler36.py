from utils import is_palindrome, is_binary_palindrome


def main():
    candidates = [i for i in range(0, 1000001) if is_palindrome(i) and is_binary_palindrome(i)]
    print(candidates)
    print(sum(candidates))

main()
