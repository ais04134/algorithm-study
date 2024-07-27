import sys
from collections import deque
 
input = sys.stdin.readline
N, L = map(int, input().split())
A = list(map(int, input().split()))
deq = deque()

for i in range(N):
    while deq and (deq[-1][1] > A[i]): # 더 큰 값이 있으면 반복적으로 제거
        deq.pop() 
	
    deq.append((i + 1, A[i]))         
	
    if deq[-1][0] - deq[0][0] >= L:    
        deq.popleft()
 
    print(deq[0][1], end=' ')

