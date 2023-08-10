from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

N = int(input())

arr = tuple(map(int, input().split()))
ps = [True for _ in range(N)]
ps_two = [True for _ in range(N)]
max_num = max(arr)
min_num = min(arr)
ans = [arr[0]]
print(arr)
print(ps)

for i in range(N):
    for j in range(N):
        if ps[j] and arr[j] <= max_num:
            if ans[-1] < arr[j] and ps_two:
                ans.append(arr[j])
                ps_two[j] = False
        else: ps[j] = False




        if j == N:
            max_num = ans[-1]
        print(ans)


