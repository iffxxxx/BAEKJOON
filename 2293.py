# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2293

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
knapsack = [1] + [0 for _ in range(K)]

Coin = []
for _ in range(N):
    c = int(input())
    Coin.append(c)

for c in Coin:
    for j in range(1, K + 1):
        if j - c >= 0:
            knapsack[j] += knapsack[j - c]

print(knapsack[K])

# 실패한 케이스 - 메모리 초과
# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         knapsack[i][j] = knapsack[i - 1][j]
        
#         if j - Coin[i - 1] >= 0:
#             knapsack[i][j] += knapsack[i][j - Coin[i - 1]]
    
# print(knapsack[N][K])