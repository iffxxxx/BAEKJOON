# https://www.acmicpc.net/problem/2565 ภüฑ๊มู

import sys
input = sys.stdin.readline

N = int(input())
Dp = [1] * N
line = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    line.append([a, b])

line.sort()

for i in range(1, N):
    for j in range(0, i):
        if line[j][1] < line[i][1]:
            Dp[i] = max(Dp[i], Dp[j] + 1)

print(N - max(Dp))