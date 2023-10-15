"""
출처: https://www.acmicpc.net/problem/2798
"""

'''
Input
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card_num = list(map(int, input().split()))


'''
코드
'''

from itertools import combinations

def 블랙잭(N: int, M: int, card_num: list) -> int:
    블랙잭_조합_합 = list(map(sum, combinations(card_num, 3)))

    return


