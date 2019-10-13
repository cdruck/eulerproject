
def is_palindrome(a: int) -> bool:
    return str(a) == str(a)[::-1]

def divisors(n):
    divs = [i for i in range(2, n+1) if n % i == 0]
    return divs

def generate_n_primes(n, primes=[2]):
    p = 2
    while len(primes) < n:
        p += 1
        if is_prime(p, primes):
            primes.append(p)
    return sorted(primes, reverse=True)

def generate_primes_up_to(max_num):
    pass

def is_prime(n, primes):
    return all((n%p > 0 for p in primes))
