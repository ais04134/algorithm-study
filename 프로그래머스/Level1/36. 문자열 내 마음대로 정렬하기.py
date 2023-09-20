'''

https://programmers.co.kr/learn/courses/30/lessons/12915

'''

strings = ["cdx", "abce", "abcd"]
n = 2

# def solution(strings, n): return sorted(strings, key = lambda x: (x[n], x))
# x[n]으로 정렬하고 x[n]이 같을 경우 x를 기준으로 정렬하였다.  별표 5

def solution(strings, n):
    strings.sort()
    answer=sorted(strings, key=lambda string: string[n])
    return answer # 아...문제를 잘못 이해해서 이렇게 하면 되는걸 삽질했네..


print(solution(strings, n))