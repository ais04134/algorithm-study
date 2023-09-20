'''

문제 설명
문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

제한 사항
str은 길이 1 이상인 문자열입니다.
입출력 예
s	return
"Zbcdefg"	"gfedcbZ"

'''

s = "ZbAcDdefg"

def solution(s):
    answer_list = sorted(list(s))
    answer_list.reverse()
    answer = ''
    for i in answer_list:
        answer = answer + i

    return answer

# def solution(s):
#     return ''.join(sorted(s, reverse=True)) # 문자열에서 .join을 이런식으로도 사용 가능하다.

'''----------------------------------------------------------------'''
## 밑에 코드는 문제를 착각해서..ㅋㅋㅋ 두개 코드에서 내가 잠깐 오해했던 부분 생각하고 넘어가자
def solution(s):
    answer_list = sorted(list(s))
    lowercase = ''
    uppercase = ''
    for i in answer_list:
        if i.islower() == False:
            uppercase = uppercase + i
        else:
            lowercase = lowercase + i
    answer = lowercase + uppercase

    return answer


# def solution(s):
#     answer_list = sorted(list(s))
#     answer = ''
#     lowercase = ''
#     uppercase = ''
#     for i in answer_list:
#         if answer_list[i].lower() == True:
#             uppercase = uppercase + answer_list[i]
#         else:
#             lowercase = lowercase + answer_list[i]
#     answer = lowercase + uppercase
#
#     return answer


print(solution(s))