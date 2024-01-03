import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if cabbage_patch[ny][nx] == 1:
                cabbage_patch[ny][nx] = 0
                dfs(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    count = 0
    cabbage_patch = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        
        cabbage_patch[y][x] = 1

    for x in range(M):
        for y in range(N):
            if cabbage_patch[y][x] == 1:
                dfs(x, y)

                count += 1
        
    print(count)


# from collections import deque

# import sys
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline

# T = int(input())

# def bfs(start_x, start_y):
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
    
#     queue = deque([(start_x, start_y)])
#     cabbage_patch[start_y][start_x] = 0  # 방문한 곳은 0으로 표시

#     while queue:
#         current_x, current_y = queue.popleft()

#         for i in range(4):
#             nx = current_x + dx[i]
#             ny = current_y + dy[i]
#             if (0 <= nx < M) and (0 <= ny < N) and cabbage_patch[ny][nx] == 1:
#                 cabbage_patch[ny][nx] = 0  # 방문한 곳은 0으로 표시
#                 queue.append((nx, ny))

# for _ in range(T):
#     M, N, K = map(int, input().split())
#     count = 0
#     cabbage_patch = [[0 for _ in range(M)] for _ in range(N)]

#     for i in range(K):
#         x, y = map(int, input().split())
#         cabbage_patch[y][x] = 1

#     for x in range(M):
#         for y in range(N):
#             if cabbage_patch[y][x] == 1:
#                 bfs(x, y)
#                 count += 1

#     print(count)
