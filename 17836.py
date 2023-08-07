# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/17836

import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
Mat = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def BFS(y, x, g):
    queue = deque([(y, x, g)])
    visited[y][x][g] = 1
    while queue:
        vy, vx, gram = queue.popleft()
        if vy == N - 1 and vx == M - 1 and visited[vy][vx][gram] - 1 <= T:
            return visited[vy][vx][gram] - 1
        
        for i in range(4):
            cy = vy + dy[i]
            cx = vx + dx[i]
            if 0 <= cy < N and 0 <= cx < M:
                if gram == 0:
                    if Mat[cy][cx] == 0 and visited[cy][cx][gram] == 0:
                        queue.append((cy, cx, gram))
                        visited[cy][cx][gram] = visited[vy][vx][gram] + 1
                    elif Mat[cy][cx] == 2 and visited[cy][cx][gram + 1] == 0:
                        queue.append((cy, cx, gram + 1))
                        visited[cy][cx][gram + 1] = visited[vy][vx][gram] + 1
                elif gram == 1 and visited[cy][cx][gram] == 0:
                    if Mat[cy][cx] == 0 or Mat[cy][cx] == 1:
                        queue.append((cy, cx, gram))
                        visited[cy][cx][gram] = visited[vy][vx][gram] + 1
    return 'Fail'

print(BFS(0, 0, 0))