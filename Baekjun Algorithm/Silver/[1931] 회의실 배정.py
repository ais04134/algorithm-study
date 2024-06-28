import sys
input = sys.stdin.readline

N = int(input())
timeline = []

for i in range(N):
    timeline.append(tuple(map(int, input().split())))

timeline.sort(key= lambda x: (x[1], x[0])) # 종료 시간, 시작시간 기준으로 정렬
count = 1
end = timeline[0][1]

for i in range(1, N):
    if timeline[i][0]>=end:
        end = timeline[i][1]
        count += 1

print(count)