# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

inven = [[0, 0]]
for _ in range(N):
    W, V = map(int, input().split())
    inven.append([W, V])

for i in range(1, N + 1):
    for j in range(1, K + 1):
        W = inven[i][0]
        V = inven[i][1]
        
        if j < W:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], V + dp[i - 1][j - W])

print(dp[N][K])