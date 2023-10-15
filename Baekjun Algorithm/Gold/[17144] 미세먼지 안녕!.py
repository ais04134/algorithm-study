"""
출처: https://www.acmicpc.net/problem/17144
"""

'''
Input
'''

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split()) # R x C 격자, T: 수행 횟수
room = []

for i in range(R):
    room.append(list(map(int, input().split())))


'''
코드
'''
direction = [(-1,0),(1,0), (0,1), (0,-1)]

def 미세먼지_확산(A,x,y):
    '''
    :param A: 먼지량
    :param x: x 좌표
    :param y: y 좌표
    :return: 남아있는 먼지량
    '''
    count = 0 # 확산되는 공간 수
    for i in direction:
        if 0 <= x+i[0] <= R-1 and 0 <= y+i[1] <= C-1: # 범위 내 위치해 있으면.
            if room[x+i[0]][y+i[1]] != -1: # 청소기가 아니면!
                deum[x+i[0]][y+i[1]] += A // 5
                count += 1

    return A - (A // 5)*count

# for _ in range(T) # T번 수행
deum = [[0 for i in range(C)] for j in range(R)]

for i in range(R):
    for j in range(C):
        if room[i][j] != 0 and room[i][j] != -1:
            room[i][j] = 미세먼지_확산(room[i][j],i,j)

# room, deum 합하기
for i in range(R):
    for j in range(C):
        room[i][j] += deum[i][j]

c, d = 0, 0 # 앞뒤

for j in room[2]:






for i in range(R):
    print(deum[i])

print("---")

for i in range(R):
    print(room[i])









