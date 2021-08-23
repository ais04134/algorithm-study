'''

def solution(a, b):
    if a == b: return a
    elif a < b: return sum(list(range(a, b+1)))
    else: return sum(list(range(b, a+1)))

'''

'''

def solution(phone_number): return (len(phone_number)-4)*"*"+phone_number[-4:]

'''