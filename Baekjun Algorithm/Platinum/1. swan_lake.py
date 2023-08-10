'''

문제출처 : https://www.acmicpc.net/problem/3197

'''

'''

8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...

'''
# import os, io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# Ver_6

import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())
maps = [list(input().strip()) for _ in range(N)]

# 해당 위치가 몇 초 후에 전부 녹는지 저장한 배열
time = [[0] * M for _ in range(N)]
# 방문 유무 확인
visit = [[False for _ in range(M)] for _ in range(N)]
swan = []
dydx = [(0,1),(0,-1),(1,0),(-1,0)]

queue = deque()
for i in range(N):  # 물, 백조 구별 및 위치 확인
    for j in range(M):
        if maps[i][j] == ".":
            queue.append((i, j))
            visit[i][j] = True
        elif maps[i][j] == "L":
            queue.append((i, j))
            swan.append((i, j))
            visit[i][j] = True

while queue: # 각 위치들에 있는 빙하가 녹는 시간을 time에 저장
    i, j = queue.popleft()
    for dy, dx in dydx:
        ny, nx = i + dy, j + dx
        if not visit[ny][nx] and 0 <= ny < N and 0 <= nx < M:
            queue.append((ny, nx))
            time[ny][nx] = time[i][j] + 1
            visit[ny][nx] = True
            day = time[ny][nx] # 일딴 이렇게 짜는데 개선 필요함
return day

# BFS
def BFS(start_y, start_x, dy, dx, Day):
    changing_set = set([])
    queue = [[start_y, start_x]]

    while queue:
        maps[start_y][start_x] = "."
        pos = queue[0]
        del queue[0]

        for i in range(4):
            ny = pos[0] + dy[i]
            nx = pos[1] + dx[i]
            if 0 <= ny < N  and 0 <= nx < M:
                if maps[ny][nx] == ".":
                    if time[ny][nx] == 0:
                        time[ny][nx] = 1
                        queue.append([ny, nx])
                else:
                    time[ny][nx] = Day + 1
                    changing_set.add((ny, nx))
                    maps[ny][nx] = "."

    return changing_set

def BFS_find(start_A_y, start_A_x, start_L_y, start_L_x, dy, dx):
    min_day_list = []
    if start_A_y - start_L_y > 0:
        if start_A_x - start_L_x > 0:
            for i in range(abs(start_A_y - start_L_y) - 1):
                min_day_list.append(time[start_A_y - (i + 1)][start_A_x])
                print(min_day_list)
            for j in range(abs(start_A_x - start_L_x) - 1):
                min_day_list.append(time[start_A_y][start_A_x - (j + 1)])
                print(min_day_list)
        else:
            for i in range(abs(start_A_y - start_L_y) - 1):
                min_day_list.append(time[start_A_y - (i +1)][start_A_x])
            for j in range(abs(start_A_x - start_L_x)):
                min_day_list.append(time[start_A_y][start_A_x + (j + 1)])
    else:
        if start_A_x - start_L_x > 0:
            for i in range(abs(start_A_y - start_L_y) - 1):
                min_day_list.append(time[start_A_y + (i + 1)][start_A_x])
            for j in range(abs(start_A_x - start_L_x) - 1):
                min_day_list.append(time[start_A_y][start_A_x - (j + 1)])
        else:
            for i in range(abs(start_A_y - start_L_y) - 1):
                min_day_list.append(time[start_A_y + (i + 1)][start_A_x])
            for j in range(abs(start_A_x - start_L_x) - 1):
                min_day_list.append(time[start_A_y][start_A_x + (j + 1)])
    min_day = max(min_day_list)
    print(min_day_list)
    queue = [[start_A_y, start_A_x]]
    time[start_A_y][start_A_x] = 1500
    read = [min_day]

    while queue:
        print(queue)
        print(min_day)
        pos = queue[0]
        del queue[0]

        for i in range(4):
            ny = pos[0] + dy[i]
            nx = pos[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if time[ny][nx] <= min_day and time[ny][nx] != 1500:
                    queue.append([ny, nx])
                    if time[ny][nx] == int:
                        time[ny][nx] = [time[ny][nx], time[pos[0]][pos[1]]]
                    else:
                        time[ny][nx] += [time[pos[0]][pos[1]]]

        if [pos[0], pos[1]] == [start_L_y, start_L_x]:
            if min_day > time[pos[0]][pos[1]]:
                min_day = time[pos[0]][pos[1]]
                read.append(min_day)

        time[pos[0]][pos[1]] = 1500

        for i in time:
            print(i)

    return min(read)

def swan_lake(N, M, maps, Day):
    for i in range(N): # 백조 구별 및 위치 확인
        for j in range(M):
            if
            elif maps[i][j] == "L":
                swan.append((i, j))


    time[swan[0][0]][swan[0][1]] = time[swan[1][0]][swan[1][1]] = 1
    melt_set = BFS(swan[0][0], swan[0][1], dy, dx, Day) | BFS(swan[1][0], swan[1][1], dy, dx, Day)
    new_melting = set([])
    Day += 1
    for i in time:
        print(i)
    print(" --------------------------------------------")
    while melt_set:

        for i, j in melt_set:
            new_melting.update(BFS(i, j, dy, dx, Day))

        Day += 1
        melt_set = new_melting
        new_melting = set([])

    for i in time:
        print(i)
    print("-----------------------------------------------")

    answer = BFS_find(swan[0][0], swan[0][1], swan[1][0], swan[1][1], dy, dx) - 1

    return answer

print(swan_lake(N, M, maps, Day))

# Ver_6_ 미완
import sys

input = sys.stdin.readline

N,M = map(int, input().split())
maps = [list(input().strip()) for _ in range(N)]

# 해당 위치가 몇 초 후에 전부 녹는지 저장한 배열
time = [[0] * M for _ in range(N)]
visit = [False for _ in range(M)] for _ in range(N)
swan = []
Day = 2
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# BFS
def BFS(start_y, start_x, dy, dx, Day):
    changing_set = set([])
    queue = [[start_y, start_x]]

    while queue:
        maps[start_y][start_x] = "."
        pos = queue[0]
        del queue[0]

        for i in range(4):
            ny = pos[0] + dy[i]
            nx = pos[1] + dx[i]
            if 0 <= ny < N  and 0 <= nx < M:
                if maps[ny][nx] == ".":
                    if time[ny][nx] == 0:
                        time[ny][nx] = 1
                        queue.append([ny, nx])
                else:
                    time[ny][nx] = Day + 1
                    changing_set.add((ny, nx))
                    maps[ny][nx] = "."

    return changing_set

def BFS_find(start_A_y, start_A_x, start_L_y, start_L_x, dy, dx):
    min_day_list = []
    if start_A_y - start_L_y > 0:
        if start_A_x - start_L_x > 0:
            for i in range(abs(start_A_y - start_L_y) - 1):
                min_day_list.append(time[start_A_y - (i + 1)][start_A_x])
                print(min_day_list)
            for j in range(abs(start_A_x - start_L_x) - 1):
                min_day_list.append(time[start_A_y][start_A_x - (j + 1)])
                print(min_day_list)
        else:
            for i in range(abs(start_A_y - start_L_y) - 1):
                min_day_list.append(time[start_A_y - (i +1)][start_A_x])
            for j in range(abs(start_A_x - start_L_x)):
                min_day_list.append(time[start_A_y][start_A_x + (j + 1)])
    else:
        if start_A_x - start_L_x > 0:
            for i in range(abs(start_A_y - start_L_y) - 1):
                min_day_list.append(time[start_A_y + (i + 1)][start_A_x])
            for j in range(abs(start_A_x - start_L_x) - 1):
                min_day_list.append(time[start_A_y][start_A_x - (j + 1)])
        else:
            for i in range(abs(start_A_y - start_L_y) - 1):
                min_day_list.append(time[start_A_y + (i + 1)][start_A_x])
            for j in range(abs(start_A_x - start_L_x) - 1):
                min_day_list.append(time[start_A_y][start_A_x + (j + 1)])
    min_day = max(min_day_list)
    print(min_day_list)
    queue = [[start_A_y, start_A_x]]
    time[start_A_y][start_A_x] = 1500
    read = [min_day]

    while queue:
        print(queue)
        print(min_day)
        pos = queue[0]
        del queue[0]

        for i in range(4):
            ny = pos[0] + dy[i]
            nx = pos[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if time[ny][nx] <= min_day and time[ny][nx] != 1500:
                    queue.append([ny, nx])
                    if time[ny][nx] == int:
                        time[ny][nx] = [time[ny][nx], time[pos[0]][pos[1]]]
                    else:
                        time[ny][nx] += [time[pos[0]][pos[1]]]

        if [pos[0], pos[1]] == [start_L_y, start_L_x]:
            if min_day > time[pos[0]][pos[1]]:
                min_day = time[pos[0]][pos[1]]
                read.append(min_day)

        time[pos[0]][pos[1]] = 1500

        for i in time:
            print(i)

    return min(read)

def swan_lake(N, M, maps, Day):
    for i in range(N): # 백조 구별 및 위치 확인
        for j in range(M):
            if maps[i][j] == "L" or maps[i][j] == '.':
                swan.append((i, j))
                if len((swan)) == 2:
                    break

    time[swan[0][0]][swan[0][1]] = time[swan[1][0]][swan[1][1]] = 1
    melt_set = BFS(swan[0][0], swan[0][1], dy, dx, Day) | BFS(swan[1][0], swan[1][1], dy, dx, Day)
    new_melting = set([])
    Day += 1
    for i in time:
        print(i)
    print(" --------------------------------------------")
    while melt_set:

        for i, j in melt_set:
            new_melting.update(BFS(i, j, dy, dx, Day))

        Day += 1
        melt_set = new_melting
        new_melting = set([])

    for i in time:
        print(i)
    print("-----------------------------------------------")

    answer = BFS_find(swan[0][0], swan[0][1], swan[1][0], swan[1][1], dy, dx) - 1

    return answer

print(swan_lake(N, M, maps, Day))

# # Ver_5
# import copy
# import sys
#
# input = sys.stdin.readline
#
# N,M = map(int, input().split())
# maps = [list(input().strip()) for _ in range(N)]
# swan = []
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# for i in maps:
#     print(i)
# for i in visit:
#     print(i)
#
#
# # BFS
# def BFS(start_y, start_x, dx, dy):
#     changing_set = set([])
#     queue = [[start_y, start_x]]
#     visit[start_y][start_x] += 1
#
#     while queue:
#         maps[start_y][start_x] = "."
#         pos = queue[0]
#         del queue[0]
#
#         for i in range(4):
#             nx = pos[0] + dx[i]
#             ny = pos[1] + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if maps[nx][ny] == ".":
#                     if visit[nx][ny] == 0: # visit_find[nx][ny] > visit_find[pos[0]][pos[0]] + 1
#                         visit[nx][ny] = visit[pos[0]][pos[0]] + 1
#                         queue.append([nx, ny])
#                 else:
#                     changing_set.add((nx, ny))
#                     maps[nx][ny] = "."
#
#     return changing_set
#
# def BFS_find(new_melting, find_set, start_x, start_y, dx, dy):
#     queue = [[start_x, start_y]]
#     visit_find = copy.deepcopy(visit)
#     visit_find[start_x][start_y] += 1
#
#     while queue:
#         pos = queue[0]
#         del queue[0]
#
#         for i in range(4):
#             nx = pos[0] + dx[i]
#             ny = pos[1] + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if maps[nx][ny] == ".":
#                     if visit_find[nx][ny] == 0: # visit_find[nx][ny] > visit_find[pos[0]][pos[0]] + 1
#                         visit_find[nx][ny] = visit_find[pos[0]][pos[0]] + 1
#                         queue.append([nx, ny])
#                         find_set.add((nx, ny))
#                 else:
#                     new_melting.add((nx, ny))
#                     maps[nx][ny] = "."
#
# def swan_lake(N, M, maps):
#     for i in range(N): # 백조 구별 및 위치 확인
#         for j in range(M):
#             if maps[i][j] == "L":
#                 swan.append((i, j))
#                 if len((swan)) == 2:
#                     break
#
#     find_set = set([])
#     melt_list = [BFS(swan[0][0], swan[0][1], dx, dy), BFS(swan[1][0], swan[1][1], dx, dy)]
#     new_melting = set([])
#     day = 1
#     A = set(["dummy"])
#     L = set(["dummy"])
#
#     while A & L:
#         new_melting_list = []
#         for i, j in melt_list[0]:
#             BFS_find(new_melting, find_set, i, j, dx, dy)
#         A = find_set
#         new_melting_list.append(new_melting)
#         find_set = set([])
#         for i, j in melt_list[1]:
#             BFS_find(new_melting, find_set, i, j, dx, dy)
#         L = find_set
#         find_set = set([])
#         new_melting_list.append(new_melting)
#
#         melt_list = new_melting_list
#         day += 1
#
#         for i in maps:
#             print(i)
#         for i in visit:
#             print(i)
#
#     return day
#
# print(swan_lake(N, M, maps))

# # Ver_5
# import copy
# import sys
# from typing import List, Any, Set
#
# input = sys.stdin.readline
#
# N,M = map(int, input().split())
# maps = [list(input().strip()) for _ in range(N)]
# visit = [[0] * M for _ in range(N)]
# swan = []
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# # BFS
# def BFS(start_y: int, start_x: int, dx: List[int], dy: List[int]) -> Set[list[int | Any] | Any]:
#     changing_set = set([])
#     queue = [[start_y, start_x]]
#     visit[start_y][start_x] += 1
#
#     while queue:
#         maps[start_y][start_x] = "."
#         pos = queue[0]
#         del queue[0]
#
#         for i in range(4):
#             nx = pos[0] + dx[i]
#             ny = pos[1] + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if maps[nx][ny] == ".":
#                     if visit[nx][ny] == 0 or visit[nx][ny] > visit[pos[0]][pos[0]] + 1:
#                         visit[nx][ny] = visit[pos[0]][pos[0]] + 1
#                         queue.append([nx, ny])
#                 else:
#                     changing_set.add((nx, ny))
#                     maps[nx][ny] = "."
#
#     return changing_set
#
# def BFS_find(new_melting: set, find_set: set, start_x: int, start_y: int, dx: List[int], dy: List[int]):
#     queue = [[start_x, start_y]]
#     visit_find = copy.deepcopy(visit)
#     visit_find[start_x][start_y] += 1
#
#     while queue:
#         pos = queue[0]
#         del queue[0]
#
#         for i in range(4):
#             nx = pos[0] + dx[i]
#             ny = pos[1] + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if maps[nx][ny] == ".":
#                     if visit_find[nx][ny] == 0 or visit_find[nx][ny] > visit_find[pos[0]][pos[0]] + 1:
#                         visit_find[nx][ny] = visit_find[pos[0]][pos[0]] + 1
#                         queue.append([nx, ny])
#                         find_set.add((nx, ny))
#                 else:
#                     new_melting.add((nx, ny))
#                     maps[nx][ny] = "."
#
# def swan_lake(N: int, M: int, maps: List[List[str]]) -> int:
#     for i in range(N): # 백조 구별 및 위치 확인
#         for j in range(M):
#             if maps[i][j] == "L":
#                 swan.append((i, j))
#                 if len((swan)) == 2:
#                     break
#
#     find_set = set([])
#     melt_list = [BFS(swan[0][0], swan[0][1], dx, dy), BFS(swan[1][0], swan[1][1], dx, dy)]
#     new_melting = set([])
#     day = 1
#     A = set(["dummy"])
#     L = set(["dummy"])
#
#     while A & L:
#         new_melting_list = []
#         for i, j in melt_list[0]:
#             BFS_find(new_melting, find_set, i, j, dx, dy)
#         A = find_set
#         new_melting_list.append(new_melting)
#         find_set = set([])
#         for i, j in melt_list[1]:
#             BFS_find(new_melting, find_set, i, j, dx, dy)
#         L = find_set
#         find_set = set([])
#         new_melting_list.append(new_melting)
#
#         melt_list = new_melting_list
#         day += 1
#
#     return day
#
# print(swan_lake(N, M, maps))

# # Ver_4
#
# import sys
# from typing import List
#
# input = sys.stdin.readline
#
# N,M = map(int, input().split())
# maps = [list(input().strip()) for _ in range(N)]
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# # BFS
# def BFS(start_x: int, start_y: int, dx: List[int], dy: List[int]) -> List[List[int]]:
#     changing_list = []
#     queue = [[start_x, start_y]]
#
#     while queue:
#         pos = queue[0]
#         del queue[0]
#
#         for i in range(4):
#             nx = pos[0] + dx[i]
#             ny = pos[1] + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if maps[nx][ny] == ".":
#                     maps[nx][ny] = "L"
#                     queue.append([nx, ny])
#                 elif maps[nx][ny] == "X" and changing_list.count([nx, ny]) == 0:
#                     changing_list.append([nx, ny])
#
#     return changing_list
#
# def swan_lake(N: int, M: int, maps: List[List[str]]) -> int:
#     dummy = 0
#     for j in range(N): # 백조 구별 및 위치 확인
#         try:
#             a = maps[j].index("L")
#             if dummy == 0:
#                 swan_A_row = j
#                 swan_A_column = a
#                 dummy += 1
#             else:
#                 swan_L_row = j
#                 swan_L_column = a
#                 break
#         except:
#             pass
#
#     melt_list = [BFS(swan_A_row, swan_A_column, dx, dy), BFS(swan_L_row, swan_L_column, dx, dy)]
#     day = 1
#
#     for d in range(max(N, M)):
#         for q in range(2):
#             for i, j in melt_list[q]:
#                 maps[i][j] = "L"
#
#         for i, j in melt_list[0]:
#             for z, r in melt_list[1]:
#                 if 0 <= abs(i - z) + abs(j - r) <= 1:
#                     return day
#
#         for q in range(2):
#             for i, j in melt_list[q]:
#                 melt_list[q] = BFS(i, j, dx, dy)
#
#         day += 1
#
# print(swan_lake(N, M, maps))

# # Ver_3
#
# import sys
# from typing import List
#
# input = sys.stdin.readline
#
# N,M = map(int, input().split())
# maps = [list(input().strip()) for _ in range(N)]
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# # BFS
# def BFS(start_x: int, start_y: int, dx: List[int], dy: List[int]) -> List[List[int]]:
#     melt_list = []
#     queue = [[start_x, start_y]]
#
#     while queue:
#         pos = queue[0]
#         del queue[0]
#
#         for i in range(4):
#             nx = pos[0] + dx[i]
#             ny = pos[1] + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 match maps[nx][ny]:
#                     case ".":
#                         queue.append([nx, ny])
#                         maps[nx][ny] = "L"
#                     case "X":
#                         melt_list.append([nx, ny])
#                         maps[nx][ny] = "L"
#
#     return melt_list
#
# def swan_lake(N: int, M: int, maps: List[List[str]]) -> int:
#     dummy = 0
#     for j in range(N): # 백조 구별 및 위치 확인
#         try:
#             a = maps[j].index("L")
#             if dummy == 0:
#                 swan_A_row = j
#                 swan_A_column = a
#                 dummy += 1
#             else:
#                 swan_L_row = j
#                 swan_L_column = a
#                 break
#         except:
#             pass
#
#     A = BFS(swan_A_row, swan_A_column, dx, dy)
#     L = BFS(swan_L_row, swan_L_column, dx, dy)
#     day = 1
#
#     for d in range(max(N, M)):
#         for i, j in A:
#             for z, r in L:
#                 if 0 <= abs(i - z) + abs(j - r) <= 1:
#                     return day
#
#         melt_list_new = []
#         for i, j in A:
#             for z in range(4):
#                 nx = i + dx[z]
#                 ny = j + dy[z]
#                 if 0 <= nx < N and 0 <= ny < M:
#                     match maps[nx][ny]:
#                         case "X":
#                             maps[nx][ny] = "."
#                             melt_list_new.append([nx, ny])
#                         case ".":
#                             melt_list_new += BFS(nx, ny, dx, dy)
#
#         A = melt_list_new
#         melt_list_new.clear()
#
#         for i, j in L:
#             for z in range(4):
#                 nx = i + dx[z]
#                 ny = j + dy[z]
#                 if 0 <= nx < N and 0 <= ny < M:
#                     match maps[nx][ny]:
#                         case "X":
#                             maps[nx][ny] = "."
#                             melt_list_new.append([nx, ny])
#                         case ".":
#                             melt_list_new += BFS(nx, ny, dx, dy)
#
#         L = melt_list_new
#         melt_list_new.clear()
#         day += 1
#
# print(swan_lake(N, M, maps))


# # Ver_3
#
# import sys
# from typing import List
#
# input = sys.stdin.readline
#
# N,M = map(int, input().split())
# maps = [list(input().strip()) for _ in range(N)]
#
# # BFS
# def BFS(start_x: int, start_y: int) -> List[List[int]]:
#     visit = [[0] * M for _ in range(N)]
#     changing_list = []
#
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#
#     visit[start_x][start_y] = 1
#     queue = [[start_x, start_y]]
#
#     while queue:
#         pos = queue[0]
#         del queue[0]
#
#         for i in range(4):
#             nx = pos[0] + dx[i]
#             ny = pos[1] + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if maps[nx][ny] != "X":
#                     if visit[nx][ny] == 0 or visit[nx][ny] > visit[pos[0]][pos[1]] + 1:
#                         visit[nx][ny] = visit[pos[0]][pos[1]] + 1
#                         queue.append([nx, ny])
#                 else:
#                     changing_list.append([nx, ny])
#
#     return changing_list
#
# def swan_lake(N: int, M: int, maps: List[List[str]]) -> int:
#     dummy = 0
#     for j in range(N): # 백조 구별 및 위치 확인
#         try:
#             a = maps[j].index("L")
#             if dummy == 0:
#                 maps[j][a] = "A"
#                 swan_A_row = j
#                 swan_A_column = a
#                 dummy += 1
#             else:
#                 swan_L_row = j
#                 swan_L_column = a
#                 break
#         except:
#             pass
#
#     A = BFS(swan_A_row, swan_A_column)
#     L = BFS(swan_L_row, swan_L_column)
#
#     answer = 3000 # 1 ≤ R, C ≤ 1500
#
#     for i, j in A: # 얼음 -> 백조
#         for z, r in L:
#             if answer > abs(i - z) + abs(j - r):
#                 answer = abs(i - z) + abs(j - r)
#
#     if answer % 2 == 1:
#         return answer // 2 + answer % 2
#     else:
#         return answer // 2 + answer % 2 + 1
#
# print(swan_lake(N, M, maps))


# Ver_2

# import sys
# from typing import List
#
# sys.setrecursionlimit(10**6)
#
# input = sys.stdin.readline
#
# N,M = map(int, input().split())
# maps = [list(input().strip()) for _ in range(N)]
#
# def recursive_function(swan: str, N: int, M: int, row: int, column: int):
#     dummy = 0
#
#     if row + 1 <= N - 1:
#         if maps[row + 1][column] == ".":
#             maps[row + 1][column] = swan
#             recursive_function(swan, N, M, row + 1, column)
#         elif maps[row + 1][column] == "X":
#             dummy += 1
#     else:
#         dummy += 1
#
#     if row - 1 >= 0:
#         if maps[row - 1][column] == ".":
#             maps[row - 1][column] = swan
#             recursive_function(swan, N, M, row - 1, column)
#         elif maps[row - 1][column] == "X":
#             dummy += 1
#     else:
#         dummy += 1
#
#     if column + 1 <= M - 1:
#         if maps[row][column + 1] == ".":
#             maps[row][column + 1] = swan
#             recursive_function(swan, N, M, row, column + 1)
#         elif maps[row][column + 1] == "X":
#             dummy += 1
#     else:
#         dummy += 1
#
#     if column - 1 >= 0:
#         if maps[row][column - 1] == ".":
#             maps[row][column - 1] = swan
#             recursive_function(swan, N, M, row, column - 1)
#         elif maps[row][column - 1] == "X":
#             dummy += 1
#     else:
#         dummy += 1
#
#     if dummy >= 1:
#         return
#
#
# def swan_lake(N: int, M: int, maps: List[List[str]]) -> int:
#     dummy = 0
#     for j in range(N): # 백조 구별 및 위치 확인
#         try:
#             a = maps[j].index("L")
#             if dummy == 0:
#                 maps[j][a] = "A"
#                 swan_A_row = j
#                 swan_A_column = a
#                 dummy += 1
#             else:
#                 swan_L_row = j
#                 swan_L_column = a
#                 break
#         except:
#             pass
#
#     recursive_function("A", N, M, swan_A_row, swan_A_column)
#     recursive_function("L", N, M, swan_L_row, swan_L_column)
#
#     changing_list_A = []
#     changing_list_L = []
#     for j in range(N):
#         for z in range(M):
#             if maps[j][z] == "X":
#                 if j + 1 < N:
#                     if maps[j + 1][z] == "A":
#                         changing_list_A.append([j, z])
#                         continue
#                     elif maps[j + 1][z] == "L":
#                         changing_list_L.append([j, z])
#                         continue
#                 if j - 1 >= 0:
#                     if maps[j - 1][z] == "A":
#                         changing_list_A.append([j, z])
#                         continue
#                     elif maps[j - 1][z] == "L":
#                         changing_list_L.append([j, z])
#                         continue
#                 if z + 1 < M:
#                     if maps[j][z + 1] == "A":
#                         changing_list_A.append([j, z])
#                         continue
#                     elif maps[j][z + 1] == "L":
#                         changing_list_L.append([j, z])
#                         continue
#                 if z - 1 >= 0:
#                     if maps[j][z - 1] == "A":
#                         changing_list_A.append([j, z])
#                         continue
#                     elif maps[j][z - 1] == "L":
#                         changing_list_L.append([j, z])
#                         continue
#
#     answer = 3000 # 1 ≤ R, C ≤ 1500
#
#     for i, j in changing_list_A: # 얼음 -> 백조
#         for z, r in changing_list_L:
#             if answer > abs(i - z) + abs(j - r):
#                 answer = abs(i - z) + abs(j - r)
#
#     if answer % 2 == 1:
#         return answer // 2 + answer % 2
#     else:
#         return answer // 2 + answer % 2 +1
#
# print(swan_lake(N, M, maps))


# Ver_1
#
# import sys
# from typing import List
#
# sys.setrecursionlimit(10**6)
#
# input = sys.stdin.readline
#
# N,M = map(int, input().split())
# maps = [list(input().strip()) for _ in range(N)]
#
# def recursive_function(swan: str, N: int, M: int, row: int, column: int):
#     test = 0
#
#     if row + 1 <= N - 1:
#         if maps[row + 1][column] == ".":
#             maps[row + 1][column] = swan
#             recursive_function(swan, N, M, row + 1, column)
#         elif maps[row + 1][column] == "X":
#             test += 1
#     else:
#         test += 1
#
#     if row - 1 >= 0:
#         if maps[row - 1][column] == ".":
#             maps[row - 1][column] = swan
#             recursive_function(swan, N, M, row - 1, column)
#         elif maps[row - 1][column] == "X":
#             test += 1
#     else:
#         test += 1
#
#     if column + 1 <= M - 1:
#         if maps[row][column + 1] == ".":
#             maps[row][column + 1] = swan
#             recursive_function(swan, N, M, row, column + 1)
#         elif maps[row][column + 1] == "X":
#             test += 1
#     else:
#         test += 1
#
#     if column - 1 >= 0:
#         if maps[row][column - 1] == ".":
#             maps[row][column - 1] = swan
#             recursive_function(swan, N, M, row, column - 1)
#         elif maps[row][column - 1] == "X":
#             test += 1
#     else:
#         test += 1
#
#     if test >= 1:
#         return
#
#
#
# def swan_lake(N: int, M: int, maps: List[List[str]]) -> int:
#     dummy = 0
#     for j in range(N): # 백조 구별 및 위치 확인
#         try:
#             a = maps[j].index("L")
#             if dummy == 0:
#                 maps[j][a] = "A"
#                 swan_A_row = j
#                 swan_A_column = a
#                 dummy += 1
#             else:
#                 swan_L_row = j
#                 swan_L_column = a
#                 break
#         except:
#             pass
#
#     recursive_function("A", N, M, swan_A_row, swan_A_column)
#     recursive_function("L", N, M, swan_L_row, swan_L_column)
#
#     for i in range(max(N, M)):  # 얼음이 다 녹는 최대 일수만큼 반복
#         for j in range(N):
#             for z in range(M):
#                 dummy_list = []
#                 if maps[j][z] == "A":
#                     if j + 1 < N:
#                         dummy_list.append(maps[j + 1][z])
#                     if j - 1 >= 0:
#                         dummy_list.append(maps[j - 1][z])
#                     if z + 1 < M:
#                         dummy_list.append(maps[j][z + 1])
#                     if z - 1 >= 0:
#                         dummy_list.append(maps[j][z - 1])
#
#                     if dummy_list.count("L") >= 1:
#                         return i
#
#                 elif maps[j][z] == "L":
#                     if j + 1 < N:
#                         dummy_list.append(maps[j + 1][z])
#                     if j - 1 >= 0:
#                         dummy_list.append(maps[j - 1][z])
#                     if z + 1 < M:
#                         dummy_list.append(maps[j][z + 1])
#                     if z - 1 >= 0:
#                         dummy_list.append(maps[j][z - 1])
#
#                     if dummy_list.count("A") >= 1:
#                         return i
#
#                 dummy_list.clear()
#
#         changing_list_A = []
#         changing_list_L = []
#         for j in range(N):
#             for z in range(M):
#                 dummy_list = []
#                 if maps[j][z] == "X":
#                     if j + 1 < N:
#                         dummy_list.append(maps[j + 1][z])
#                     if j - 1 >= 0:
#                         dummy_list.append(maps[j - 1][z])
#                     if z + 1 < M:
#                         dummy_list.append(maps[j][z + 1])
#                     if z - 1 >= 0:
#                         dummy_list.append(maps[j][z - 1])
#
#                     if dummy_list.count("A") >= 1:
#                         changing_list_A.append([j, z])
#                     elif dummy_list.count("L") >= 1:
#                         changing_list_L.append([j, z])
#                 dummy_list.clear()
#
#         for i, j in changing_list_A:
#             maps[i][j] = "A"
#         for i, j in changing_list_L:
#             maps[i][j] = "L"
#
# print(swan_lake(N, M, maps))