'''

https://www.acmicpc.net/problem/10163

'''

num = int(input())
paper = [[0 for _ in range(1001)] for _ in range(1001)]

def paper(num):
    a, b, x, y = map(int, input().split())
    for i in range(num):
        for j in range(x+1):
            for z in range(y+1):
                paper[a+j][b+z] = 1

    answer = 0
    for i in paper:
        answer += sum(i)

    return answer

paper(num)
