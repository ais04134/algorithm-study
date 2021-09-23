'''

문제: https://programmers.co.kr/learn/courses/30/lessons/17684

'''


def solution(msg):
    answer = []
    # 딕셔너리 초기값
    dic = {}
    for i in range(26):
        dic[chr(ord('A') + i)] = i + 1

    i = 0
    while i < len(msg):
        j = i
        # 딕셔너리에 매칭되는 key가 없을 때까지
        while msg[i:j + 1] in dic.keys() and j < len(msg):
            j += 1
        if j == len(msg): break
        # 매칭된 문자열은 출력, 매칭 안된 문자열은 딕셔너리에 저장
        answer.append(dic[msg[i:j]])
        dic[msg[i:j + 1]] = len(dic) + 1
        i = j

    # 마지막 남은 문자열 출력
    answer.append(dic[msg[i:j]])
    return answer

# def solution(msg):
#     myDic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,27)))
#     answer = []
#
#     state = 1 # 1: ok. 2: add
#     while len(msg) > 0:
#         temp = -1
#         for j in range(1, len(msg)+1):
#             if list(myDic.keys()).count(msg[0:j]) != 0:
#                 temp = myDic[msg[0:j]]
#                 state = 1
#             else :
#                 # add to dictionary
#                 myDic[msg[0:j]] = len(myDic)+1
#                 state = 2
#                 break
#         answer += [temp]
#         if state == 2 :
#             msg = msg[j-1:]
#         else :
#             msg = ""
#     return answer


