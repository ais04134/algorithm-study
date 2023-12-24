'''

문제 출처: https://www.acmicpc.net/problem/16287

<test case>
14 13
1 3 5 7 9 11 13 14 152 4 23 53 8

'''

import sys

input = sys.stdin.readline

w, n = map(int, input().split())
A = list(map(int, input().split()))
memoization = [False] * w

for i in range(n):
    for j in range(i + 1, n):
        if A[i] + A[j] < w and memoization[w - A[i] - A[j]]:
            print("YES")
            sys.exit(0)

    for j in range(i):
        if A[i] + A[j] < w:
            memoization[A[i] + A[j]] = True

print("NO")




import sys
input = sys.stdin.readline

W, A = map(int, input().split())
article_list = list(map(int, input().split()))
m = [False] * W

def Parcel(W, A, article_list):
    for i in range(A):
        for j in range(i + 1, A):
            if article_list[i] + article_list[j] < W and m[W - article_list[i] - article_list[j]]:
                print("Y")
                return "YES"


        for j in range(i):
            if article_list[i] + article_list[j] < W:
                m[article_list[i] + article_list[j]] = True

    return "NO"

print(Parcel(W, A,article_list))




# for i in range(n):
#     for j in range(i + 1, n):
#         if A[i] + A[j] < w and memoization[w - A[i] - A[j]]:
#             print("YES")
#             sys.exit(0)
#
#     for j in range(i):
#         if A[i] + A[j] < w:
#             memoization[A[i] + A[j]] = True
#
# print("NO")



# from sys import stdin
#
# input = stdin.readline
#
# W, A = tuple(map(int, input().split()))
# article_list = list(map(int, input().split()))
# article_tuple = tuple(sorted(article_list, reverse=True))
#
# def Parcel(W, A, article_tuple):
#     remaining_weight = W
#     for i in range(A):
#         one = i
#         if remaining_weight - article_tuple[one] > 0:
#             remaining_weight -= article_tuple[one]
#         elif remaining_weight - article_tuple[one] <= 0:  # 소포의 개수가 4개가 아니므로
#             break
#
#         for j in range(A-i):
#             two = min(j + 1, A - 1)
#             if remaining_weight - article_tuple[two] > 0:
#                 remaining_weight -= article_tuple[two]
#             elif remaining_weight - article_tuple[two] <= 0:
#                 remaining_weight = W
#                 break
#
#             for z in range(A-j):
#                 three = min(z + 2, A - 2)
#                 if remaining_weight - article_tuple[three] > 0:
#                     remaining_weight -= article_tuple[three]
#                 elif remaining_weight - article_tuple[three] <= 0:
#                     remaining_weight = W
#                     break
#
#                 for t in range(A-z):
#                     four = min(t + 3, A - 3)
#                     if remaining_weight - article_tuple[four] > 0:  #
#                         break
#                     elif remaining_weight - article_tuple[four] < 0:
#                         remaining_weight = W
#                     else:
#                         return "YES"
#
#     return "NO"
#
# print(Parcel(W, A, article_tuple))
#
# from sys import stdin
#
# input = stdin.readline
#
# W, A = tuple(map(int, input().split()))
# article_list = list(map(int, input().split()))
# article_tuple = tuple(sorted(article_list, reverse=True))
#
# def Parcel(W, A, article_tuple):
#     remaining_weight = W
#     for i in range(A):
#         one = i
#         if remaining_weight - article_tuple[one] > 0:
#             remaining_weight -= article_tuple[one]
#         else: break
#
#         for j in range(A-i):
#             two = min(j + 1, A - 1)
#             if remaining_weight - article_tuple[two] > 0:
#                 remaining_weight -= article_tuple[two]
#             else:
#                 remaining_weight = W
#                 break
#
#             for z in range(A-j):
#                 three = min(z + 2, A - 2)
#                 if remaining_weight - article_tuple[three] > 0:
#                     remaining_weight -= article_tuple[three]
#                 else:
#                     remaining_weight = W
#                     break
#
#                 for t in range(A-z):
#                     four = min(t + 3, A - 3)
#                     if remaining_weight - article_tuple[four] > 0:  #
#                         break
#                     elif remaining_weight - article_tuple[four] < 0:
#                         remaining_weight = W
#                     else:
#                         return "YES"
#
#     return "NO"
#
# print(Parcel(W, A, article_tuple))


# from sys import stdin
#
# input = stdin.readline
#
# W, A = tuple(map(int, input().split())) # 무게, 원소 개수
# article_list = list(map(int, input().split())) # 물품 리스트
# article_tuple = tuple(sorted(article_list))

import unittest

# W, A = (21, 7)
# article_list = [10, 1, 4, 6, 2, 8, 5] # 물품 리스트
# article_tuple = tuple(sorted(article_list))
#
#
# def Confirm_plus(i, num):
#     if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#         i[num] = i[num]+A-1 // 2 + 1
#         if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#             i.sort()
#         else:
#             i[num] = i[num]+A-1 // 2 - 1
#             if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#                 i.sort()
#             else:
#                 i[num] = i[num]+A-1 // 2
#                 if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#                     i.sort()
#
# def Confirm_minus(i, num):
#     if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#         i[num] = i[num] // 2 + 1
#         if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#             i.sort()
#         else:
#             i[num] = i[num] // 2 - 1
#             if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#                 i.sort()
#             else:
#                 i[num] = i[num] // 2
#                 if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#                     i.sort()
#
#
# def Parcel(W, A, article_tuple):
#     old_i = [0, (A - 1) // 3, 2 * ((A - 1) // 3), A - 1]
#     i = [0, (A - 1) // 3, 2 * ((A - 1) // 3), A - 1] # 선택한 물품의 시작 인덱스 값
#     answer = "_"
#     loop = 0
#     # noinspection PyUnreachableCode
#     while answer != "YES" or answer != "NO":
#         sum_w = article_tuple[i[0]]+article_tuple[i[1]]+article_tuple[i[2]]+article_tuple[i[3]]
#         if W != sum_w:
#             if W > sum_w:
#                 for j in range(4):
#                     Confirm_plus(i, j)
#                     if i != old_i:
#                         i = old_i
#                         break
#                 answer = "NO"
#                 break
#             else:
#                 for j in range(4):
#                     Confirm_minus(i, j)
#                     if i != old_i:
#                         i = old_i
#                         break
#                 answer = "NO"
#                 break
#         else:
#             answer = "YES"
#             break
#         if loop == 5:
#             answer = "NO"
#             break
#
#     return answer
#
# print(Parcel(W, A, article_tuple))

# W, A = (21, 7)
# article_list = [10, 1, 4, 6, 2, 8, 5] # 물품 리스트
# article_tuple = tuple(sorted(article_list))
#
#
# def Confirm_plus(i, num):
#     if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#         i[num] = i[num]+A-1 // 2 + 1
#         if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#             i.sort()
#         else:
#             i[num] = i[num]+A-1 // 2 - 1
#             if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#                 i.sort()
#             else:
#                 i[num] = i[num]+A-1 // 2
#                 if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#                     i.sort()
#
# def Confirm_minus(i, num):
#     if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#         i[num] = i[num] // 2 + 1
#         if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#             i.sort()
#         else:
#             i[num] = i[num] // 2 - 1
#             if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#                 i.sort()
#             else:
#                 i[num] = i[num] // 2
#                 if i[0] != i[1] != i[2] != i[3] and 0 <= i[num] <= A - 1:
#                     i.sort()
#
#
# def Parcel(W, A, article_tuple):
#     old_i = [0, (A - 1) // 3, 2 * ((A - 1) // 3), A - 1]
#     i = [0, (A - 1) // 3, 2 * ((A - 1) // 3), A - 1] # 선택한 물품의 시작 인덱스 값
#     answer = "_"
#     loop = 0
#     # noinspection PyUnreachableCode
#     while answer != "YES" or answer != "NO":
#         sum_w = article_tuple[i[0]]+article_tuple[i[1]]+article_tuple[i[2]]+article_tuple[i[3]]
#         if W != sum_w:
#             if W > sum_w:
#                 for j in range(4):
#                     Confirm_plus(i, j)
#                     if i != old_i:
#                         i = old_i
#                         break
#                 answer = "NO"
#                 break
#             else:
#                 for j in range(4):
#                     Confirm_minus(i, j)
#                     if i != old_i:
#                         i = old_i
#                         break
#                 answer = "NO"
#                 break
#         else:
#             answer = "YES"
#             break
#         if loop == 5:
#             answer = "NO"
#             break
#
#     return answer
#
# print(Parcel(W, A, article_tuple))
