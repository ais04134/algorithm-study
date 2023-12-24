"""

문제 출처: https://www.acmicpc.net/problem/10163

<test case>
4
0 2 10 10
7 9 8 4
8 4 10 6
6 0 12 10

"""
import sys
input = sys.stdin.readline

N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]

for i in p:
    clash = list(filter(lambda x: 0 < min(i[0]+i[2], x[0]+x[2]) - max(i[0], x[0]) and 0 < min(i[1]+i[3], x[1]+x[3]) - max(i[1], x[1]), p[p.index(i)+1:]))
    if clash != []:
        clash = list(map(lambda x: (max(x[0], i[0]), min(x[0]+x[2], i[0]+i[2]), max(x[1], i[1]), min(x[1]+x[3], i[1]+i[3])), clash))
        reference_coordinates = sorted(sum([[(i[0], i[2], i[3], 0), (i[1], i[2], i[3], 1)] for i in clash], []), key= lambda x: (x[0], x[1])) # (x, y1, y2, 0: 시작 and 1: 끝)
        sum_area = 0
        y = 0
        print(reference_coordinates)
        for j in range(len(reference_coordinates)):
            if reference_coordinates[j][3] == 0: # 시작
                if 0 <= j - 1:
                    if reference_coordinates[j][0] != reference_coordinates[j-1][0]:
                        sum_area+= (reference_coordinates[j][0] - reference_coordinates[j-1][0])*y
                        y += reference_coordinates[j][2] - reference_coordinates[j][1]
                    else: # 중복되는 y 구간이 있느냐?
                        if min(reference_coordinates[j][2], reference_coordinates[j-1][2]) - max(reference_coordinates[j][1], reference_coordinates[j-1][1]) > 0:
                            y += reference_coordinates[j][2] - reference_coordinates[j][1] - (min(reference_coordinates[j][2], reference_coordinates[j-1][2]) - max(reference_coordinates[j][1], reference_coordinates[j-1][1]))
                        else:
                            y += reference_coordinates[j][2] - reference_coordinates[j][1]
                else:
                    y += reference_coordinates[j][2] - reference_coordinates[j][1]
            else:
                # if 0 <= j - 1:
                if reference_coordinates[j][0] != reference_coordinates[j-1][0]:
                    sum_area += (reference_coordinates[j][0] - reference_coordinates[j-1][0])*y
                    y -= reference_coordinates[j][2] - reference_coordinates[j][1]
                else: # 중복되는 y 구간이 있느냐?
                    if min(reference_coordinates[j][2], reference_coordinates[j-1][2]) - max(reference_coordinates[j][1], reference_coordinates[j-1][1]) > 0:
                        y -= reference_coordinates[j][2] - reference_coordinates[j][1] - (min(reference_coordinates[j][2], reference_coordinates[j-1][2]) - max(reference_coordinates[j][1], reference_coordinates[j-1][1]))
                    else:
                        y -= reference_coordinates[j][2] - reference_coordinates[j][1]

        print(i[2]*i[3] - sum_area)
    else:
        print(i[2]*i[3])


                    # for j in reference_coordinates:


import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
queries, line_x, line_y = [], set(), set()

for _ in range(N):
	q = list(map(int, input().split()))
	x1, y1, x2, y2 = q[0], q[1], q[0] + q[2], q[1] + q[3]
	queries.append((x1, y1, x2, y2))
	line_x.add(x1)
	line_x.add(x2)
	line_y.add(y1)
	line_y.add(y2)

line_x = sorted(line_x)
line_y = sorted(line_y)
comp_x = {v: i for i, v in enumerate(line_x)}
comp_y = {v: i for i, v in enumerate(line_y)}
dx = [line_x[i] - line_x[i - 1] for i in range(1, len(line_x))]
dy = [line_y[i] - line_y[i - 1] for i in range(1, len(line_y))]

paper = [[0] * len(dx) for _ in range(len(dy))]

for i in range(1, len(queries) + 1):
	x1, y1, x2, y2 = queries[i - 1]
	for x in range(comp_x[x1], comp_x[x2]):
		for y in range(comp_y[y1], comp_y[y2]):
			paper[y][x] = i

ans = [0] * (N + 1)
for y in range(len(paper)):
	for x in range(len(paper[0])):
		ans[paper[y][x]] += dx[x] * dy[y]

print('\n'.join(map(str, ans[1:])))


# 압축 안하고 브루트포스
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
#
# N = int(input())
# paper = [[0] * 1001 for _ in range(1001)]
# for n in range(1, N + 1):
# 	x, y, w, h = map(int, input().split())
# 	for i in range(y, y + h):
# 		for j in range(x, x + w):
# 			paper[i][j] = n
#
# ans = [0] * (N + 1)
# for line in paper:
# 	for p in line:
# 		ans[p] += 1
#
# print('\n'.join(map(str, ans[1:])))




