'''

문제: https://www.acmicpc.net/problem/16572

'''

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# p = [list(map(int, input().split())) for _ in range(N)]
#
# # var-1
# def triangles(x):
#     tri = []
#     for i in range(1, x[2] + 1):
#         for j in range(i):
#             tri.append((x[0] + x[2] - i, x[1] + j))
#
#     return tri
#
# all_pixel = len(set(sum(list(map(triangles, p)), [])))
#
# print(all_pixel)
#
# # var-2
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# print(len(set(sum(list(map(lambda x: [[(x[0] + x[2] - i, x[1] + j) for j in range(i)] for i in range(1, x[2] + 1)], [list(map(int, input().split())) for _ in range(N)])), []))))

# var-3
import sys
input = sys.stdin.readline
N = 2001
n = int(input())
arr = [[0] * N for _ in range(N)]
ans =0
def triangles(x):
    global ans
    for i in range(1, x[2] + 1):
        for j in range(i):
            if arr[x[0] + x[2] - i][x[1] + j] == 0:
                arr[x[0] + x[2] - i][x[1] + j] = 1
                ans += 1
            else:
                break
list(map(triangles, [list(map(int, input().split())) for _ in range(n)]))
print(ans)

import sys
input = sys.stdin.readline

N = 2001
arr = [[0] * N for _ in range(N)]
ans = 0

for i in range(int(input())):
    a, b, c = map(int, input().split())
    if arr[a][b] < c: arr[a][b] = c

    