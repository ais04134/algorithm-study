import sys
input = sys.stdin.readline

computers_number = int(input())
computers_pairs_number = int(input())
graph =[[False] * (computers_number+1) for _ in range(computers_number+1)]

for i in range(computers_pairs_number):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1 # input 데이터를 graph 형식으로 변환

visited = [False] * (computers_number+1)
count = 0

def dfs(v):
    global count

    visited[v] = True

    for i in range(1, computers_number + 1):
        if not visited[i] and graph[v][i] == 1: # 방문하지 않았고, 연결되어 있다면
            count += 1
            dfs(i)

    return count

print(dfs(1))