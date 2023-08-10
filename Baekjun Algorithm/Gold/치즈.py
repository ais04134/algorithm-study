import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())
maps = [list(input().strip()) for _ in range(N)]
Cheese = 0

# 해당 위치가 몇 초 후에 전부 녹는지 저장한 배열
time = [[0] * M for _ in range(N)]
# 방문 유무 확인
visit = [[False for _ in range(M)] for _ in range(N)]
dydx = [(0,1),(0,-1),(1,0),(-1,0)]

queue = deque()
queue.append((0, 0))
visit[0][0] = True
next_list = []
day = 0

while True:
    while queue:
        i, j = queue.popleft()
        for dy, dx in dydx:
            ny, nx = i + dy, j + dx
            if  0 <= ny < N and 0 <= nx < M  and not visit[ny][nx]:
                if maps[ny][nx] == "0":
                    queue.append((ny, nx))
                    time[ny][nx] = time[i][j] + 1
                    visit[ny][nx] = True
                    day = time[ny][nx]
                else:
                    next_list.append((ny, nx))

    Old = Cheese
    if len(next_list) != 0:
        for y, x in next_list:
            queue.append((y, x))
            maps[y][x] = "0"
        Cheese = len(next_list)
        next_list = []
    else:
        break

print(day+1)
print(Old)

