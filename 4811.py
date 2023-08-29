# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/4811

import sys
input = sys.stdin.readline

DP = [[0] * 31 for _ in range(31)]
for i in range(1, 31):
    DP[0][i] = 1

for i in range(1, 31):
    for j in range(i, 31):
        DP[i][j] = DP[i - 1][j] + DP[i][j - 1]

while True:
    N = int(input())
    if N == 0:
        break
    else:
        print(DP[N][N])