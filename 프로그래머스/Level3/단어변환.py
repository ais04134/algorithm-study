'''

출처: https://school.programmers.co.kr/learn/courses/30/lessons/43163

'''
'''
제약조건

1. 알파벳은 소문자로만 이루어져 있음(길이는 3~10)
2. words에는 3~50개 이하의 단어가 있음, 중복 x
3. begin != target
4. 변환할 수 없는 경우 0을 return
'''
from collections import deque


def can_transform(word1, word2):
    # 두 단어가 한 글자만 차이나는지 확인
    diff_count = sum(c1 != c2 for c1, c2 in zip(word1, word2))
    return diff_count == 1


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = set()  # 이미 방문한 단어를 저장하는 집합
    queue = deque([(begin, 0)])  # 큐에 시작 단어와 현재 단계 수(0)를 넣음

    while queue:
        current_word, step = queue.popleft()  # 큐에서 현재 단어와 단계를 가져옴

        if current_word == target:
            return step  # 목표 단어에 도달한 경우 현재 단계 수를 반환

        for word in words:
            if word not in visited and can_transform(current_word, word):
                visited.add(word)  # 방문 표시
                queue.append((word, step + 1))  # 큐에 다음 단어와 단계 수를 추가

    return 0  # 변환할 수 없는 경우 0 반환