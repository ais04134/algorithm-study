'''

1914번 문제 출처: https://www.acmicpc.net/problem/1914

유형: 재귀

'''

import sys

input = sys.stdin.readline
N = int(input())

def move(N, a, b, c):
    if N == 1:
        print(f"{a} {c}")
    else:
        move(N-1, a, c, b)
        move(1, a, b, c)
        move(N-1, b, a, c) # 이걸 어떻게 바로 생각해내지??... 나는 한참 걸렸다.

print(2**N-1) # N개의 원반이 있으면 2^(N-1)번 움직여야 한다. 이건, 직접 손으로 3~4개라 생각하고 움직여 보면 안다.
if N <= 20:
    move(N, 1, 2, 3)





