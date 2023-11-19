'''

출처: https://school.programmers.co.kr/learn/courses/30/lessons/118667

'''

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

def solution(queue1, queue2):
    # 만약 합친 값의 나머지가 1이면 절반으로 못 쪼개서 안됨 리턴
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)

    # 아니면 큰쪽에서 작은쪽으로 넘겨주는거 반복하기!

    # 큰쪽에서 작은쪽 넘겨주는거 한번 다 했는데도 단되면 못 하는 것이므로 안됨 리턴
    return sum_answer


print(solution(queue1, queue2))