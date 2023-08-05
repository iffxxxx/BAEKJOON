#-*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2193

import sys
input = sys.stdin.readline

DP = [0, 1]
for i in range(89):
    DP.append(DP[i] + DP[i + 1])

print(DP)

# 시간 초과
# def PIB(N):
#     if N == 1:
#         return 1
#     elif N == 2:
#         return 1
#     else:
#         return PIB(N - 1) + PIB(N - 2)

print(DP[int(input())])