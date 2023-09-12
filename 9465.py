# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    Num = [list(map(int, input().split())) for _ in range(2)]
    Dp = [[0] * (n + 1) for _ in range(2)]
    
    if n == 1:
        print(max(Num[0][0], Num[1][0]))
    else:
        Dp[0][1] = Num[0][0]
        Dp[1][1] = Num[1][0]
        Dp[0][2] = Num[1][0] + Num[0][1]
        Dp[1][2] = Num[0][0] + Num[1][1]
        for i in range(2, n + 1):
            for j in range(2):
                Dp[j][i] = max(Dp[abs(j -1)][i - 1], Dp[abs(j - 1)][i - 2]) + Num[j][i - 1]

        print(max(Dp[0][-1], Dp[1][-1]))