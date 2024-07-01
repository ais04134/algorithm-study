import sys
input = sys.stdin.readline

n = int(input())
arr = []
white, blue = 0, 0

for _ in range(n):
    arr.append(list(input().split()))

def cut(x, y, n):
    global white, blue
    color = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != arr[i][j]:
                cut(x, y, n // 2) # 1사분면
                cut(x, y + n // 2, n // 2) # 2사분면
                cut(x + n // 2, y, n // 2) # 3사분면
                cut(x + n // 2, y + n // 2, n // 2) # 4사분면
                return
            
    if color == '0':
        white += 1
    else:
        blue += 1

cut(0, 0, n)
print(white)
print(blue)