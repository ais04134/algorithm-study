import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_set = set() # 듣도 못한 사람
b_set = set() # 보도 못한 사람

for i in range(a):
    a_set.add(input())

for i in range(b):
    b_set.add(input())

answer = list(a_set & b_set) # 듣도 보도 못한 사람
answer.sort()

print(len(answer))

for i in answer:
    print(i, end= "")