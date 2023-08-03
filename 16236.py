# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/16236

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Mat = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
y, x, size = 0, 0, 2

for i in range(N):
    for j in range(N):
        if Mat[i][j] == 9:
            y, x = i, j
            Mat[i][j] = 0
            break

def BFS(y, x, size):
    visited = [[0] * N for _ in range(N)]
    queue = deque([(y, x)])
    visited[y][x] = 1
    able = []
    while queue:
        vy, vx = queue.popleft()
        for i in range(4):
            cy = vy + dy[i]
            cx = vx + dx[i]
            if 0 <= cy < N and 0 <= cx < N and visited[cy][cx] == 0:
                if Mat[cy][cx] <= size:
                    queue.append((cy, cx))
                    visited[cy][cx] = visited[vy][vx] + 1
                    if 0 < Mat[cy][cx] < size:
                        able.append((cy, cx, visited[cy][cx] - 1))
    return able

cnt = 0
answer = 0

while True:
    able = BFS(y, x, size)
    able.sort(key = lambda x : (-x[2], -x[0], -x[1]))   # pop을 사용하기 위해 역순으로
    
    if len(able) == 0:
        break
    
    else:
        y, x, dis = able.pop()
        answer += dis
        Mat[y][x] = 0
        
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0

print(answer)