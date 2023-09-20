
# n : 전체 학생 수, lost : 체육복 없는 학생 수, reserver : 여분의 채육복을 가지고 있는 학생 수
# 여벌의 체육복을 가져온 학생이 체육복을 도난당했을 수 있다. 이때 체육복을 하나만 도난 당했다고 가정한다. 남은 체육복이 하나이기 때문에 다른 학생에게 체육복을 빌려줄 수 없다.
# 체육수업을 들을 수 있는 학생의 최댓값을 구하여라


# 탐욕법...그리고 이 문제 중복이 없다는걸 고려해서 set 자료형으로 접근하였다.
def solution(n, lost, reserve):
    reser_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)

    for i in reser_del:
        if i - 1 in lost_del:
            lost_del.remove(i - 1)
        elif i + 1 in lost_del:
            lost_del.remove(i + 1)

    return n - len(lost_del)


print(solution(5,[2,4,5],[1,3,5]))

