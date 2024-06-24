import sys
input = sys.stdin.readline

n = int(input()) # 총 인원
t_shirt_size = list(map(int, input().split())) # 티셔츠 사이즈
T, P = map(int, input().split()) # 티셔츠와 펜의 묶음 수
t_bundle = 0 # 티셔츠 묶음

for i in t_shirt_size:
    if i % T == 0:
        t_bundle += i // T
    else:
        t_bundle += i // T + 1

print(t_bundle)
print(n // P, n % P)
