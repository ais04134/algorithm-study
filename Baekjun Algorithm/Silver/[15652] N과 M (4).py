from itertools import combinations_with_replacement

N, M = map(int, input().split())
A = list(combinations_with_replacement([i for i in range(1, N + 1)], M))

for i in sorted(A):
    for j in i:
        print(j, end= " ")
    print()