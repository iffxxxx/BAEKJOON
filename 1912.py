# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1912

import sys
input = sys.stdin.readline

N = int(input())
Num = list(map(int, input().split()))

for i in range(1, N):
    Num[i] = max(Num[i], Num[i] + Num[i -1])

print(max(Num))


# 실패한 케이스 1 -  시간초과
# Sum = 0
# for i in range(N):
#     Sum += Num[i]
#     Num[i] = Sum

# max = Num[0]
# for i in range(N):
#     for j in range(i):
#         if max < Num[i] - Num[j]:
#             max = Num[i] - Num[j]

# print(max)