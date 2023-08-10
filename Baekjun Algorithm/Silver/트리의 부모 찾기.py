'''

문제: https://www.acmicpc.net/problem/11725

'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

tree= [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0 for _ in range(N+1)]
queue=[1]

while queue:
    child = queue.pop(0)
    for i in tree[child]:
        if parent[i]==0:
            parent[i]=child
            queue.append(i)

for i in range(2, N+1):
    print(parent[i])


# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N = int(input())
# answer = [0 for x in range(N+1)]
# tree = dict()
#
# for i in range(1, N + 1):
#     tree[i] = []
# for _ in range(N - 1):
#     n1, n2 = map(int, input().split())
#     tree[n1].append(n2)
#     tree[n2].append(n1)
#
# for i in tree.get("1"):
#     answer[i] = 1
# queue = deque(tree.get("1"))
# while queue:
#
#
# print(tree)