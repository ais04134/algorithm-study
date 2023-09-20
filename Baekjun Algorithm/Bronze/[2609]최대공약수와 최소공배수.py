import sys
from collections import deque

input = sys.stdin.readline
n = deque(range(1, int(input())+1,))

while len(n) != 1:
    n.popleft()
    n.rotate(-1)

print(n[0])