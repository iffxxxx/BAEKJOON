# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1890

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
Mat = [list(map(int, input().split())) for _ in range(n)]
Dp = [[0] * n for _ in range(n)]
Dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(Dp[n - 1][n - 1])
        
        dy, dx = i + Mat[i][j], j + Mat[i][j]
        
        if dy < n:
            Dp[dy][j] += Dp[i][j]
        if dx < n:
            Dp[i][dx] += Dp[i][j]