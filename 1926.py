# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1926

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
Mat = [list(map(int, input().split())) for _ in range(n)]

def BFS(y, x):
    queue = deque([(y, x)])
    Mat[y][x] = 0
    cnt = 1
    
    while queue:
        vy, vx = queue.popleft()
        for i in range(4):
            cy, cx = vy + dy[i], vx + dx[i]
            
            if 0 <= cy < n and 0 <= cx < m and Mat[cy][cx] == 1:
                Mat[cy][cx] = 0
                queue.append((cy, cx))
                cnt += 1
    
    return cnt

answer = []
for i in range(n):
    for j in range(m):
        if Mat[i][j] == 1:
            answer.append(BFS(i, j))

print(len(answer))
if len(answer) == 0:
    print(0)
else:
    print(max(answer))