# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2294

import sys
input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())
Num = [int(input()) for _ in range(N)]

dp = [INF] * (K + 1)
dp[0] = 0

for n in Num:
    for i in range(n, K + 1):
        dp[i] = min(dp[i], dp[i - n] + 1)

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])