'''

https://programmers.co.kr/learn/courses/30/lessons/17686

'''

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

def solution(files):
    files_value = list(map(lambda x: x.lower(),files))
    files_value.sort()
    dic = dict(zip(files,files_value)) # 원래값과 정렬을 위한 값을 key, value 값으로 나눔

    for k, v in dic.items(): # value 값을 HEAD, NUMBER, TAIL 값으로 나눈 튜플로 저장
        v = [v[:"v[^0-9]"], v[4:]]
        print(v)

print(solution(files))




import re
def solution(files): return [''.join(s) for s in sorted([re.split(r"([0-9]+)", s) for s in files], key=lambda x: (x[0].lower(), int(x[1])))]