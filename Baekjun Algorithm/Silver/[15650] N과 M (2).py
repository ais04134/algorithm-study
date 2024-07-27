from itertools import combinations

N, M = map(int, input().split())
A = list(combinations([i for i in range(1, N + 1)], M))

for i in sorted(A):
    for j in i:
        print(j, end= " ")
    print()