# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2579

import sys
input = sys.stdin.readline

N = int(input())
Num = [int(input()) for _ in range(N)]

dp = [0] * N
if N <= 2:
    print(sum(Num))
else:
    dp[0] = Num[0]
    dp[1] = Num[0] + Num[1]
    dp[2] = max(Num[0], Num[1]) + Num[2]
    for i in range(3, N):
        dp[i] = max(dp[i - 3] + Num[i - 1], dp[i - 2]) + Num[i]

    print(dp[-1])