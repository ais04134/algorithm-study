"""

문제 출처: https://www.acmicpc.net/problem/18185

"""

import sys
input = sys.stdin.buffer.readline

N = int(input())
arr = list(map(int, input().split())) + [0, 0]

price = 0

for i in range(N):
    if arr[i] != 0:
        if arr[i+1] == 0:
            count = arr[i]
            arr[i] -= count
            price += 3*count
        elif arr[i+1] > arr[i+2]:
            count = min(arr[i], arr[i+1] - arr[i+2])
            arr[i] -= count
            arr[i + 1] -= count
            price += 5 * count
            count = min(arr[i], arr[i + 1], arr[i + 2])
            arr[i] -= count
            arr[i + 1] -= count
            arr[i + 2] -= count
            price += 7 * count
        else:
            count = min(arr[i], arr[i + 1], arr[i + 2])
            arr[i] -= count
            arr[i + 1] -= count
            arr[i + 2] -= count
            price += 7 * count
        price += arr[i]*3

print(price)



