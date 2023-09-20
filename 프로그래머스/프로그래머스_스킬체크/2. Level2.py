'''

r_ans = 0
rr_ans = 0
def solution(n):
    global r_ans, rr_ans
    ans = [0,1,1,2]
    if n <= 3:
        rr_ans = ans[n] + r_ans
        return rr_ans
    if n%2 == 0:
        solution(n//2)
    else:
        r_ans += 1
        solution((n-1)//2)
    return rr_ans

'''

'''

def solution(n, count = 0):
    return n if bin(n).count("1") is count else solution(n+1, bin(n).count("1") if count is 0 else count)

'''