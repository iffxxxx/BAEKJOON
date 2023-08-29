# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/9084

import sys
input = sys.stdin.readline

for i in range(int(input())):
    N = int(input())
    Coin = [0] + list(map(int, input().split()))
    
    M = int(input())
    
    Knapsack = [[1] + [0 for _ in range(M)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            Knapsack[i][j] = Knapsack[i - 1][j]
            
            if j - Coin[i] >= 0:
                Knapsack[i][j] += Knapsack[i][j - Coin[i]]
                
    print(Knapsack[N][M])