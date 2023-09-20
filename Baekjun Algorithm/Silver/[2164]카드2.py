'''
문제 출처: https://www.acmicpc.net/problem/2164

deque를 활용한 접근 방법. 
list에서, "pop", "append"를 사용하여 코드를 작성하니, 시간초과 발생.

deque와 비교 필요.
'''

import sys
from collections import deque

input = sys.stdin.readline
n = deque(range(1, int(input())+1,))

while len(n) != 1:
    n.popleft()
    n.rotate(-1)

print(n[0])
