import sys
import math
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

maxDepth = 0
deepest = 1
visited = [False] * (n + 1)

def dfs(cur, h):
    global maxDepth
    global deepest

    visited[cur] = True
    if maxDepth < h:
        maxDepth = h
        deepest = cur

    for k in arr[cur]:
        if not visited[k]:
            dfs(k, h + 1)


dfs(1, 0)

maxDepth = 0
visited = [False] * (n + 1)
dfs(deepest, 0)

maxDepth = 0
visited = [False] * (n + 1)
dfs(deepest, 0)

maxDepth = 0
visited = [False] * (n + 1)
dfs(deepest, 0)

maxDepth = 0
visited = [False] * (n + 1)
dfs(deepest, 0)

print(math.floor(math.log2(maxDepth + 1)))