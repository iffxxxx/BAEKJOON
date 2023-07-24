# https://www.acmicpc.net/problem/2156 포도주 시식

import sys
input = sys.stdin.readline

N = int(input())
Dp = [0] * 10000
wine = [0] * 10000
for i in range(N):
    wine[i] = int(input())

Dp[0] = wine[0]
Dp[1] = wine[0] + wine[1]
Dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], Dp[1])

for i in range(3, N):
    Dp[i] = max(Dp[i - 2] + wine[i], Dp[i - 3] + wine[i - 1] + wine[i], Dp[i - 1])

print(max(Dp))