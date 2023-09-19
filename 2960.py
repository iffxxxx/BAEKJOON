# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2960

n, k = map(int, input().split())

Dp = [True for i in range(n + 1)]

cnt = 0
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if Dp[j]:
            Dp[j] = False
            cnt += 1
        if cnt == k:
            print(j)
            exit(0)