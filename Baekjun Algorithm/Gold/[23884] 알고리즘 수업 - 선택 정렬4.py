'''

23884번 문제 출처: https://www.acmicpc.net/problem/23884

'''

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

print(
    N, K, A, A[:0]
)

def selection_sort(A,K):
    for i in range(K):
        if i != 0:
            max_index = A.index(max(A[:-i]))
        else:
            max_index = A.index(max(A))
        if A[max_index] > A[-(i+1)]:
            A[max_index], A[-(i+1)] = A[-(i+1)], A[max_index]
        else: return -1
        print(A)
    return A


print(selection_sort(A, K))
