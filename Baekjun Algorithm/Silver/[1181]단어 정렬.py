'''

https://www.acmicpc.net/problem/1181

'''

import sys
input = sys.stdin.readline
n = int(input())

answer = sorted(list(set([input().strip() for _ in range(n)])))
answer.sort(key=len)

for i in answer:
    print(i)
