# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/14501

import sys
input = sys.stdin.readline

N = int(input())
scd = []
for _ in range(N):
    scd.append(list(map(int, input().split())))

DP = [0] * (N + 1)

for i in range(N):
    for j in range(i + scd[i][0], N + 1):
        DP[j] = max(DP[j], DP[i] + scd[i][1])

print(DP[-1])