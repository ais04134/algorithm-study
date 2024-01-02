import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

A_sort = sorted(A, key= lambda x: (x[0], x[1]))

for i in A_sort:
    print(' '.join(map(str, i)))