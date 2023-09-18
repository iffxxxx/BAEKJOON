# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1697

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
Dp = [0] * 100001

def BFS(start):
    queue = deque([start])
    
    while queue:
        cur_node = queue.popleft()
        
        if cur_node == k:
            print(Dp[k])
            return
        
        if cur_node - 1 >= 0 and Dp[cur_node - 1] == 0:
            Dp[cur_node - 1] = Dp[cur_node] + 1
            queue.append(cur_node - 1)
        if cur_node + 1 < 100001 and Dp[cur_node + 1] == 0:
            Dp[cur_node + 1] = Dp[cur_node] + 1
            queue.append(cur_node + 1)
        if cur_node * 2 < 100001 and Dp[cur_node * 2] == 0:
            Dp[cur_node * 2] = Dp[cur_node] + 1
            queue.append(cur_node * 2)

BFS(n)