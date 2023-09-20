'''

https://programmers.co.kr/learn/courses/30/lessons/72411

'''

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for i in course:
        temp=[]
        for j in orders:
            combi = combinations(sorted(j),i)
            temp+=combi
        counter = Counter(temp)
        print(counter)
        if max(counter.values())>1:
            answer +=[''.join(x) for x in counter if counter[x]==max(counter.values())]
    return answer

print(solution(orders, course))
