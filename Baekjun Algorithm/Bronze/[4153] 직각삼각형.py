import sys

input = sys.stdin.readline

while True:
    side_lengths = list(map(int, input().split()))
    if side_lengths[0] == 0:
        break
    side_lengths.sort()
    if side_lengths[2]**2 == side_lengths[1]**2 + side_lengths[0]**2: # 피타고라스 정리
        print('right')
    else:
        print('wrong')    