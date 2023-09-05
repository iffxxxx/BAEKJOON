# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/12852

import sys
input = sys.stdin.readline

N = int(input())
dp = [[0, []] for _ in range(N + 1)]
dp[1][1] += [1]

for i in range(2, N + 1):
    flag = 0
    dp[i][0] = dp[i - 1][0] + 1
    if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
        flag = 1
        dp[i][0] = dp[i // 3][0] + 1
    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        flag = 2
        dp[i][0] = dp[i // 2][0] + 1
        
    if flag == 0:
        dp[i][1] = (dp[i - 1][1]) + [i]
    elif flag == 1:
        dp[i][1] = (dp[i // 3][1]) + [i]
    else:
        dp[i][1] = (dp[i // 2][1]) + [i]

print(dp[N][0])
print(*sorted(dp[N][1], reverse= True))