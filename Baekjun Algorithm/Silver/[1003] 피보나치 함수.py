import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    zero,one=1,0 
    for _ in range(n):
        zero,one = one,zero+one 
    print(zero,one)