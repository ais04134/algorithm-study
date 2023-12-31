import sys
from collections import Counter

input = sys.stdin.readline

M = int(input())
card = list(map(int, input().split()))
N = int(input())
card_user = list(map(int, input().split()))

counts = Counter(card)

for i in range(len(card_user)):
    if card_user[i] in counts:
        print(counts[card_user[i]], end=' ')
    else:
        print(0, end=' ')


########################################################
# 풀이1
'''
코드는 간결하나, 시간 복잡도가 높음.
딕셔너리 형태로 수정해야될 것 같음.
'''
########################################################
# import sys

# input = sys.stdin.readline

# M = int(input())
# card = list(map(int, input().split()))
# N = int(input())
# card_user = list(map(int, input().split()))

# print(' '.join([str(card.count(i)) for i in card_user]))