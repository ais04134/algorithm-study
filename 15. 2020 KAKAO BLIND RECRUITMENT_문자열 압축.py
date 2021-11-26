# -*- coding: utf-8 -*-
'''

문제출처: https://programmers.co.kr/learn/courses/30/lessons/60057

'''
# 으어어 문제를 잘 못 이해하고 못 풀어버렸다..
s = "abcabcabcabcdededededede"

# def solution(s):
#     compressed_text_fragments = []
#
#     for i in range(len(s)):
#         if s[:i+1] == s[i+1:2*(i+1)]:
#             number_of_repetitions = 1
#
#             for j in range(len(s)//(len(s[:i+1])+i)):
#                 if s[:i+1] == s[(i+1)*(j+1):(i+1)*(j+2)]:
#                     number_of_repetitions += 1
#                 elif s[(i+1)*(j+1):(i+1)*(j+2)] == s[(i+1)*(j+2):(i+1)*(j+3)]:
#
#                 else:
#                     if number_of_repetitions == 1:
#                         compressed_text_fragments.append(s[:i+1] + s[(i+1) * (j+1):])
#                     else:
#                         compressed_text_fragments.append(str(number_of_repetitions) + s[:i+1] + s[(i+1) * (j+1):])
#
#     if compressed_text_fragments == []:
#         return len(s)
#
#     answer = min(list(map(len, compressed_text_fragments)))
#
#     return answer
#
# print(len("4abcdededededede"))
#
#
# print(solution(s))

# s = "abcabcabcabcdededededede"
s = "aaaakkaaaakkaaaakk"

# def solution(s: str)-> int:
#     answer = ""
#     number = 1
#     while True:
#         for i in range(len(s)//2):
#             if s[0:i+1] == s[i+1:2*(i+1)]:
#                 number += 1
#                 s = s[i+1:]
#                 if s[0:i+1] != s[i+1:2*(i+1)]:
#                     answer += f"{number}"+s[0:i+1]
#                     number = 1
#                     s = s[i+1:]
#                 break
#         if s == "":
#             return answer
#             break
#
#
# print(solution(s))

string = "kbdgbdgsdksdkkkk"

def solution(string: str)-> int:
    answer_list = []
    for i in range((len(string)//2)+1): # i개씩 자르는 경우들 n/2이상은 의미가 없다.# 문자열 길이가 1인 경우가 있을 수 있으므로 +1 해준다.
        number = 1
        s = string
        answer = ""
        for j in range((len(string))): # i개씩 문자열을 자르는 작업!
            if s[0:i + 1] == s[i + 1:2 * (i + 1)]: # 만약 자른 문자열이 이후 그마만큼의 문자열과 같을 경우
                number += 1
                s = s[i+1:]
            else: # 자른 문자열이 이후 문자열과 다를 경우
                if number == 1: # 반복이 없었을시 값 그대로 더하기
                    answer += s[0:i + 1]
                    s = s[i+1:]
                else: # 반복이 있었을시 반복 횟수만큼 숫자를 더한 후 값 더하기
                    answer += f"{number}" + s[0:i + 1]
                    s = s[i+1:]
                    number = 1

        answer_list.append(len(answer)) # i개씩 문자열을 잘랐을때의 결과값의 길이를 answer_list에 저장

    return min(answer_list) # 그중 최소값을 출력


print(solution(string))
