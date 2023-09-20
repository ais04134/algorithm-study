'''

문제출처: https://school.programmers.co.kr/learn/courses/30/lessons/92335#qna

'''

import math

# 소수 판별 함수
def is_prime_number(x):
    if x ==1: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return False
    return True

# 10 진수 -> k 진수 변환 함수
def launching(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]

solution=lambda n, k:len(list(filter(lambda x: x != '' and is_prime_number(int(x)), launching(n, k).split('0'))))


# def solution(n, k):
#     num_k_list = list(filter(lambda x: x != '', launching(n, k).split('0')))
#     answer = len(list(filter(lambda x: is_prime_number(int(x)), num_k_list)))
#     return answer
#
#
# print(solution(437674, 3))

