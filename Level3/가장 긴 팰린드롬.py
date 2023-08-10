'''

문제출처: https://school.programmers.co.kr/learn/courses/30/lessons/12904?language=python3

'''

s = "abcdebb"

print(s[1:3])
def solution(s):
    palindrome_list = []
    for i in range(len(s) - 1):
        if s[i - 1: i + 2] == s[i - 1: i + 2][::-1]: # 코드 전체적으로 수정 해야겠다.
            palindrome_list.append(i)
        if s[i: i + 2] == s[i: i + 1][::-1]  and i + 1<= len(s):
            palindrome_list.append([i, i+1])
    # for i in range(1, len(s)//2+ 1):
    #     for j in palindrome_list:
    #         if j is int:
    #             if s[i - 1: i + 2] != s[i - 1: i + 2][::-1]
    print(len(s))

    return palindrome_list



print(solution(s))


