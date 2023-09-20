import sys
import math

input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))

def is_prime_number(x):
    if x == 1: return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False 
        return True 

print(sum(map(lambda x: is_prime_number(x), p)))
