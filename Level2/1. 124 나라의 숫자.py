'''

문제 설명
124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

124 나라에는 자연수만 존재합니다.
124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

10진법	124 나라	10진법	124 나라
1	1	6	14
2	2	7	21
3	4	8	22
4	11	9	24
5	12	10	41
자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

제한사항
n은 500,000,000이하의 자연수 입니다.
입출력 예
n	result
1	1
2	2
3	4
4	11

'''

# 3진법으로 변환하고 012 -> 124 로 바꾸면 해결될 것 같다.
n = 4

def solution(n):
    if n <= 3: return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r] # 리스팩.... 반성하는 중

# 3진법으로 변환하고 012 -> 124 로 바꾸면 해결될 것 같다.
# def antilogarithm(n, q): # n의 정수값을 10진수 -> q진수로 변환하는 함수
#     rev_base = ''
#
#     while n > 0:
#         n, mod = divmod(n, q)
#         rev_base += str(mod)
#
#     return rev_base[::-1]
#
# def solution(n):
#     if n == 1: return "1"
#     subject_language = antilogarithm(n-1, 3)
#     subject_language = ",".join(subject_language).split(",")
#     for i in range(len(subject_language)):
#         if subject_language[i] == "0":
#             subject_language[i] = "1"
#         elif subject_language[i] == "1" and subject_language[0] != "1":
#             subject_language[i] = "2"
#         elif subject_language[i] == "2":
#             subject_language[i] = "4"
#     subject_language = "".join(subject_language)
#
#     return subject_language
#
# print(solution(n))

