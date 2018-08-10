import math

def prime_factorization(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n /= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            primes.append(i)
            n /= i
    if n > 2:
        primes.append(int(n))
    return primes


print(prime_factorization(10))
