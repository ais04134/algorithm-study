'''

문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.
입출력 예
s	n	result
"AB"	1	"BC"
"z"	1	"a"
"a B z"	4	"e F d"

'''

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# a b c d e f g h i j k l m n o p q r s t u v w x y z


# 딕셔너리 방식으로도 풀어보기
# uppercase_dictionary = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F',}
# lowercase dictionary

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'


def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if uppercase.find(s[i]) != -1:
            if uppercase.find(s[i]) + n > 25:
                x = uppercase.find(s[i]) + n - 26
                answer = answer + uppercase[x]
            else:
                x = uppercase.find(s[i]) + n
                answer = answer + uppercase[x]

        elif lowercase.find(s[i]) != -1:
            if lowercase.find(s[i]) + n > 25:
                x = lowercase.find(s[i]) + n - 26
                answer = answer + lowercase[x]
            else:
                x = lowercase.find(s[i]) + n
                answer = answer + lowercase[x]
        else:
            answer = answer + " "

    return answer

# 밑에 이 코드랑 내 코드랑 비교되는 점이 많다. 좀 더 효율적으로 코드를 작성할 수 있었던 부분들을 다시 생각해보자.

# def caesar(s, n):
#     lower_list = "abcdefghijklmnopqrstuvwxyz"
#     upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
#     result = []
#
#     for i in s:
#         if i is " ":
#             result.append(" ")
#         elif i.islower() is True:
#             new_ = lower_list.find(i) + n
#             result.append(lower_list[new_ % 26])
#         else:
#             new_ = upper_list.find(i) + n
#             result.append(upper_list[new_ % 26])
    # return "".join(result)

