import sys
input = sys.stdin.readline

N = int(input())
time_ = list(map(int, input().split()))
time_.sort()
bummy = 0
answer = 0

for i in time_:
    bummy += i
    answer += bummy 

print(answer)