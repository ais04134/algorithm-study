import sys
input = sys.stdin.readline

t = int(input())

def func(x):
  if x==1: return 1
  elif x==2: return 2
  elif x==3: return 4
  else: return func(x-1)+func(x-2)+func(x-3)

for _ in range(t):
  n = int(input())
  
  print(func(n))