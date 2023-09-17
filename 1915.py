# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1915

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
Mat = [list(map(int, list(input().rstrip()))) for i in range(n)]
Dp = [[0] * m for _ in range(n)]
    
temp = 0
for y in range(n):
    for x in range(m):
        if y == 0 or x == 0:
            Dp[y][x] = Mat[y][x]
            temp = max(temp, Dp[y][x]) # 반례
        elif Mat[y][x] == 1:
            Dp[y][x] = min(Dp[y - 1][x - 1], Dp[y - 1][x], Dp[y][x - 1]) + 1
            temp = max(temp, Dp[y][x])

# print(Dp)
print(temp ** 2)