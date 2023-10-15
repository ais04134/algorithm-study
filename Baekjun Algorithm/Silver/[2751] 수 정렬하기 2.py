'''
출처: https://www.acmicpc.net/problem/2751
'''

'''
Input
'''

import sys
input = sys.stdin.readline

N = int(input())
list_len = [int(input()) for x in range(N)]


'''
풀이 코드
'''

list_len.sort()

for i in list_len:
    print(i)