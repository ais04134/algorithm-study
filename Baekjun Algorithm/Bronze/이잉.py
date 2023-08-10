def solution(n, s): return [-1] if n>s else [s//n]*(n-s%n)+[s//n+1]*(s%n)

solution=lambda n,s:[[s//n]*(n-s%n)+[s//n+1]*(s%n),[-1]][n>s]