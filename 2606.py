# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2606

import sys
from collections import deque

n = int(input())
Mat = [[] for i in range(n + 1)]
visited = [0] * (n + 1)

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    Mat[u].append(v)
    Mat[v].append(u)

def BFS():
    q = deque([1])
    visited[1] = 1
    
    while q:
        cur = q.popleft()
        for n in Mat[cur]:
            if visited[n] == 0:
                q.append(n)
                visited[n] = 1
                
    print(sum(visited) - 1)
    return

BFS()