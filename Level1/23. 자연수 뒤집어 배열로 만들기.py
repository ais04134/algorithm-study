'''

문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
입출력 예
n	return
12345	[5,4,3,2,1]

'''

n = 12314

def int_make(n):
    n = int(n)
    return n

def solution(n):
    n = ' '.join(str(n))
    answer = str(n).split()
    answer.reverse()

    return list(map(int_make,answer))



print(solution(n))

# 이런식으로 활용 가능하다. 바로 int가 되는 부분 그리고 reversed(str(n)) 이 부분도 잘 생각해보자
# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))