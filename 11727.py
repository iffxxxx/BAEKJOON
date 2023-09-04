# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/11727

import sys
input = sys.stdin.readline

N = int(input())
dp = [1] * (N + 1)

for i in range(2, N + 1):
    dp[i] = (dp[i - 2] * 2 + dp[i - 1]) % 10007

print(dp[-1])