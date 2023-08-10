"""

문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/12938

"""
# 1.
from itertools import combinations_with_replacement as H

def solution(n, s): return [-1] if n>s else sorted(max([list(x) for x in H(range(1, s), n) if sum(x) == s], key = lambda a: eval("*".join([str(n) for n in a]))))

def solution(n, s):
    if n>s: return [-1]
    else:
        list = [s//n for x in range(n)]
        for i in range(s%n):
            list[-(i+1)] = s//n + 1
        return list

def solution(n, s): return [-1] if n>s else [s//n]*(n-s%n)+[s//n+1]*(s%n)

solution(2,9)

print(solution(2,9))
