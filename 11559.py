# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/11559

import sys
from collections import deque
input = sys.stdin.readline

Mat = []
for _ in range(12):
    Mat.append(list(input().rstrip()))
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def Down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if Mat[k][i] == "." and Mat[j][i] != ".":
                    Mat[k][i] = Mat[j][i]
                    Mat[j][i] = "."
                    break

def BFS(y, x):
    visited = [[0 for _ in range(6)] for _ in range(12)]
    queue = deque([(y, x)])
    visited[y][x] = 1
    
    temp.append((y, x))
    while queue:
        vy, vx = queue.popleft()
        for i in range(4):
            cy = vy + dy[i]
            cx = vx + dx[i]
            if 0 <= cy < 12 and 0 <= cx < 6 and visited[cy][cx] == 0 and Mat[cy][cx] == Mat[y][x]:
                visited[cy][cx] = 1
                queue.append((cy, cx))
                temp.append((cy,cx))

cnt = 0
while True:
    flag = 0
    for i in range(12):
        for j in range(6):
            if Mat[i][j] != ".":
                temp = []
                BFS(i, j)
                if len(temp) >= 4:
                    flag = 1
                    for a, b in temp:
                        Mat[a][b] = "."
    if flag == 0:
        break
    Down()
    cnt += 1
    
print(cnt)