def make_qwalhou_right(w: str) -> str:
    check_w = 0
    u = ''
    v = ''
    char_count = 0
    char = w[char_count]
    result = ''

    if w == "":
        return result # 공백일때 리턴

    while char_count < len(w):
        if char == '(':
            u = u + char
            check_w += 1
            char_count += 1
            char = w[char_count]
        elif char == ')':
            u = u + char
            check_w -= 1
            char_count += 1
            char = w[char_count]
        if check_w == 0:
            v = v + w[char_count:]
            break # u랑 v로 나누기

    check_u = 0
    u_answer = 'YES'

    for i in u:
        if i == '(':
            check_u += 1
        elif i == ')':
            check_u -= 1
        if check_u < 0:
            u_answer = 'NO' # u가 맞는지 판단
    if u_answer == 'YES':
        result = u + make_qwalhou_right(v)
    elif u_answer == 'NO':
        u = u[1:-1]
        for i in u:
            if i == '(':
                i == ')'
            elif i == ')':
                i == '('
        result = '(' + make_qwalhou_right(v) + ')' + u # v

    return result


w = input('괄호 문자열을 숫자가 맞게 입력해주세요.:')
print(make_qwalhou_right(w))