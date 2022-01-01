'''

https://programmers.co.kr/learn/courses/30/lessons/86491

'''

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    answer = [sorted(i) for i in sizes]
    width_max = max([i[0] for i in answer])
    length_max = max([i[1] for i in answer])
    return width_max*length_max

print(solution(sizes))