'''

https://www.acmicpc.net/problem/1509

'''

import sys
from collections import defaultdict

input = sys.stdin.readline

pal_str = input().strip()
bump = [0]*len(pal_str) # True/False 덤프
palindrome = []

pal_str_dict = defaultdict(int)

for key in pal_str:


# for i in pal_str:
#     '''
#     만약, i, j가 같다면 for문을 종료하고 다른 포인터를 움직임.
#     '''
#     for j in pal_str:
#         if i != j: continue
#         else:
#             break


print(len(palindrome))
