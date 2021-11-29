'''

https://programmers.co.kr/learn/courses/30/lessons/42888

'''

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    record = list(map(lambda x:x.split(),record)) # 이런식으로 각 개체의 값을 리스트로 바꿔서 2차원으로 표현해준다.
    name_dict = {}
    answer = []
    for i in record:
        # if name_dict in not i[1]:
        #     name_dict[i[1]] = i[2]
        # else:
        #     name_dict[i[1]] = i[2]  <- 결국 덮어쓰는 형식이므로 동일하다.
        if len(i) == 3:
            name_dict[i[1]] = i[2]
    for i in record:
        if i[0] == 'Enter':
            answer.append(f"{name_dict.get(i[1])}님이 들어왔습니다.")
        elif i[0] == 'Leave':
            answer.append(f"{name_dict.get(i[1])}님이 나갔습니다.")
    return answer


print(solution(record))
