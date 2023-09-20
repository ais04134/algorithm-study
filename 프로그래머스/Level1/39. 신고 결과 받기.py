'''

문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=python3

'''
from collections import Counter
from itertools import groupby

def solution(id_list, report, k):
    answer = []
    report = sorted(list(map(lambda x:x.split(), list(set(report)))), key=lambda x:x[0])
    report_s = list(map(lambda x:x[1], report)) # 신고자만 추출
    counter = dict(Counter(report_s))
    for i in range(len(report)):
        if counter.get(report[i][1]) >= k:
            report[i][1] = 1
        else:
            report[i][1] = 0
    group = groupby(report, lambda x: x[0])
    group_dict = {}
    for key, group in group:
        group_dict[key] = list(group)
    for i in id_list:
        if i in group_dict:
            answer.append(sum(list(map(lambda x: x[1], group_dict.get(i)))))
        else:
            answer.append(0)

    return answer