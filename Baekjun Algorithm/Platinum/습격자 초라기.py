'''

문제: https://www.acmicpc.net/problem/1006

1
8 100
70 60 55 43 57 60 44 50
58 40 47 90 45 52 80 40

'''

import sys

input = sys.stdin.readline
n = int(input())

for i in range(n):
    N, K = map(int, input().split())
    L_1 = list(map(int, input().split()))
    L_2 = list(map(int, input().split()))
    d = [[0] * N, [0] * N]
    all_L = sorted(L_1 + L_2, reverse= True)

    for j in all_L:


    print(all_L)

    print(d)



