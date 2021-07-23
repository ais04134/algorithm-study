nums = [1,2,3,4]

import itertools

def is_prime_number(num):
    if num == 1 or num == 0:
        return False
    else:
        n = int(num ** 0.5)

        for i in range(2, n + 1):
            if num % i == 0:
                return False
        return True

def solution(nums):
    a = list(itertools.combinations((nums), 3))
    b = []
    answer = 0
    for i in a:
        b.insert(0, sum(i))
    for i in b:
        if is_prime_number(i) == False:
            answer += 1

    return answer

# 이런 식으로 생각 하는 편이 더 좋았을 것 같아..!

# from itertools import combinations
#
# def is_prime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True
#
# def solution(nums):
#     answer = 0
#
#     temp = list(combinations(nums, 3))
#     for i in temp:
#         if is_prime(sum(i)):
#             answer += 1
#     return answer
