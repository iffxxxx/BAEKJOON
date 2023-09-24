# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1003

import sys
input = sys.stdin.readline

Dp = [[0, 0] for i in range(41)]
Dp[0] = [1, 0]
Dp[1] = [0, 1]
for i in range(2, 41):
    for j in range(2):
        Dp[i][j] = Dp[i - 1][j] + Dp[i - 2][j]

for _ in range(int(input())):
    cnt_0 = 0
    cnt_1 = 0
    n = int(input())
    print(Dp[n][0], Dp[n][1])
    
# def fibonacci(n):
#     global cnt_0, cnt_1
#     if n == 0:
#         cnt_0 += 1
#         return 0
#     elif n == 1:
#         cnt_1 += 1
#         return 1
#     else:
#         return fibonacci(n -1) + fibonacci(n - 2)

# for _ in range(int(input())):
#     cnt_0 = 0
#     cnt_1 = 0
#     N = int(input())
#     fibonacci(N)
#     print(cnt_0, cnt_1)