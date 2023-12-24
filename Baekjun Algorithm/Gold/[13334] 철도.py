"""

문제 출처: https://www.acmicpc.net/problem/13334

<test case>

5
-5 5
30 40
-5 5
50 40
5 -5
10

"""
from heapq import heappush, heappop
# import sys
# i=sys.stdin.readline
# n=int(i())
# l=[sorted(map(int,i().split()),reverse=True)for _ in' '*n)]
# l.sort()
# L=int(i())
# a,h=0,[]
# for s,e in l:
#     if L<s-e: continue
#     while h and h[0]<s-L: heappop(h)
#     heappush(h,e)
#     if a<len(h):a=len(h)
# print(a)


# from heapq import heappush, heappop
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# lines = []
# for _ in range(n):
#     r, t = map(int, input().split())
#     if r < t:
#         r, t = t, r
#     lines.append((r, t))
#
# lines.sort()
# L = int(input())
# ans, heap = 0, []
#
# for s, e in lines:
#     if L < s - e: continue
#     while heap and heap[0] < s - L: heappop(heap)
#     heappush(heap, e)
#     ans = max(ans, len(heap))
#
# print(ans)

# from heapq import heappush, heappop
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# lines = []
# for i in range(n):
#     d = input().strip()
#     space = d.find(" ", 1, - 1)
#     r, t = int(d[:space]), int(d[space+1:])
#     if r < t:
#         r, t = t, r
#     lines.append((r, t))
#
# lines.sort()
# L = int(input())
# ans, heap = 0, []
#
# for s, e in lines:
#     if L < s - e: continue
#     while heap and heap[0] < s - L: heappop(heap)
#     heappush(heap, e)
#     ans = max(ans, len(heap))
#
# print(ans)

import os, io
from heapq import heappush, heappop
input = io.BytesIO(os.read(0, 999999999)).readline

N = int(input())
arr = []
for i in range(N):
    h, o = map(int, input().split(b" ", 1))
    if h > o: arr.append((h, o))
    else: arr.append((o, h))
D = int(input())
arr = [x for x in arr if x[0]-x[1] <= D]
arr.sort()
heap = []
ans = 0
for o, h in arr:
    bound = o - D
    while heap and heap[0] < bound:
        heappop(heap)
    heappush(heap, h)
    if ans < len(heap):
        ans = len(heap)

os.write(1, (str(ans) + "\n").encode())


#wlsxkr77님의 코드로 테스트 진행했습니다.
from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def solve():
    N = int(input())
    arr = []
    for i in range(N):
        h, o = map(int, input().split(" ", 1))
        if h > o:
            arr.append((h, o))
        else:
            arr.append((o, h))
    D = int(input())
    arr = [x for x in arr if x[0]-x[1] <= D]
    arr.sort()
    heap = []
    ans = 0
    for o, h in arr:
        bound = o - D
        while heap and heap[0] < bound:
            heappop(heap)
        heappush(heap, h)
        if ans < len(heap):
            ans = len(heap)

    return ans


if __name__ == '__main__':
    print(solve())

# import sys
# from heapq import heappush, heappop
# stdin = sys.stdin.buffer
#
# stdin.readline()
# arr = stdin.read().split()
# d = int(arr.pop())
# lines = sorted(map(lambda a, b: (a, b) if a < b else (b, a), ([map(int, arr)] 2)), key=lambda x: x[1])




# from heapq import heappush, heappop
# from sys import stdin
# input = stdin.readline
#
# n = int(input())
# lines = []
# for i in range(n):
#     r, t = map(int, input().split(" ", 1))
#     if r < t:
#         r, t = t, r
#     lines.append((r, t))
#
# lines.sort()
# L = int(input())
# ans, heap = 0, []
#
# for s, e in lines:
#     if L < s - e: continue
#     while heap and heap[0] < s - L: heappop(heap)
#     heappush(heap, e)
#     ans = max(ans, len(heap))
#
# print(ans)

# for i, j in heap_two:
#     if L < i - j:
#         continue
#     while heap_two and heap_two[0] < i - L:
#         heappop(heap_two)
#     heappush(heap_two, j)
#     if answer < len(heap_two):
#         answer = max(answer, len(heap_two))
#
# print(answer)
#
# lines = [sorted(map(int, input().split())) for _ in range(n)]
# lines.sort(key=lambda x: x[1])
# L = int(input())
# ans, heap = 0, []
#
# for s, e in lines:
#     if L < e - s: continue
#     while heap and heap[0] < e - L: heappop(heap)
#     heappush(heap, s)
#     if ans < len(heap): ans = len(heap)
#
# print(ans)

import sys

input = sys.stdin.buffer.readline

N, B, C = map(int, input().split())
arr = list(map(int, input().split()))

from functools import reduce

reduce(lambda x, y: x + y, [1, 2, 3], 0)