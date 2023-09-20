import itertools

def Kakao_Bank(n, m, x, y, r, c, k):
    st = ""
    if abs(x-r) + abs(y-c) > k: return "impossible"
    elif (k - (abs(x-r) + abs(y-c)))%2 == 1: return "impossible"
    else:
        if x-r >= 0: st += "u"*abs(x-r)
        else: st += "d"*abs(x-r)
        if y-c >= 0: st += "l"*abs(y-c)
        else: st += "r"*abs(y-c)

        l = [st]
        for i in range((k - (abs(x - r) + abs(y - c))) // 2):
            l = sum(list(map(lambda x: [x+"lr", x+"du"], l)), [])

        ps = sorted(sum(list(map(lambda x: list(itertools.permutations(x, k)), l)), []))

        for i in ps:
            st = [x, y]
            for j in i:
                if j == "u": st[0] -= 1
                elif j == "d": st[0] += 1
                elif j == "r": st[1] += 1
                else: st[1] -= 1
                if st[0] < 1 or st[0] > n or st[1] < 1 or st[1] > m: break

            if st[0] == r and st[1] == c: return "".join(i)

print(Kakao_Bank(3, 4, 2, 3, 3, 1, 5))
print(Kakao_Bank(2, 2, 1, 1, 2, 2, 2))
print(Kakao_Bank(3, 3, 1, 2, 3, 3, 4))

def Kakao_Bank_ver2(n, m, x, y, r, c, k): #항상 최적의 값으로 이동한다. # 1. 갈수있고 2. 범위를 안넘는다
    answer = ""
    if abs(x - r) + abs(y - c) > k: return "impossible"
    elif (k - (abs(x - r) + abs(y - c))) % 2 == 1: return "impossible"
    for i in range(1, k+1): # d 아래, l 왼, r 오른, u 위
        if (k -i - (abs(x + 1 - r) + abs(y - c))) % 2 != 1 and x + 1 <= n:
            x += 1
            answer += "d"
        elif (k - i - (abs(x - r) + abs(y - 1 - c))) % 2 != 1 and y - 1 >= 1:
            y -= 1
            answer += "l"
        elif (k - i - (abs(x - r) + abs(y + 1 - c))) % 2 != 1 and y + 1 <= m:
            y += 1
            answer += "r"
        elif (k - i - (abs(x - 1 - r) + abs(y - c))) % 2 != 1 and x - 1 >= 1:
            x -= 1
            answer += "u"
    if (x, y) == (r, c): return answer
    else: return "impossible"


print(Kakao_Bank_ver2(3, 4, 2, 3, 3, 1, 5))
print(Kakao_Bank_ver2(2, 2, 1, 1, 2, 2, 2))
print(Kakao_Bank_ver2(3, 3, 1, 2, 3, 3, 4))




