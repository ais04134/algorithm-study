# 첫 재출 결과 60.0/100

# def solution(score):
#     '''
#     :param score: 점수
#     :return: 최소 젤리 수
#     '''
#     # 사용 가능한 숫자(젤리) 집합
#     numbers = [100, 50, 5, 1]
#     # 각 점수에 대한 최소 젤리 수를 저장할 배열
#     dp = [float('inf')] * (score + 1)
#     dp[0] = 0
#
#     for i in range(1, score + 1):
#         for num in numbers:
#             if i >= num:
#                 dp[i] = min(dp[i], dp[i - num] + 1)
#
#     return dp[score]


# 두번째 재출 결과 0.0/100

# def solution(score):
#     '''
#     :param score: 점수
#     :return: 최소 젤리 수
#     '''
#     # 사용 가능한 숫자(젤리) 집합
#     numbers = [100, 50, 5, 1]
#     n = len(numbers)
#     dp = [float('inf')] * (score + 1)
#     dp[0] = 0
#
#     for i in range(1, n):
#         for j in range(numbers[i], score + 1):
#             dp[j] = min(dp[j], dp[j - numbers[i]] + 1)
#
#     return dp[score]

# 세번째 제출 결과 80.0/100

# def solution(score):
#     '''
#     :param score: 점수
#     :return: 최소 젤리 수
#     '''
#     # 사용 가능한 숫자(젤리) 집합
#     numbers = [100, 50, 5, 1]
#     dp = [0] + [-1] * (score)
#
#     for num in numbers:
#         for i in range(num, score + 1):
#             if dp[i - num] != -1 and (dp[i] == -1 or dp[i] > dp[i - num] + 1):
#                 dp[i] = dp[i - num] + 1
#
#     return dp[score]


# 마지막 제출 결과 100.0/100

def solution(score):
    '''
    :param score: 점수
    :return: 최소 젤리 수
    '''
    # 사용 가능한 숫자(젤리) 집합
    numbers = [100, 50, 5, 1]
    answer = 0

    for num in numbers:
        count = score // num # 현재 숫자로 몇 개의 젤리를 사용할 수 있는지 계산
        answer += count # 해당 숫자로 사용한 젤리 수를 더함
        score -= count * num

    return answer


# 테스트 예제
print(solution(319))
print(solution(156))
print(solution(551))