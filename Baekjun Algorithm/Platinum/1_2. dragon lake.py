# import os, io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

import sys

input = sys.stdin.readline


R, C = map(int, input().split())
arr = [[9] * (C + 2) for _ in range(R + 2)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
sq, bq = [], []
day = 0

print(R)
print(C)

for r in range(1, R + 1):
    line = input().rstrip()

    print(line)
    for c, x in enumerate(line, start=1):
        print(c, x)
        if x == "X":
            arr[r][c] = 0
            bq.append((r, c))
        elif x == "L":
            arr[r][c] = 1
        else:
            arr[r][c] = 2
            sq.append((r, c))

arr[sq[1][0]][sq[1][1]] = 0

s2y, s2x = sq.pop()

while bq:
    new_sq, new_bq = [], []
    for y, x in sq:
        flag = 0
        for dy, dx in d:
            r, c = y + dy, x + dx
            if arr[r][c] == 0:
                arr[r][c] = 2
                sq.append((r, c))
                new_sq.append((y, x))
            elif arr[r][c] == 1 and not flag:
                flag = 1
    if arr[s2y][s2x] == 2: break

    for y, x in bq:
        for dy, dx in d:
            r, c = y + dy, x + dx
            if arr[r][c] == 1:
                arr[r][c] = 0
                new_bq.append((r, c))
    sq = new_sq
    bq = new_bq
    day += 1

print(day)