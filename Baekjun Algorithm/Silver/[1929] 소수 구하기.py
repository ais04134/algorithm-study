import sys

def get_primes(n):
    is_prime = [False, False] + [True] * (n-1)
    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return primes

m, n = map(int, sys.stdin.readline().split())

primes = get_primes(n)

for p in primes:
    if p >= m:
        print(p)