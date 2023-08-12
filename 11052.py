# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/11052

import sys
input = sys.stdin.readline

N = int(input())
Num = [0] + list(map(int, input().split()))

DP = [0] * (N + 1)

for i in range(1, N + 1):
    DP[i] = Num[i]
    for j in range(i):
        DP[i] = max(DP[i], DP[j] +DP[i - j])
print(DP[-1])