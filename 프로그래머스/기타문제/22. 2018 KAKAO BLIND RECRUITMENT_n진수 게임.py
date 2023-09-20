'''

문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3

'''
'''
1. n 진법으로 변환 함수 만들기
2. 돌아가는 횟수 만큼의 값들을 나열하고 그 값에 대해 for 문 돌릴 수 있도록 만들기
3. for 문 돌아가면서 미루 구할 숫자를 더하기

'''


def _10toN(num, n): # num 숫자가 들어오면 n 진수로 변환 해주는 함수
    n_dic = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
        13: 'D', 14: 'E', 15: 'F'
    }
    result = ''
    q, r = divmod(num, n)

    while q > 0:
        result = n_dic[r] + result
        q, r = divmod(q,n)

    result = n_dic[r] + result
    return result


def solution(n, t, m, p):
    answer = ''
    number = ""
    for i in range(m*t):
        number += _10toN(i,n)
        if len(number) > m*t + p:
            break
    for i in range(len(number)):
        for j in range((len(number)//m)+1):
            if (i+1) == m*j+p:
                answer += number[i]
                if len(answer) == t: return answer