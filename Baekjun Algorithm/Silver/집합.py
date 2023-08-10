'''

문제: https://www.acmicpc.net/problem/11723

'''


import sys
input = sys.stdin.readline

S = set()

for _ in range(int(input())):
    a = input().split()
    if a[0] == 'add': S.add(int(a[1]))
    elif a[0] == 'remove':
        if int(a[1]) in S: S.remove(int(a[1]))
    elif a[0] == 'check':
        if int(a[1]) in S: print(1)
        else: print(0)
    elif a[0] == 'toggle':
        if int(a[1]) in S: S.remove(int(a[1]))
        else: S.add(int(a[1]))
    elif a[0] == 'all': S = set([x for x in range(1, 21)])
    elif a[0] == 'empty': S.clear()

