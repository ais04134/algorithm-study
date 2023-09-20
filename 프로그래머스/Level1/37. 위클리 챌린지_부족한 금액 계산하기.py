'''

https://programmers.co.kr/learn/courses/30/lessons/82612

'''

def solution(price, money, count):
    answer = money
    for i in range(count):
        answer -= (i+1)*price
    if answer >= 0: return 0
    else: return abs(answer)