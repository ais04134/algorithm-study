# 1~n 까지의 합을 구하는 코드를 재귀적인 방식과 반복적인 방식으로 비교해보고
# 어떤게 더 시간 복잡도가 작은 값을 가지는지 고려해보자

def sum_recursive(n): # O(n)
    if n <= 1:
        return n
    else:
        return n + sum(n-1)

def sum_lterative(n): # O(n) <- 시간복잡도는 동일하나 계산상의 효율성은 while을 사용하는 lterative version이 더 좋다.
    s = 0
    while n >= 0:
        s += n
        n -= 1
    return s


'''
(04) 피보나치 순열
문제 설명
인자로 0 또는 양의 정수인 x 가 주어질 때, Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.

Fibonacci 순열은 아래와 같이 정의됩니다.
F0 = 0
F1 = 1
Fn = Fn - 1 + Fn - 2, n >= 2

재귀함수 작성 연습을 의도한 것이므로, 재귀적 방법으로도 프로그래밍해 보고, 반복적 방법으로도 프로그래밍해 보시기 바랍니다.

'''

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2) # 자기 자신을 불러서 반복한다는 의미

# 생각해보니 이런식으로 작성하는게 좀 더 좋을듯!
# def fibonacci_recursive2(n):
#     if n <= 1: return n
#     elif n >= 2: return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)





def fibonacci_lterative(n):
    fn_2, fn_1 = 0, 1
    if x == 0 or x == 1:
        return x
    else:
        for i in range(x):
            fn_2, fn_1 = fn_1, fn_2 + fn_1 # 다시 생각해보기
        return fn_2

print(fibonacci_recursive(10))


