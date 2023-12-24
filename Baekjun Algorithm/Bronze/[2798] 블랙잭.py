import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))

card_three_sum = list(map(sum, combinations(card, 3)))

print(max(filter(lambda x: M - x >= 0, card_three_sum)))