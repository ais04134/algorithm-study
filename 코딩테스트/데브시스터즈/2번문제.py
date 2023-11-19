# 100.0/100

def solution(capacity, routes):
    '''
    :param capacity: 들 수 있는 선물의 최대값
    :param routes: [giftNum, from, to]
    :return: true/false
    '''
    events = []  # 이벤트(선물을 넣거나 빼는 지점)를 저장할 리스트
    for gift, start, end in routes:
        events.append((start, gift))  # 선물을 넣는 이벤트
        events.append((end, -gift))  # 선물을 빼는 이벤트

    events.sort()  # 이벤트를 시간 순서대로 정렬

    current_capacity = capacity  # 현재 용량을 초기화
    for time, change in events:
        current_capacity -= change  # 이벤트에 따라 선물 양을 더하거나 빕니다.
        if current_capacity < 0:
            return False  # 용량을 초과한 경우 False 반환
    return True

# 예제 테스트
print(solution(9, [[3, 2, 6], [5, 1, 4], [1, 7, 13]]))  # True
print(solution(8, [[3, 12, 16], [8, 2, 12], [1, 14, 15]]))  # True
print(solution(20, [[5, 1, 15], [14, 3, 18], [3, 15, 21], [9, 14, 52]]))  # False
