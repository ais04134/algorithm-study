# 100.0/100

def solution(pouches):
    '''
    :param pouches: list('주머니1', '주머니2',...), 젤리 주머니는 abced라는 5가지 종류의 젤리로 구성되어 있음
    :return: 가져갈 수 있는 최대 주머니 수
    '''
    jelly_types = "abcde"  # 가능한 젤리 종류
    answer = 0

    for jelly in jelly_types:  # 각 젤리 기준으로 반복
        pocket_count = []

        for pocket in pouches:
            pocket_count.append(pocket.count(jelly) * 2 - len(pocket))
        pocket_count.sort(reverse=True)

        max_pocket = 0  # 최대 주머니 수
        dummy_variable = 0

        for i in pocket_count:  # 특정 젤리 기준 최대 주머니 수
            dummy_variable += i

            if dummy_variable <= 0:
                break
            else:
                max_pocket += 1

        if answer < max_pocket:
            answer = max_pocket

    return answer

# 에제테스트
print(solution(["cab", "adaaa", "e"]))
print(solution(["aabb", "baba"]))
print(solution(["d", "a", "e", "d", "abdcc"]))
print(solution(["a"]))






