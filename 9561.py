# https://www.acmicpc.net/problem/9461

import sys
input = sys.stdin.readline

dp = [0, 1, 1, 1]
for i in range(4, 101):
    dp.append(dp[i - 3] + dp[i - 2])

# 시간초과
# def Tri(M):
#     if M == 1:
#         return 1
#     elif M == 2:
#         return 1
#     elif M == 3:
#         return 1
#     else:
#         return Tri(M - 3) + Tri(M - 2)

N = int(input())
for _ in range(N):
    print(dp[int(input())])